# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.github.com/events"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.get('http://httpbin.org/get', params=payload)
r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# sending get request and saving the response as response object 
#r = requests.get(url = URL)
  
# extracting data in json format 
#data = r.url() 

print(r.text)
  
"""  
# extracting latitude, longitude and formatted address  
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address)) 
"""