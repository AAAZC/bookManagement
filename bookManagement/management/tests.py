from django.test import TestCase
import re
# Create your tests here.

st = ["123456789", '2321.....aDWQ', 'wqeqweqwq','123','wqe','#$%^&*%^qweqx', 'qwert1234456....', '________']
for test in st:
    ret = re.match("(?!^\\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$)(?!^[_/,\;#]).{8,12}", test)
    if ret:
        print(test)
    else:
        print('error')