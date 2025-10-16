import pandas as pd

from .dataset_access import get_dataset, get_duckdb_connection

con = get_duckdb_connection()

dataset = get_dataset()


def get_work_interest_correlation() -> pd.DataFrame:
    query = f"""
        SELECT Work_Interest, treatment, COUNT(*) as count 
        FROM '{dataset}'
        GROUP BY Work_Interest, treatment
    """
    return con.execute(query).fetchdf().pivot(
        index='Work_Interest', columns='treatment', values='count')


def get_interview_attitude() -> pd.DataFrame:
    query = f"""
        SELECT mental_health_interview, COUNT(*) as count 
        FROM '{dataset}' 
        GROUP BY mental_health_interview
    """
    return con.execute(query).fetchdf()


def get_care_options_distribution() -> pd.DataFrame:
    query = f"""
        SELECT care_options, COUNT(*) as count 
        FROM '{dataset}' 
        GROUP BY care_options
    """
    return con.execute(query).fetchdf()
