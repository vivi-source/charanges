import re

text = "The ghost that says boo haunts the loo"
print(text)

match = re.findall(".oo", text, re.IGNORECASE)
print(match)
