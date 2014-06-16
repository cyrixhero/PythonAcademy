import requests
import json

ACCESS_TOKEN = 'Your facebook access_token'
base_url = 'https://graph.facebook.com/691655927568347/likes'
fields = 'id&limit=1000'
url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)
# print url

# Interpret the response as JSON and convert back
# to Python data structures
# content = requests.get(url).json()
content = requests.get(url)
raw = json.loads(content.text)
terminate = len(raw["data"])

a = list()
for k in range(0, terminate - 1):
    UID = raw["data"][k]["id"]
    print("Processing: " + str(k + 1) + " of " + str(terminate))
    a.append(UID)
print terminate
print a

# dump contents to file:
outputFile = "Your CSV file Path"
output = open(outputFile, "w")
print("Dumping to file...")

for i in range(0, len(a)):
    output.write(str(a[i].encode("utf-8", "ignore")) + "\n")

output.close() 

# Pretty-print the JSON and display it
# print json.dumps(content, indent=1)
