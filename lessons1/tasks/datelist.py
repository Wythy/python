import datetime

start_year = 1900
x = datetime.datetime.now()
present_year = x.year

# print(type(present_year))

while start_year <= present_year:
    # start_year = start_year + 1
    print(start_year)
    start_year += 1
