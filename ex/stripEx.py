tempTxt = """
                # <BookingInformation xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://xml.hotelpass.com/HTPWS_V04SCHEMA/Response/HotelBooking_Response.xsd">	<BaseInformation WHC_RefNo="1603230188-1" Agent_RefNo="2-00226">		<BookingStatus>08</BookingStatus>       <TotalAmount Currency="USD" Exchange="1176.8400" TotalWon="25890.48">22.0000</TotalAmount>		<CXLDeadDate Guarantee="2">20160624</CXLDeadDate>	</BaseInformation>	<RequestInformation ServiceCode="MYKUL150SV000029">		<City CityCode="MYKUL">Kuala Lumpur</City>		<Hotel HotelCode="MYKUL150">D`Oriental Inn</Hotel>		<Date InDate="20160701" OutDate="20160702"/>		<RoomCnt SGLCnt="1" DBLCnt="0" TWNCnt="0" TRPCnt="0"/>		<RoomType>DOUBLE STANDARD</RoomType>		<Meal>ROOM ONLY</Meal>	</RequestInformation><Error ErrorYN=''> <ErrorDesc Code=''></ErrorDesc></Error></BookingInformation>"""

result = tempTxt.strip()
print(result)