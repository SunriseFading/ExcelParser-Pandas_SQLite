from handlers import ReportHandler


def main(db_name: str, table_name: str, xlsx_path: str) -> None:
    handler = ReportHandler(db_name=db_name, table_name=table_name, xlsx_path=xlsx_path)
    handler.create_db_table()
    handler.insert_all_data()
    handler.get_report()
    handler.output_report()


if __name__ == "__main__":
    main(db_name="data.sqlite3", table_name="report", xlsx_path="data.xlsx")
