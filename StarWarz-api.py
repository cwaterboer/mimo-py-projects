import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data=[]
  
  try:
    response = requests.get(url)
    response.raise_for_status()
  
    data = response.json()
  except requests.HTTPError as e:
    return None

  return data

option = input("What data would you like to explore?").strip().lower()

data = fetch_data(option)

if data:
  for dat in data:
    print(dat["name"])
else:
    print("Unable to download data")
