from mohawk import Sender
import requests

url = "https://prod.jdgroupmesh.cloud/stores/jdsportsuk/products/16117278?channel=iphone-app&expand=variations,informationBlocks,customisations"
content = '' #ANY CONTENT IF U NEED
content_type = 'application/json' # CONTENT TYPE

sender = Sender({'id': 'd1bdff50c5',
'key': '3442497330233aecfe132ddfbbd4d46d',
'algorithm': 'sha256'}, url, "GET", content=content, content_type=content_type)

headers = {
    "x-api-key": "4CE1177BB983470AB15E703EC95E5285",
    "X-Request-Auth": sender.request_header,
}

s = requests.Session()

r = s.get('https://prod.jdgroupmesh.cloud/stores/jdsportsuk/products/16117278?channel=iphone-app&expand=variations,informationBlocks,customisations', headers=headers)

print(r.text)
