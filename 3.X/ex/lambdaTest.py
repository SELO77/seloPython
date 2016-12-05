result = (lambda x: x**2)(10)
print(result)

resultList = list(map(lambda x:x**2, range(0,10)))
print(resultList)

# resultList = list(map(lambda x:x={}, range(0,4)))


{
  "method": "search",
  "apikey": "MrGMb0FuIBR2QwDhMtYZG7vCARPb7jmUbrjC5Ss7PXg",
  "service": "hotels.roomList",
  "condition": {
    "hotelCode": "JPTYO0001",
    "checkInDate": "2016-05-16",
    "checkOutDate": "2016-05-17",
    "roomCount": 2,
    "adultCount": 4,
    "childCount": 2,
    "childAges": "14-iterator,generator,16"
  }
}


{
  "service": "hotels.roomList",
  "apiKey": "MrGMb0FuIBR2QwDhMtYZG7vCARPb7jmUbrjC5Ss7PXg",
  "currencyCode": "KRW",
  "condition": {
    "childAges": null,
    "hotelCode": "JPTYO0001",
    "childCount": "0",
    "checkOutDate": "2016-04-20",
    "roomCount": "1",
    "checkInDate": "2016-04-19",
    "adultCount": "2"
  },
  "languageCode": "KO",
  "method": "search",
  "userNo": null,
  "timeZone": "Asia/Seoul"
}