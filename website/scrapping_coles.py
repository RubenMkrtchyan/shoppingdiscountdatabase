# Author: The Vinh Ly
# Date: 25/07/2022
from inspect import classify_class_attrs
from pydoc import classname
from bs4 import BeautifulSoup
from idna import alabel
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

# target detail class name
arg_detail = {
    'name': 'product-name',
    'brand': 'product-brand',
    'price': 'price-container',
    'info': 'product-info',
    'discount': 'discount-text',
    'saved': 'product-save-value'
}

source_of_products = {
    'tab': []
}

saved_data = {
    'name': [],
    'brand': [],
    'price': [],
    'info': [],
    'discount': [],
    'saved': []
}

# get the source file
url = "https://shop.coles.com.au/a/national/everything/browse"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

html = driver.page_source
# get the data
soup = BeautifulSoup(html.lower(), "html.parser")

# print(list(arg_detail.values())[0])
for _ in range(len(arg_detail)):
    # search for each detail
    for el in soup.find_all('span', {'class', list(arg_detail.values())[_]}):
        saved_data[list(saved_data.keys())[_]].append(el.get_text())

for _ in saved_data.items():
    print('---------o0o-----------')
    print(_)


# Collecting data
    #
 
# Location
    # base on VIC, Sydney
    # 


# Sorting
    # 3 advertisement
    # most discount
    # less discount
# Filtering
    # 