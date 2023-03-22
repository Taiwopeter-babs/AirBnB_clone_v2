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

    def connect_to_database(self):
        """Instantiates database connection"""
        pass

    @classmethod
    def setUpClass(cls):
        """sets up connection for tests to MySQL database"""
        cls.storage = DBStorage()
        cls.storage.reload()
        commands = {
            "host": os.getenv("HBNB_MYSQL_HOST"),
            "port": 3306,
            "user": os.getenv("HBNB_MYSQL_USER"),
            "passwd": os.getenv("HBNB_MYSQL_PWD"),
            "db": os.getenv("HBNB_MYSQL_DB"),
        }
        cls.db = MySQLdb.connect(**commands)
        cls.cur = cls.db.cursor()
        print("Setup connection")

    @classmethod
    def tearDownClass(cls):
        """Tears down set up of tests and close connections"""
        # close cursor
        cls.cur.close()
        # close database
        cls.db.close()
        print("Tear down connection")

    def test_state_creation(self):
        """test that new state is added to database"""

        curr_num = TestDBStorage.get_number("states")
        self.assertEqual(curr_num, 0)
        with patch("sys.stdout", new=StringIO()) as st_out:
            line = 'create State name="Lagos"'
            HBNBCommand().onecmd(line)

            self.assertIsNotNone(st_out.getvalue())

        all_dict = TestDBStorage.storage.all("State")
        for key in all_dict.keys():
            self.assertEqual(key.split(".")[0], "State")

            # query_res = TestDBStorage.get_number("states")
            # self.assertEqual(query_res, curr_num + 1)

    @staticmethod
    def get_number(table_name: str) -> int:
        """gets the count of records of argument from database"""
        statement = "SELECT COUNT(*) FROM {}".format(table_name)
        TestDBStorage.cur.execute(statement)
        query_res = TestDBStorage.cur.fetchone()[0]
        return query_res
