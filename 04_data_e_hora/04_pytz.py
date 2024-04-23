#pip install pytz

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)