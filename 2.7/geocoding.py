#-*- coding:utf-8 -*-
import math

# latitude(lat) 위도: 적도로부터 북쪽 또는 남쪽으로 얼마나 떨어져 있는지 나타내는 위치.
# longitude(lon) 경도 그리니치 천문대를 지나는 본초 자오선을 표준으로 동쪽 또는 서쪽으로 얼마나 떨어져 있는지 나타내는 위치
def calculate_distance(lat1, lng1, lat2, lng2):
    R = 6371 # km

    dLat = math.radians((lat2 - lat1))
    dLon = math.radians((lng2 - lng1))
    a = pow(math.sin(dLat/2), 2) + pow(math.cos(math.radians(lat1)), 2) * pow(math.sin(dLon/2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c



# calculation seoul and dubai distance
# distance 6791KM by https://www.distancecalculator.net/

# print calculate_distance(37.56826000, 126.97783000, 25.25817000, 55.30472000) # 6325.50053636
# print calculate_distance(37.34, 126.59, 25.16, 55.18) # 6320.50053636



class TestClass(object):

    def calculate_distance(self, lat1, lng1, lat2, lng2):
        R = 6371  # km

        dLat = math.radians((lat2 - lat1))
        dLon = math.radians((lng2 - lng1))
        a = pow(math.sin(dLat / 2), 2) + pow(math.cos(math.radians(lat1)),
                                             2) * pow(math.sin(dLon / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def make_simulator(self):
        print self.calculate_distance(37.56826000, 126.97783000, 25.25817000, 55.30472000)
        for v in range(9):
            print v


TestClass().make_simulator()