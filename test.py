import ujson

test_dict = {
  "name" : "이새로찬",
  "phone" : "01075655582",
  "num": 1
}

rs = ujson.dumps(test_dict)
print(type(rs))
print(rs)


by = b"\uc774"
print(type(by))

rs = by.decode('utf-8')
print(type(rs))



#
#
# reqBody = """{'domainInfo': '192.168.11.64:3000', 'emailType': 'bookingComplete', 'data': '{"countryNameEN":"Vietnam","hotelHomepageURL":null,"sellerCompName":"\\ud2b8\\ub798\\ube14\\ud558\\uc6b0 \\uc608\\uc57d\\uc13c\\ud130","sellerNotice":null,"inclusionItems":"\\uc870\\uc2dd \\ud3ec\\ud568. \\ubb34\\uc120 \\uc778\\ud130\\ub137 \\ud3ec\\ud568.","vendorBookingItemCode":"267795352","currencyCode":"KRW","sellerCompCode":"200000","roomCount":1,"checkInDate":1472515200,"checkInInstructions":"<p><b>\\ucd9c\\ubc1c \\uc804 \\uc54c\\uc544\\ub458 \\uc0ac\\ud56d<\\/b> <br \\/><ul>  <li>\\uc774 \\uc219\\ubc15 \\uc2dc\\uc124\\uc740 \\uacf5\\ud56d\\uc5d0\\uc11c\\uc758 \\uad50\\ud1b5\\ud3b8\\uc744 \\uc81c\\uacf5\\ud569\\ub2c8\\ub2e4(\\ubcc4\\ub3c4\\uc758 \\uc694\\uae08\\uc774 \\uc801\\uc6a9\\ub420 \\uc218 \\uc788\\uc74c). \\uace0\\uac1d\\uaed8\\uc11c\\ub294 \\uc608\\uc57d \\ud655\\uc778\\uc5d0 \\ub098\\uc640 \\uc788\\ub294 \\uc5f0\\ub77d\\ucc98 \\uc815\\ubcf4\\ub85c \\ub3c4\\ucc29 24\\uc2dc\\uac04 \\uc804 \\uc219\\ubc15 \\uc2dc\\uc124\\uc5d0 \\uc5f0\\ub77d\\ud558\\uc5ec \\ub3c4\\ucc29 \\uc138\\ubd80 \\uc0ac\\ud56d\\uc744 \\uc54c\\ub824\\uc8fc\\uc154\\uc57c \\ud569\\ub2c8\\ub2e4. <\\/li> <li>\\uc774 \\uc219\\ubc15 \\uc2dc\\uc124\\uc740 \\uc548\\ub0b4\\uacac\\uc744 \\ube44\\ub86f\\ud55c \\ubaa8\\ub4e0 \\uc560\\uc644\\ub3d9\\ubb3c\\uc758 \\ucd9c\\uc785\\uc744 \\uae08\\uc9c0\\ud558\\uace0 \\uc788\\uc2b5\\ub2c8\\ub2e4. <\\/li> <\\/ul><\\/p><p><b>\\uc694\\uae08<\\/b> <br \\/><p>\\uc11c\\ube44\\uc2a4 \\uc774\\uc6a9 \\uc2dc \\ub610\\ub294 \\uccb4\\ud06c\\uc778\\/\\uccb4\\ud06c\\uc544\\uc6c3 \\uc2dc \\uc219\\ubc15 \\uc2dc\\uc124 \\uce21\\uc5d0\\uc11c \\uccad\\uad6c\\ud558\\ub294 \\uc694\\uae08 \\ubc0f \\ubcf4\\uc99d\\uae08\\uc740 \\ub2e4\\uc74c\\uacfc \\uac19\\uc2b5\\ub2c8\\ub2e4. <\\/p> <ul>     <li>\\uacf5\\ud56d \\uc154\\ud2c0 \\uc694\\uae08: \\ucc28\\ub7c9 1\\ub300\\ub2f9 VND 403200(one-way)<\\/li>             <\\/ul> <p>\\uc704 \\ubaa9\\ub85d\\uc5d0 \\uba85\\uc2dc\\ub418\\uc9c0 \\uc54a\\uc740 \\ub2e4\\ub978 \\ud56d\\ubaa9\\uc774 \\uc788\\uc744 \\uc218\\ub3c4 \\uc788\\uc2b5\\ub2c8\\ub2e4. \\uc694\\uae08 \\ubc0f \\ubcf4\\uc99d\\uae08\\uc740 \\uc138\\uc804 \\uae08\\uc561\\uc77c \\uc218 \\uc788\\uc73c\\uba70 \\ubcc0\\uacbd\\ub420 \\uc218 \\uc788\\uc2b5\\ub2c8\\ub2e4. <\\/p><\\/p>","childCount":0,"chargeCondition":[{"vendorToTime":"2016-08-29 18:00","vendorCurrencyCode":"USD","sellerCurrencyCode":"KRW","sellerToTime":"2016-08-26 17:30:00","vendorCancelChargeAmount":0,"sellerCancelChargeAmount":0,"vendorFromTime":"2016-06-07 15:43:15","sellerFromTime":"2016-06-05 15:43:15"},{"vendorToTime":"2016-08-30 18:00","vendorCurrencyCode":"USD","sellerCurrencyCode":"KRW","sellerToTime":"2016-08-29 17:30:00","vendorCancelChargeAmount":6000,"sellerCancelChargeAmount":0,"vendorFromTime":"2016-08-30 18:00","sellerFromTime":"2016-08-29 00:00:00"}],"travelers":[{"gender":"M","lastName":"lee","localFullName":"\\uc774\\uc0c8\\ub85c\\ucc2c","paxTypeCode":"ADT","firstName":"selo"}],"sellerRoomTypeName":null,"clientRequest":null,"hotelNameEN":"May De Ville Legend Hotel","vendorCompName":"EAN","sellerLogoImage":null,"cityNameEN":"Hanoi","hotelDefaultImage":"http:\\/\\/media.expedia.com\\/hotels\\/7000000\\/6010000\\/6004400\\/6004311\\/6004311_94_b.jpg","hotelPhoneNo":null,"checkOutDate":1472601600,"hotelAddress":"1 Hai Tuong Lane, 24 Ta Hien Street Hoan Kiem District","serllerPhoneNo":"1544-8812","hotelPostalCode":"","adultCount":1,"vendorCompCode":"200041","amountSum":7200,"numOfNight":1,"vendorBookingCode":"130181774748"}'}"""
# print(reqBody)
# print(type(reqBody))
#
# endcode_str = reqBody.decode("utf-8")
# print(endcode_str)
# print(type(endcode_str))