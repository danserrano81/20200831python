import http.client

conn = http.client.HTTPSConnection("brianiswu-nflarrest-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "brianiswu-nflarrest-v1.p.rapidapi.com",
    'x-rapidapi-key': "dee532eb92msh538d09fc71698fcp1a77ddjsnb6b931ca749f"
    }

conn.request("GET", "/crime/topTeams/%7Bcrimeid%7D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
