from core.rest_client import RestCline

class Forks(RestCline):

    def List_forks(self,owner,repo,**kwargs):
        """
        https://developer.github.com/v3/repos/forks#list-forks
        """
        return self.get('/repos/{}/{}/forks'.format(owner,repo),**kwargs)
