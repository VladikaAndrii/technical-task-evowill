import sqlite3
from typing import List
from loguru import logger


ACTIVITY_DB_NAME = "activity.db"


class ActivityDatabase:
    def __init__(self, db_name=ACTIVITY_DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS activities (
                            id INTEGER PRIMARY KEY,
                            activity TEXT,
                            type TEXT,
                            participants INTEGER,
                            price REAL,
                            accessibility REAL
                        )''')
        self.conn.commit()

    def save_activity(self, activity: dict) -> None:
        sql = '''INSERT INTO activities (activity, type, participants, price, accessibility)
                 VALUES (?, ?, ?, ?, ?)'''
        values = (
            activity["activity"],
            activity["type"],
            activity["participants"],
            activity["price"],
            activity["accessibility"]
        )

        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(sql, values)
                self.conn.commit()
        except sqlite3.Error as exception:
            logger.exception(exception)

    def get_latest_activities(self, limit: int = 5) -> List[tuple]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM activities ORDER BY id DESC LIMIT ?", (limit,))
        return cursor.fetchall()
