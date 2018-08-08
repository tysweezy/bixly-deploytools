import logging
from fabric import Connection as FabConnection
from fabric.exceptions import GroupException
from .exceptions import RepoException

class BixlyConnection(object):
    
    def __init__(self, host, username=None, password=None, port=None, path=None):

        """
        Basic properties to form a connection to a 
        bixly server.
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.path = path
        self.connection = self.connect()

    def connect(self):
        """ 
        Get connection from a bixly server
        """

        fabconnect = FabConnection(
            self.host, 
            user=self.username, 
            port=self.port, 
            connect_kwargs={'password': self.password}
        )

        return fabconnect

    def pull_from_repo(self, branch='master'):
        """
        Pulls from remote repo. User can specify branch.

        Most cases: staging == develop and prod == master
        default branch will be master
        """
        with self.connection:
            try: 
                self.connection.run('git stash')
                self.connection.run('git fetch origin {0}'.format(branch))
                self.connection.run('git checkout {0}'.format(branch))
                self.connection.run('git pull origin {0}'.format(branch))
                logging.info("{0} branch updated on server".format(branch))
            except RepoException as repo_error:
                # TODO: should I exit program and close process? 
                # I don't want the program to continue if there are any problems with git
                logging.error('git pull proccess failed. could not deploy. {0}'.format(repo_error))

 
class DeployDjango(BixlyConnection):
    
    def __init__(self, *args, **kwargs):
        """
        Grab properties from parent class. Start 
        connection to Django server to run deployment commands
        """
        super(DeployDjango, self).__init__(*args, **kwargs)
        self.connection = self.connect()

    def virtualenv(self):
        """ 
        activate virtualenv on server

        cd [to path]
        run source {venvfolder}/bin/activate
        """
        pass

    def test_run(self):
        """
        Just a test command to make sure all is well :) 
        """
        self.connection.run('ls -al')


class AngularDeploy(BixlyConnection):
    
    def __init__(self, *args, **kwargs):
        super(AngularDeploy, self).__init__(*args, **kwargs)
        self.connection = self.connect()


class NodeDeploy(BixlyConnection):
    
    def __init__(self, *args, **kwargs):
        super(NodeDeploy, self).__init__(*args, **kwargs)
        self.connection = self.connect()    