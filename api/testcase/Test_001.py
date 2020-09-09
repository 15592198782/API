# import sys
# sys.path.append("E:\github\zhaochaoyi\api")
from database.RestClient import RestClient
r=RestClient("http://httpbin.org")
x=r.post("/post",json={"a":"b"})
print(x.text)

