from database.RestClient import RestClient
class Repos(RestClient):
    def __init__(self,api_root_url,**kwargs):
        super(Repos,self).__init__(api_root_url,**kwargs)
    def list_your_repos(self,**kwargs):      #  visibility=None,affiliation=None,type=None,sort=None,direction=None
        # params={"visibility":visibility,"affiliation":affiliation,"type":type,"direction":direction}

        return self.get("/user/repos",**kwargs)     #params=params
    def list_user_repos(self,username,**kwargs):
        """
        :param username: username
        """
        return self.get("/users/{}/repos".format(username),**kwargs)
    def create_user_repo(self,**kwargs):
        return self.post("/user/repos",**kwargs)
    def create_organization_repo(self,org,**kwargs):
        return self.post("/orgs/{}/repos".format(org),**kwargs)
    def get_repo(self,owner,repo,**kwargs):
        return self.get("/repos/{}/{}".format(owner.repo),**kwargs)
    def edit_repo(self,owner,repo,**kwargs):
        return self.patch("/repos/{}/{}".format(owner,repo),**kwargs)