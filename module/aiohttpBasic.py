import asyncio
import aiohttp
import json

url = "http://ws.traport.com/BrokerServices.asmx/OnDemandString"
headers = {
  'content-type': 'application/x-www-form-urlencoded'
}

data = """
request=<UserPointGetRequest_V_1_0 xmlns="http://ws.BuildTrips.com/WS/V1">
    <RequestHeader
      LanguageCode="KO"
      TestOrLive="L"
      RequestUno="11000"
      ApplySiteCode="110000-01"
      MinutesToGMT="540"
      WSPassword="trips5907"
      WSSiteCode="110000-01"
      TransactionSetID="110000-01^/members/myPoint.html^http://www.traport.com/members/changPass.html^2j4nlvki64jjqn9fuj9ncdcj0z7k2nn0^^192.168.11.15^ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"/>
    <RequestContent>
      <UpdateFromDate>2015-06-28</UpdateFromDate>
      <UpdateToDate>2016-06-28</UpdateToDate>
      <UserNo>11000</UserNo>
    </RequestContent>
  </UserPointGetRequest_V_1_0>
  &isSave=string
"""


async def fetch_page(session, url):

  url = """http://ws.traport.com/BrokerServices.asmx/OnDemandString?request=<UserPointGetRequest_V_1_0 xmlns="http://ws.BuildTrips.com/WS/V1">     <RequestHeader       LanguageCode="KO"       TestOrLive="L"       RequestUno="11000"       ApplySiteCode="110000-01"       MinutesToGMT="540"       WSPassword="trips5907"       WSSiteCode="110000-01"       TransactionSetID="110000-01^/members/myPoint.html^http://www.traport.com/members/changPass.html^2j4nlvki64jjqn9fuj9ncdcj0z7k2nn0^^192.168.11.15^ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"/>     <RequestContent>       <UpdateFromDate>2015-06-28</UpdateFromDate>       <UpdateToDate>2016-06-28</UpdateToDate>       <UserNo>11000</UserNo>     </RequestContent>   </UserPointGetRequest_V_1_0>   &amp;isSave=string"""

  headers = {
    'content-type': 'application/x-www-form-urlencoded'
  }

  data = """
  request=<UserPointGetRequest_V_1_0 xmlns="http://ws.BuildTrips.com/WS/V1">
    <RequestHeader
      LanguageCode="KO"
      TestOrLive="L"
      RequestUno="11000"
      ApplySiteCode="110000-01"
      MinutesToGMT="540"
      WSPassword="trips5907"
      WSSiteCode="110000-01"
      TransactionSetID="110000-01^/members/myPoint.html^http://www.traport.com/members/changPass.html^2j4nlvki64jjqn9fuj9ncdcj0z7k2nn0^^192.168.11.15^ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"/>
    <RequestContent>
      <UpdateFromDate>2015-06-28</UpdateFromDate>
      <UpdateToDate>2016-06-28</UpdateToDate>
      <UserNo>11000</UserNo>
    </RequestContent>
  </UserPointGetRequest_V_1_0>
  &isSave=string
  """

  params = {
    'request': ''
  }

  with aiohttp.Timeout(10):
    async with session.get(url, data=data, headers=headers) as response:
      print(response)
      print(response.status)
      assert response.status == 200
      return await response.read()


loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
  content = loop.run_until_complete(fetch_page(session, "http://python.org"))
  # print(content)