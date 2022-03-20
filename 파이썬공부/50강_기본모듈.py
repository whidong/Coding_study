import sys
#명령 매개변수
print(sys.argv)
"""
import datetime

datetime.datetime.now()
"""
from datetime import datetime
now = datetime(2000,1,1,1,1,1)#특정시간을 입력
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import time

print("A")
time.sleep(2)
print("B")

from urllib import request

target = request.urlopen("http://hanbit.co.kr")
content = target.read()

print(content[:100])




