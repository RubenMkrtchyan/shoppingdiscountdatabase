from flask import Blueprint, render_template
import json
import os
import math

cwd = os.getcwd()

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/products')
def products():
    f = open(cwd + '\website\coles.json', 'r')

    print(f)
    data = json.loads(f.read())

    print(data["products"])
    
    products = data["products"]
    for i in products:
        print(i)

    products_size = len(products)
    col_setting = [math.ceil(products_size/2), math.ceil(products_size/3), math.ceil(products_size/4), math.ceil(products_size/5), math.ceil(products_size/6)]

    return render_template('products.html', products=products, len = col_setting)

@views.route('/about-us')
def aboutUs():
    return render_template('aboutus.html')