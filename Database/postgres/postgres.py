import psycopg2
from Database.db import Db


class Postgres(Db):

    def __init__(self, connection):
        self.cur = None
        super(connection)

    def __execute__(self, query):
        try:
            self.cur = self.connection.cursor()
            self.cur.execute(query)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def execute(self, query):
        self.__execute__(query)

    def fetch_many(self, query, size):
        self.__execute__(query)
        return self.cur.fetchmany(size)

    def fetch_all(self, query):
        print ('Query Passed {}'.format(query))
        self.__execute__(query)
        return self.cur.fetchall()

    def fetch_one(self, query):
        self.__execute__(query)
        return self.cur.fetchone()
