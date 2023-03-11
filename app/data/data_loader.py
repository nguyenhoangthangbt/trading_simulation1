import pandas as pd

class DataLoader:
    @staticmethod
    def get_data(file_path):
        df = pd.read_csv(file_path)
        return df
