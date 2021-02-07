import requests
import json
import itertools
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"




holding_symbols = ["AAPL","AMZN","AAL"]
country_codes = ['US']

options = {
    "symbol":holding_symbols,
    "region":country_codes
}


headers = {
    'x-rapidapi-key': "d5e95517a2msh75c98018c625d82p12ab5ejsndd559dc778fd",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }


keys = options.keys()
values = (options[key] for key in keys)
query_strings = [dict(zip(keys, combination)) for combination in itertools.product(*values)]


response_objs = []
for query in query_strings:
    response = requests.request("GET",url,headers=headers,params=query)
    response_obj = json.loads(response.text)
    response_objs.append(response_obj)

print(response_objs)





