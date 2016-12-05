import urllib
import urllib3
import json

# curl -i -X POST \
#  -d "installed=true" \
#  -d "name=batchTester" \
#  -d "permissions=email" \
#  -d "access_token=672419332894995%7CHlgRhYGCU6KSTLbuR8_OG1DbXOw" \
#  "https://graph.facebook.com/v2.8/274927602644172/accounts/test-users"


url = 'https://graph.facebook.com/v2.8/274927602644172/accounts/test-users'

body = {
    'installed': True,
    'name': 'batchTester',
    'permissions': 'email',
    'access_token': '672419332894995%7CHlgRhYGCU6KSTLbuR8_OG1DbXOw',
}

http = urllib3.PoolManager()
r = http.request(
    'POST',
    url,
    fields=body,
)

jd = json.loads(r.data.decode('utf-8'))
print '=='
print r