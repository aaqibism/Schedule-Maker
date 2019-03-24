import urllib.request
import json

response = ""
response = urllib.request.urlopen('https://web-app.usc.edu/web/soc/api/depts/20191')
data = json.load(response)
strResponse = str(response.read())
print(type(data))
arrCode = []

val = 0
while (strResponse.find("code", val) != -1):
    indexCode = strResponse.find("code", val)
    indexName = strResponse.find("name", val)
    indexType = strResponse.find("type", val)
    if (strResponse[indexType+7] != 'Y'):
        arrCode.append(strResponse[indexCode+7:indexName-4])
    val = indexType+1
