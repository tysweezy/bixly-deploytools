from fabric import Connection as FabConnection


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

 
class DeployDjango(BixlyConnection):
    
    def __init__(self, *args, **kwargs):
        """
        Grab properties from parent class. Start 
        connection to Django server to run deployment commands
        """
        super(DeployDjango, self).__init__(*args, **kwargs)
        self.connection = self.connect()

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