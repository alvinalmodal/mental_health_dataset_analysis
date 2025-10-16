import pandas as pd

from .dataset_access import get_dataset, get_duckdb_connection

con = get_duckdb_connection()

dataset = get_dataset()


def get_history_treatment_correlation() -> pd.DataFrame:
    query = f"""
        SELECT
            family_history,
            (SUM(CASE WHEN treatment = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*) AS "Sought Treatment",
            (SUM(CASE WHEN treatment = 'No' THEN 1 ELSE 0 END) * 100.0) / COUNT(*) AS "Did Not Seek Treatment"
        FROM '{dataset}' 
        GROUP BY family_history
    """
    return con.execute(query).fetchdf()


def get_coping_social_correlation() -> pd.DataFrame:
    query = f"""
        SELECT Coping_Struggles, Social_Weakness , COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Coping_Struggles) as percentage
        FROM '{dataset}'
        GROUP BY Coping_Struggles, Social_Weakness
    """
    return con.execute(query).fetchdf().pivot(index='Coping_Struggles', columns='Social_Weakness', values='percentage')
