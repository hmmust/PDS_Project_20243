import requests
from pyquery import PyQuery as pq

doc = pq(url="https://www.kooora.com/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D9%85%D9%88%D8%A7%D8%B9%D9%8A%D8%AF-%D9%86%D8%AA%D8%A7%D8%A6%D8%AC/2025-08-26")
print(pq(doc("title")).text())
print(pq(doc(".fco-short-name")).text())