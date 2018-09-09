import unittest
from Database import *


class TestConnectionMethods(unittest.TestCase):

    def test_connections_and_insert_check_if_connection_has_proper_values(self):
        conn = Connection.init_from_file('simple.json', 'dev', 'dbConfig')

