
import numpy as np
import pandas as pd


class ExcelParser:
    def __init__(self, path: str) -> None:
        self.path = path

    def load(self, **kwargs) -> pd.DataFrame:
        return pd.read_excel(self.path, **kwargs)


class ReportParser(ExcelParser):
    def parse(self, skiprows: int = 0) -> np.ndarray:
        data_frame = self.load(skiprows=skiprows)
        return data_frame.values
