import unittest
import sys

sys.path.append('D:\Workouts\Python\Germaneness\Samples\Example1')
from Database import Connection
from Database import PostgresConnection


class TestConnectionMethods(unittest.TestCase):

    def test_connections_and_insert_check_if_connection_has_proper_values(self):
        c = PostgresConnection()
        PostgresConnection.init_from_file('simple.json', 'dev', 'dbConfig')
        self.assertEqual(c.db_name, 'PythonDB')


if __name__ == '__main__':
    unittest.main()
