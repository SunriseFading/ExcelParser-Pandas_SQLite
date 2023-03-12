import sqlite3


class SQLiteConnector:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(database=self.db_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute(self, query: str, parameters: tuple = ()) -> list[tuple]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            results = cursor.fetchall()
        return results

    def executemany(
        self, query: str, parameters: list[tuple], commit: bool = False
    ) -> None:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.executemany(query, parameters)
            if commit:
                self.connection.commit()
