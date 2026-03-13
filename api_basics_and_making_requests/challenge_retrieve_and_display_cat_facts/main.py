import requests

def print_three_cat_facts():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    cat_fact = data.get('fact', 'No fact available')
    print (cat_fact)

x=3
while x>0:      
    print_three_cat_facts()
    x-=1
