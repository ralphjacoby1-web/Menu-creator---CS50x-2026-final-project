from flask import render_template

def ars(value):
    """
    Turns float value into argentinian pesos
    """
    
    return f"ARS${value}"

def validate_string(string):
    """
    Checks if string is empty or only space characters
    """
    return bool(string and string.strip())

def show_error(error_msg):
    """
    Shows error template with error message
    """
    return render_template("error.html", error = error_msg)

def validate_price(price):
    """
    Validates that price inserted is higher than or equals to 0. And checks if it is float.
    """
    
    try:
        price = float(price)
        
        if price < 0:
            return False
        
        return True
        
    except ValueError:
        
        return False