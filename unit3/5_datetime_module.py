import datetime

now = datetime.datetime.now()
print(now)
print(datetime.date.today())
print(now.time())

print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%A, %B %d, %Y"))

dt = datetime.datetime(2024, 12, 25, 10, 30)
print(dt)

today = datetime.date.today()
print(today + datetime.timedelta(days=1))
print(today + datetime.timedelta(weeks=1))

diff = datetime.datetime(2024, 12, 31) - datetime.datetime(2024, 1, 1)
print(diff.days)

parsed = datetime.datetime.strptime("2024-12-25", "%Y-%m-%d")
print(parsed)