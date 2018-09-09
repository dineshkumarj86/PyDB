import unittest
import sys

sys.path.append('D:\Workouts\Python\Germaneness\Samples\Example1')

from Database import PostgresConnection, Postgres, Query


class TestRealDB(unittest.TestCase):

    def test_Whether_DB_Is_Connecting_And_Returning_Values(self):
        conn = PostgresConnection()
        conn.init_from_file('simple.json', 'dev', 'dbConfig')
        conn.open_connection()
        query = Query('public."application"').select().column('*').from_table()
        db = Postgres(conn)
        rows = db.fetch_all(query.query_built)
        print(rows)
        print(len(rows))
        self.assertTrue(len(rows) > 0)
        conn.close_connection()


if __name__ == '__main__':
    unittest.main()
