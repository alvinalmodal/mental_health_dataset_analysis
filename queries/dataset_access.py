import os

import duckdb
from duckdb import DuckDBPyConnection


def get_duckdb_connection() -> DuckDBPyConnection:
    return duckdb.connect(database=':memory:')


def get_dataset():
    mental_health_dataset = os.path.abspath('./data/mental_health_dataset.csv')

    if not os.path.exists(mental_health_dataset):
        print("Error: Dataset not found.")
        print("Please make sure the dataset file location is properly set.")
        exit()
    return mental_health_dataset
