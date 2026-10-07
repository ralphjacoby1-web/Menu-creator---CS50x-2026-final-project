from flask import Flask, render_template, request

from helpers import *

app = Flask(__name__)

app.jinja_env.filters["ars"] = ars

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Depending on method it chooses wether to render template or process user input.
    """
    
    if request.method == "GET":
        return render_template("index.html")
    
    
    restaurant_name = request.form.get("restaurant-name")
    
    if not validate_string(restaurant_name):
        return show_error("Restaurant name")
    
    try:
        menu = build_menu(request.form)
    except ValueError as error:
        return show_error(str(error))

    return render_template("menu.html", menu=menu, restaurant_name = restaurant_name)


def build_menu(form):
    """
    Extracts values from form and organizes them inside a dictionary
    """
        
    category_keys = form.getlist("category_key")
    category_names = form.getlist("category-name")
    
    if not category_keys:
        raise ValueError("categories")
    
    if len(category_names) != len(category_keys):
        raise ValueError("missing categories")
    
    product_names =form.getlist("product-name")
    product_categories = form.getlist("product-category")
    product_descriptions =form.getlist("product-description")
    product_prices = form.getlist("product-price")
    
    if len(product_categories) != len(product_names) or len(product_names) != len(product_prices) or len(product_prices) != len(product_descriptions):
            raise ValueError("missing values")
            
    menu = {}
    
    for key, category in zip(category_keys, category_names):
        if not validate_string(category):
            raise ValueError("Category name missing")
        menu[key] = {"name": category, "products": {}}
        
    for category, name, price, description in zip (
        product_categories,product_names,
        product_prices, product_descriptions):
        
        if category not in menu:
            raise ValueError("category does not exist")
        
        if not category or not name or not price:
            raise ValueError("missing value")
        
        if not validate_price(price):
            raise ValueError("invalid price")

        menu[category]["products"][name] = {"price": ars(price), "description": description}
    
    return menu