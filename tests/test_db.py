import unittest
import sqlite3
import os

from db_actions import ActivityDatabase


class TestActivityDatabase(unittest.TestCase):

    def setUp(self):
        self.test_db_name = "test_activity.db"
        self.db = ActivityDatabase(self.test_db_name)

    def tearDown(self):
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_create_table(self):
        # We check whether the "activities" table has been created
        with sqlite3.connect(self.test_db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='activities';")
            result = cursor.fetchone()
        self.assertIsNotNone(result)

    def test_save_activity(self):
        # Check if the data is saved correctly
        activity_data = {
            "activity": "Test Activity",
            "type": "Test Type",
            "participants": 3,
            "price": 0.5,
            "accessibility": 0.2
        }
        self.db.save_activity(activity_data)

        with sqlite3.connect(self.test_db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM activities;")
            saved_activity = cursor.fetchone()

        self.assertIsNotNone(saved_activity)
        self.assertEqual(saved_activity[1], activity_data["activity"])
        self.assertEqual(saved_activity[2], activity_data["type"])
        self.assertEqual(saved_activity[3], activity_data["participants"])
        self.assertEqual(saved_activity[4], activity_data["price"])
        self.assertEqual(saved_activity[5], activity_data["accessibility"])


if __name__ == '__main__':
    unittest.main()
