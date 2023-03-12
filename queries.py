CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        create_at TEXT,
        company VARCHAR(32) NOT NULL,
        fact_qliq_data1 INT DEFAULT 0 NOT NULL,
        fact_qliq_data2 INT DEFAULT 0 NOT NULL,
        fact_qoil_data1 INT DEFAULT 0 NOT NULL,
        fact_qoil_data2 INT DEFAULT 0 NOT NULL,
        forecast_qliq_data1 INT DEFAULT 0 NOT NULL,
        forecast_qliq_data2 DEFAULT 0 NOT NULL,
        forecast_qoil_data1 DEFAULT 0 NOT NULL,
        forecast_qoil_data2 DEFAULT 0 NOT NULL
    );"""

INSERT_DATA = """
    INSERT INTO {} (
        create_at,
        company,
        fact_qliq_data1,
        fact_qliq_data2,
        fact_qoil_data1,
        fact_qoil_data2,
        forecast_qliq_data1,
        forecast_qliq_data2,
        forecast_qoil_data1,
        forecast_qoil_data2
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

GET_REPORT = """
    SELECT
        create_at,
        sum(fact_qoil_data1) + sum(fact_qoil_data2) + sum(forecast_qoil_data1) + sum(forecast_qoil_data2) AS qoil,
        sum(fact_qliq_data1) + sum(fact_qliq_data2) + sum(forecast_qliq_data1) + sum(forecast_qliq_data2) AS qliq
    FROM
        {}
    GROUP BY
        create_at;
"""
