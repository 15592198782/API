from core.rest_client import RestCline

class Issues(RestCline):

    def create_issue(self,owner,repo,**kwargs):
        """
            https://developer.github.com/v3/issues/#create-an-issue
        """
        return self.poat("/repos/{}/{}/issues".fromat(owner,repo),**kwargs)