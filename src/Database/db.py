

class Db:

    def __init__(self, connection):
        self.connection = connection.connection
        self.query = ''
