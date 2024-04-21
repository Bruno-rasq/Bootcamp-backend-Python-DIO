from datetime import datetime, timezone, timedelta

data = datetime.now(timezone(timedelta(hours=2)))
data2 = datetime.now(timezone(timedelta(hours=-3)))

print(data)
print(data2)