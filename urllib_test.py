import urllib
# import urllib2

# url = curl -X POST -F "id=https://www.mymusictaste.com/campaign/%EC%83%A4%EC%9D%B4%EB%8B%88-SHINee-x-Jakarta-Indonesia,1344/" -F "scrape=true" https://graph.facebook.com
url = "https://graph.facebook.com"
param_id = "https://www.mymusictaste.com/campaign/%EC%83%A4%EC%9D%B4%EB%8B%88-SHINee-x-Jakarta-Indonesia,1344/"
is_scrape = "true"
values = {
    'id': param_id,
    'scrape': is_scrape,
}

# res = urllib.urlopen(url, urllib.urlencode(values))
# print res.read()
urllib.urlopen(url, urllib.urlencode(values))

# req = urllib2.Request(url, data=urllib.urlencode(values))
# res = urllib2.urlopen(req, timeout = 10)