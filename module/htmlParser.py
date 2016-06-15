import html

str_template = """
<?xml version="1.0" encoding="utf-8"?>
<string xmlns="http://www.hotelpass.com/HTPWS_V04">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;HotelRateResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://xml.hotelpass.com/HTPWS_V04/SCHEMA/Response/HotelRateSearch_Response.xsd"&gt;&lt;RequestInfo Type='0' Description='Hotel Rate Request'&gt; &lt;RequestCode&gt;JPTYO399SV000008&lt;/RequestCode&gt; &lt;InDate&gt;20160830&lt;/InDate&gt; &lt;OutDate&gt;20160831&lt;/OutDate&gt; &lt;RoomCnt SGLCnt="0" DBLCnt="1" TWNCnt="0" TRPCnt="0"&gt;&lt;/RoomCnt&gt;&lt;/RequestInfo&gt;&lt;HotelRateInformation HotelCode="JPTYO399" AreaCode="01" AreaName="Asia"&gt;Villa Fontaine Tokyo Hatchobori&lt;HotelInformation&gt; &lt;CityName&gt;Tokyo&lt;/CityName&gt; &lt;HotelName&gt;&lt;![CDATA[Villa Fontaine Tokyo Hatchobori]]&gt;&lt;/HotelName&gt; &lt;BaseInformation&gt;     &lt;Grade&gt;★★★&lt;/Grade&gt;     &lt;Address&gt;&lt;![CDATA[3-3-3 Kayaba-Cho, NihomBashi, Chuo-ku, Tokyo, Japan]]&gt;&lt;/Address&gt;     &lt;TEL&gt;81 3 5651 6660&lt;/TEL&gt;     &lt;FAX&gt;81 3 5651 6777&lt;/FAX&gt; &lt;/BaseInformation&gt; &lt;HotelImage&gt;     &lt;Image_01&gt;http://image.hotelpass.com/JPTYO3991.jpg&lt;/Image_01&gt;     &lt;Image_02&gt;http://image.hotelpass.com/JPTYO3992.jpg&lt;/Image_02&gt;     &lt;Image_03&gt;http://image.hotelpass.com/JPTYO3993.jpg&lt;/Image_03&gt;     &lt;Image_04&gt;http://image.hotelpass.com/JPTYO3994.jpg&lt;/Image_04&gt;     &lt;Image_05&gt;http://image.hotelpass.com/JPTYO3995.jpg&lt;/Image_05&gt; &lt;/HotelImage&gt; &lt;Description&gt;     &lt;HotelDesc&gt;&lt;![CDATA[빌라폰테누 도쿄 핫쵸보리는 모던하면서도 심플한 인테리어에 최신 시설과 설비를 갖춘 도심형 호텔로 도쿄 고급 쇼핑가 긴자를 시작으로 도쿄역, 츠키지 시장들과 인접해있다.

슈퍼리어룸은 약 16m² 너비의 스텐다드 타입 룸이지만 폭 140cm 사이즈 침대를 비치하여 편안하게 쉴 수 있는 공간으로 조성했으며 힐링룸은 하루의 피로를 해소할 수 있도록 릴렉스 효과를 최대화해 저반발 베게와 매트 등 최신설비를 비치하고 있다.

또한 무료 인터넷 회선 (광랜 방식)을 설치했으며 객실내 LCD TV를 통해 신작 영화나 음악, 스포츠등 풍부한 컨텐츠(100 채널)를 1,000엔 정액으로 마음껏 즐길 수 있다. 그외 조식 무료 서비스와 복사 &amp; 팩스서비스를 제공한다.

가야바쵸역 2번 출구에서 도보 3분거리에 있다.

★ 객실안내 ★
■ 스탠다드(=수페리어) 더블: 16㎡, 침대폭 140cm

* 체크인  15시 체크아웃  11시
]]&gt;&lt;/HotelDesc&gt;     &lt;Traffic&gt;&lt;![CDATA[* 핫쵸보리역 히비야센 A5출구 도보 약 3분/JR 케이요센 B1출구 도보 약 5분&lt;br&gt;
* 히비야센/도자이센 가야바쵸역 2번 출구 도보 약 3분&lt;br&gt;
* 아사쿠사센 다카라쵸역 A2출구 도보 약 10분&lt;br&gt;
* 니혼바시역 약 800미터
* 나리타공항&lt;br&gt;
- 게이세이센 스카이라이너 이용 우에노역 하차, 히비야센으로 환승 후 핫쵸보리역 하차 (약 70분 소요)&lt;br&gt;
- JR 나리타 익스프레스 이용 도쿄역 하차, JR 케이요센으로 환승 후 핫쵸보리역 하차 (약 80분 소요)&lt;br&gt;
* 하네다공항&lt;br&gt;
- 게이힌급행(도에이 아사쿠사센 직통)이용 히가시긴자역 하차, 히비야센으로 환승 후 핫쵸보리역 하차(약 45분 소요)&lt;br&gt;
- 게이힌급행(도에이 아사쿠사센 직통)이용 니혼바시역(약 35분) 하차, 도자이센 환승 후 가야바쵸역(약 2분) 하차&lt;br&gt;
]]&gt;&lt;/Traffic&gt;     &lt;Location&gt;&lt;![CDATA[가야바쵸역에서 도보 3분거리에 있으며 니혼바시가야바초(日本橋茅場町) 중심에 위치.]]&gt;&lt;/Location&gt;     &lt;Addition&gt;&lt;![CDATA[Parking]]&gt;&lt;/Addition&gt;     &lt;RoomConven&gt;&lt;![CDATA[Air Conditioning,Minibar/Mini-Refrigerator ,Hair Dryer,TV/Cable TV/Movie,Private Bath,Internet Access]]&gt;&lt;/RoomConven&gt; &lt;/Description&gt;&lt;/HotelInformation&gt;&lt;RateInformation&gt; &lt;RoomType Code="R02"&gt;&lt;![CDATA[STANDARD]]&gt;     &lt;MealType Code="M01"&gt;&lt;![CDATA[BF INC]]&gt;         &lt;ServiceCode&gt;JPTYO399SV000008&lt;/ServiceCode&gt;         &lt;Condition&gt;&lt;![CDATA[]]&gt;&lt;/Condition&gt;         &lt;NightLimit&gt;&lt;/NightLimit&gt;         &lt;CxlDeadDate&gt;20160614&lt;/CxlDeadDate&gt;         &lt;Guarantee Code=""&gt;&lt;![CDATA[]]&gt;&lt;/Guarantee&gt;         &lt;TotalAmount Currency="JPY" Exchange="11.2700" TotalWon="199479"&gt;17700.0000&lt;/TotalAmount&gt;         &lt;Available&gt;R&lt;/Available&gt;     &lt;/MealType&gt; &lt;/RoomType&gt;&lt;Error ErrorYN=''&gt; &lt;ErrorDesc Code=''&gt;&lt;/ErrorDesc&gt;&lt;/Error&gt;&lt;/RateInformation&gt;&lt;/HotelRateInformation&gt;&lt;/HotelRateResponse&gt;</string>
"""

result = html.unescape(str_template)

print(result)

