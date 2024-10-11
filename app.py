import requests

apiKey = "f57f9cfa0534813b251841de81c52b6f"
apidata1=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=52.05&lon=1.15&appid={apiKey}')
localdata=apidata1.content.strip()
print(localdata)