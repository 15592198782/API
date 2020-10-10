# import sys
# sys.path.append("E:\github\zhaochaoyi\api")
from database.RestClient import RestClient
from github import Github
r=RestClient("http://httpbin.org")
x=r.post("/post",json={"a":"b"})
print(x.text)


r = Github(username="15592198782",password="zcy773883967")
x=r.repos.list_your_repos()
print(x.text)
r = Github(token="xxxxxxxxxxxxxx")
x=r.repos.list_your_repos()
print(x.text)
r = Github(token="xxxxxxxxxxxxxx")
x=r.repos.list_your_repos(visibility="private")
print(x.text)

r = Github(token="xxxxxxxxxxxxxx")
x=r.repos.list_your_repos(visibility="all")
print(x.text)

r = Github(token="xxxxxxxxxxxxxx")
x=r.repos.list_your_repos(direction="desc")
print(x.text)

r = Github(token="xxxxxxxxxxxxxx")
data={"direction":"desc"}
x=r.repos.list_your_repos(params=data)
print(x.text)

r = Github(token="xxxxxxxxxxxxxx")
data={"direction":"desc"}
x=r.repos.list_user_repos("15592198782",params=data)
print(x.text)