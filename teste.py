import requests 
from json2html import *

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=^BVSP&interval=5min&apikey=XIL75UDXIBUG6EKY')
response = response.json()


print(json2html.convert(json = response))

#fazer request atraves do alpha vantage e retornar um HTML 