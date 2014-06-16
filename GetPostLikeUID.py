import facebook
import json
import requests

AccessToken = raw_input("Access Token:")
PostID = raw_input("{Post-ID}:")
graph = facebook.GraphAPI(AccessToken)
graphresult = graph.get_object('/' + PostID +'/' + 'likes', fields='id', limit=1000)
# graphresult = graph.get_object('/' + PostID +'/' + 'attending', fields='id', limit=1000)

audiences = list()

while "next" in graphresult["paging"]:
	terminate = len(graphresult["data"])
	for k in range(0, terminate - 1):
	    uid = graphresult["data"][k]["id"]
	    audiences.append(uid)    
	getnextpageurl = graphresult["paging"]["next"]
	nextpage = requests.get(getnextpageurl)
	graphresult = json.loads(nextpage.text)

terminate = len(graphresult["data"])
for k in range(0, terminate - 1):
    uid = graphresult["data"][k]["id"]
    audiences.append(uid)    

# print graphresult
print audiences
counts = len(audiences)
print ("Members:" + str(counts))

# dump contents to file:
outputFile = "Your CSV file Path"
output = open(outputFile, "w")
print("Dumping to file...")

for i in range(0, len(audiences)):
    output.write(str(audiences[i].encode("utf-8", "ignore")) + "\n")

output.close()