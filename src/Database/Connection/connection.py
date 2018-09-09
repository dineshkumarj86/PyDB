class Connection:

    def __init__(self, db_name, host, user_name, password, port):
        self.db_name = db_name
        self.host = host
        self.user_name = user_name
        self.password = password
        self.port = port

    def open_connection(self):
        pass