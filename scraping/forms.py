import re

import requests
from bs4 import BeautifulSoup

# Fetch the form
response = requests.get("https://httpbin.org/forms/post")
# Parse the page
page = BeautifulSoup(response.text, "html.parser")
# grab the form
form = page.find("form")

# A regexp for grabbing the fields that we want from the form
wanted_fields = re.compile("(input|textarea)")

# A set for all the unique input names in the  form
input_names = set()

# Find all occurences of either input or textarea in the
# forma dn grab the name of the element
for field in form.find_all(wanted_fields):
    input_names.add(field.get("name"))

print(input_names)