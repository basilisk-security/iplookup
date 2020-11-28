import requests
import json

print(f"""

___  __   __                      __   ___     __         ___       ___ 
 |  /  \ /  \ |        |\/|  /\  |  \ |__     |__) \ /     |  |__| |__  
 |  \__/ \__/ |___     |  | /~~\ |__/ |___    |__)  |      |  |  | |___ 

=====================================================================================
                _   _ _____         _        _____            _ _ _   _             
     /\         | | (_)  __ \       | |      / ____|          | (_) | (_)            
    /  \   _ __ | |_ _| |__) |__  __| | ___ | |     ___   __ _| |_| |_ _  ___  _ __  
   / /\ \ | '_ \| __| |  ___/ _ \/ _` |/ _ \| |    / _ \ / _` | | | __| |/ _ \| '_ \ 
  / ____ \| | | | |_| | |  |  __/ (_| | (_) | |___| (_) | (_| | | | |_| | (_) | | | |
 /_/    \_\_| |_|\__|_|_|   \___|\__,_|\___/ \_____\___/ \__,_|_|_|\__|_|\___/|_| |_|

=====================================================================================

""")
ip_add = input("targets IP: ")

response = requests.get(f'http://ip-api.com/json/{ip_add}').content

data = json.loads(response)

print("keep in mind IP's do not give an accurate location, it's only a rough estimate")
print(f"""
[#]IP: {data['query']}
[#]ping: {data ['status']}
[#]country: {data['country']}
[#]region: {data['region']}
[#]region name: {data['regionName']}
[#]city: {data['city']}
[#]zip code: {data['zip']}
[#]latitude: {data['lat']}
[#]longitude: {data['lon']}
[#]internet service provider: {data['isp']}

""")
