from datetime import datetime

import numpy as np
from db import SQLiteConnector
from parser import ReportParser
from queries import CREATE_TABLE, GET_REPORT, INSERT_DATA
from utils import get_random_date


class ReportHandler:
    def __init__(self, db_name: str, table_name: str, xlsx_path: str):
        self.db_name = db_name
        self.table_name = table_name
        self.xlsx_path = xlsx_path

    def create_db_table(self) -> None:
        with SQLiteConnector(self.db_name) as db:
            db.execute(CREATE_TABLE.format(self.table_name))

    @staticmethod
    def split_to_chunks(array: np.ndarray, n: int) -> list[np.ndarray]:
        return [array[index : index + n] for index in range(0, len(array), n)]

    def add_random_date(self, data: np.ndarray) -> np.ndarray:
        now: datetime = datetime.now()
        for item in data:
            item[0] = get_random_date(month=now.month, year=now.year)
        return data

    def insert_batch_data(self, batch: list[np.ndarray]) -> None:
        with SQLiteConnector(self.db_name) as db:
            db.executemany(INSERT_DATA.format(self.table_name), batch, commit=True)

    def insert_all_data(self, batch_size: int = 100) -> None:
        report_parser: ReportParser = ReportParser(self.xlsx_path)
        values: np.ndarray = report_parser.parse(skiprows=2)
        for batch in self.split_to_chunks(values, batch_size):
            added_random_date: np.ndarray = self.add_random_date(batch)
            self.insert_batch_data(added_random_date)

    def get_report(self) -> list[tuple]:
        with SQLiteConnector(self.db_name) as db:
            self.rows: list[tuple] = db.execute(GET_REPORT.format(self.table_name))
        return self.rows

    def output_report(self) -> None:
        for row in self.rows:
            print(f"Date: {row[0]}  Qliq: {row[1]}  Qoil: {row[2]}")
