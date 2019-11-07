import requests
import urllib.parse

api="https://geocoder.api.here.com/6.2/geocode.json?"
end1=input("Digite o primeiro endereço: ")
url = api+urllib.parse.urlencode ({"app_id":"iXivJUgwxkvkXv8UvSib", "app_code":"cb-TIUT6f369Mp921G4kjA", "searchtext":end1})
dados=requests.get(url).json()
local1 = dados["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
print (local1)

end2= input("Digite o endereço 2: ")
url2 = api+urllib.parse.urlencode ({"app_id":"iXivJUgwxkvkXv8UvSib", "app_code":"cb-TIUT6f369Mp921G4kjA", "searchtext":end2})
dados2=requests.get(url2).json()
local2 = dados2["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
print (local2)

api_rota="https://route.api.here.com/routing/7.2/calculateroute.json?"
url_rota = api_rota+urllib.parse.urlencode ({"app_id":"iXivJUgwxkvkXv8UvSib", "app_code":"cb-TIUT6f369Mp921G4kjA", "waypoint0":str(local1["Latitude"])+','+str(local1["Longitude"]),"waypoint1":str(local2["Latitude"])+','+str(local2["Longitude"]), "mode":"fastest;car;traffic:enabled", "departure":"now", "Language":"pt-BR"})
print (url_rota)
dados_rota=requests.get(url_rota).json()
print (dados_rota)
print("#")
print("#")
print("#")
print("#")
tempoRota = dados_rota["response"]["route"][0]["summary"]["text"]
print(tempoRota)
