import pandas as pd

from .dataset_access import get_dataset, get_duckdb_connection

con = get_duckdb_connection()

dataset = get_dataset()


def get_gender_distribution() -> pd.DataFrame:
    query = f"""
    SELECT
        Gender,
        COUNT(*) as Values
    FROM '{dataset}'
    GROUP BY Gender
"""
    return con.execute(query).df()


def get_country_distribution() -> pd.DataFrame:
    query = f"""
        SELECT
            Country,
            COUNT(*) as "Number of Respondents"
        FROM '{dataset}'
        GROUP BY Country
        ORDER BY "Number of Respondents" DESC
        LIMIT 10
    """
    return con.execute(query).df()


def get_occupation_distribution() -> pd.DataFrame:
    query = f"""
        SELECT
            Occupation,
            COUNT(*) as "Number of Participants"
        FROM '{dataset}'
        GROUP BY Occupation
        ORDER BY "Number of Participants" DESC
        LIMIT 10
    """
    return con.execute(query).df()
