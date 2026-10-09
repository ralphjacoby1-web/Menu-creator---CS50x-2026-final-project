# Menu creator

#### Video demo: https://youtu.be/bsh4LobLrU4

#### Description:

Menu creator is a web-based app that has the task to take categories and products and turn them into a well designed pdf.
Its pupose is to make it easier for restaurant owners to create menus for their restaurants. Normally some of them have to 
create them in word, or even worse, in paper. That's why this system exists, to leave restaurant owners to focus on the most
important thing about restaurants: Food.

## How it works

1. User enter Menu Creator
2. Adds as many categories and product as he wants
3. Asigns names to the categories
4. Asigns names, prices and description to products
5. Clicks on submit
6. Html page is rendered
7. Turns it into pdf
8. User downloads pdf

## Files

### 'app.py'

This part is the one in charge of taking the inputs of the user on the frontend and converting it into a dictionary of dictionarys that stores everything.
It also renders the index.html file when the request method is GET.
It renders an error file when some input is invalid.

### 'helpers.py'

It has some functions to help with how clean the code is.

The functions are:

ars: This takes the float values input by the user and turns it into argentinian pesos.

validate_string: validates if string is empty or it has only space characters.

show_error: displays an html file called "error.html"

validate_price: valides if price input by user is less than 0 or if it isn't a float value.

### 'static/script.js'

In charge of letting the user add new categories or products.

### 'templates/index.html'

Designed with full boostrap, it is in charge of rendering the interface for the user to create menus.

### 'templates/menu.html'

HTML template to display the menu created, fully designed with boostrap as well.

### 'templates/error.html'

Template called when function show_error is called. Displays what kind of error occurred.

## Design decisions

### Linking products to categories

Flask receives every input as flat lists, so products and categories arrive separately.
To link them, JavaScript gives each category a unique key (c0, c1...) and each product
stores the key of its category in a hidden input.

### Same name in many inputs

Since the user can add as many inputs as he wants, inputs of the same type share the same
name and I read them with request.form.getlist(), then go through them together with zip().

### Using the template tag

The HTML template tag lets me write the structure of a category or product once, and
JavaScript clones it every time the user clicks a button.

### Validating in the backend

The inputs are required in the HTML, but I also validate everything in app.py, because
anyone can change the HTML from the browser.

### Generating the PDF

I used window.print(), which keeps the design and lets the user save the menu as a PDF.

### No database

The menu is not saved, to keep the project simple.

## Possible improvements

Eventually, I would like to add some functions like the following:

- Choose between various templates
- Add a QR code linked to the menu
- Choose between different currencies
- Adding images of every product
- Being able to edit existing menus
- Login

## Acknowledgements

For this project I used:

- Boostrap
- Python
- JS
- HTML
- Flask
- Jinja

The AI-tool that helped me throughout this final project was Claude.
It helped me with:

Design decisions on frontend and backend and some JS functionalities.
