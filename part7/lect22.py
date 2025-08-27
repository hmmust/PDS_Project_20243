import requests

uop_page = requests.get("https://www.google.com/search",
                        params={'q':'UOP'})
print(uop_page.status_code)
print(uop_page.content)