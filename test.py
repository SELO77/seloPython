from datetime import datetime, timedelta

check_in = datetime.strptime("2016-08-28", "%Y-%m-%d")
check_out = datetime.strptime("2016-08-31", "%Y-%m-%d")

print(check_in)
minus = check_out - check_in
minus = minus.days
print(minus)
print(type(minus))

