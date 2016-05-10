from datetime import date, timedelta, datetime



checkInDate = "2016-06-29"
checkOutDate = "2016-06-30"

result = datetime.strptime(checkInDate, "%Y-%m-%d")
result2 = datetime.strptime(checkOutDate, "%Y-%m-%d")
# print(result)

print(type(result2 -result))
print((result2 -result).days)



# test1 = date(2016, 6, 28)
# test2 = date(2016, 6, 30)
# print(test1)

# test2 = date(checkInDate)




