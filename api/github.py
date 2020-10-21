"""from testcase.repos import Repos

class Github():
    def __init__(self,**kwargs):
        self.api_root_url="http://api.github.com"
        self.repos=Repos(self.api_root_url,**kwargs)

if __name__=='__main__':
    r=Github(token="xxxxxxxxxxxxxx")
    x=r.repos.list_your_repos()
    print()"""
from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.checks.checks import Checks
from api.git_data.gitdata import GitData


class Github():
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.checks = Checks(self.api_root_url, **kwargs)
        self.gitdata = GitData(self.api_root_url, **kwargs)
