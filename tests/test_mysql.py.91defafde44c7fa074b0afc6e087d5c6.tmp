import MySQLdb
import unittest
import os
from models.engine.db_storage import DBStorage
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Only DBStorage")
class TestDBStorage(unittest.TestCase):
    """Tests the MySQL database for correct output"""

    @classmethod
    def setUpClass(cls):
        """sets up connection for tests to MySQL database"""
        cls.storage = DBStorage()
        cls.storage.reload()
        commands = {
            "host": os.getenv("HBNB_MYSQL_HOST"),
            "user": os.getenv("HBNB_MYSQL_USER"),
            "passwd": os.getenv("HBNB_MYSQL_PWD"),
            "db": os.getenv("HBNB_MYSQL_DB"),
        }
        cls.db = MySQLdb.connect(**commands)
        cls.cur = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Tears down set up of tests and close connections"""
        # close cursor
        cls.cur.close()
        # close database
        cls.db.close()

    def test_state_creation(self):
        """test that new state is added to database"""
        with patch("sys.stdout", new=StringIO()) as st_out:
            line = 'create State name="Lagos"'
            HBNBCommand.onecmd(line)

        self.assertIsNotNone(st_out.getvalue())

        query_res = TestDBStorage.get_number_of_states("states")
        self.assertEqual(query_res, 1)

    def test_city_creation(self):
        """test that new state is added to database"""
        with patch("sys.stdout", new=StringIO()) as state_out:
            line = 'create State name="Lagos"'
            HBNBCommand.onecmd(line)

        no_of_states = TestDBStorage.get_number_of_states("states")
        self.assertEqual(no_of_states, 1)

        cls_id = state_out.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as city_out:
            line = 'create City state_id={} name="Ayobo"'.format(cls_id)
            HBNBCommand.onecmd(line)

        city_one = TestDBStorage.get_number_of_states("cities")
        self.assertEqual(city_one, 1)

        with patch("sys.stdout", new=StringIO()) as city_out:
            line = 'create City state_id={} name="Ikeja"'.format(cls_id)
            HBNBCommand.onecmd(line)

        city_two = TestDBStorage.get_number_of_states("cities")
        self.assertEqual(city_two, city_one + 1)

    @staticmethod
    def get_number_of_states(table_name: str) -> int:
        """gets the count of records of argument from database"""
        TestDBStorage.cur.execute("SELECT COUNT(*) FROM {}".format(table_name))
        query_res = TestDBStorage.cur.fetchone()[0]
        return query_res
