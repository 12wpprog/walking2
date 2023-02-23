import requests
import pandas

url = 'https://covid19.ddc.moph.go.th/api/Cases/today-case-by-provinces'

res = requests.get(url)

data = res.json()

df = pandas.json_normalize(data)

print(df)

 