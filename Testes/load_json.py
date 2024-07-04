import json

path = 'C:/Users/Scarlet/Desktop/rev2_Remaneja Sto Antonio e Jirau/plot.json'

with open(path) as f:
  data = json.load(f)


print(data)