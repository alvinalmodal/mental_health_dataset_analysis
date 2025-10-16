import pandas as pd

from .dataset_access import get_dataset, get_duckdb_connection

con = get_duckdb_connection()

dataset = get_dataset()

def get_family_history_pct() -> float:
    query = f"""
        SELECT 
            (SUM(CASE WHEN family_history = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*) 
        FROM '{dataset}'
    """
    return con.execute(query).fetchone()[0]


def get_treatment_pct() -> float:
    query = f"""
        SELECT 
            (SUM(CASE WHEN treatment = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*) 
        FROM '{dataset}'
    """
    return con.execute(query).fetchone()[0]


def get_stress_distribution() -> pd.DataFrame:
    query = f"""
        SELECT Growing_Stress, COUNT(*) as count 
        FROM '{dataset}'
        GROUP BY Growing_Stress
    """
    return con.execute(query).fetchdf()


def get_mood_swing_distribution() -> pd.DataFrame:
    query = f"""
        SELECT Mood_Swings, COUNT(*) as count
        FROM '{dataset}'
        GROUP BY Mood_Swings
    """
    return con.execute(query).fetchdf()
