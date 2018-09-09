import json
from Common import Constants
import psycopg2
from Database.Connection.connection import Connection


class PostgresConnection(Connection):

    def __init__(self):
        self.connection = None

    @classmethod
    def init_from_file(cls, file_name, env_name, config_name):
        file_handle = open(file_name, 'r')
        file_content = file_handle.read()
        connection_string = json.loads(file_content)
        super(PostgresConnection, cls).__init__(cls,
                                                connection_string[env_name][config_name][Constants.DATABASE_NAME],
                                                connection_string[env_name][config_name][Constants.HOST_NAME],
                                                connection_string[env_name][config_name][Constants.USER_NAME],
                                                connection_string[env_name][config_name][Constants.PASSWORD],
                                                connection_string[env_name][config_name][Constants.PORT])
        print(cls)
        file_handle.close()

    def __str__(self):
        return "host='{}' dbname='{}' user='{}' password='{}' port={}".format(self.host, self.db_name, self.user_name,
                                                                                self.password, self.port)

    def open_connection(self):
        self.connection = psycopg2.connect(self.__str__())

    def close_connection(self):
        self.connection.close()
