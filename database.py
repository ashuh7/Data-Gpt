import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = (
    "mysql+mysqlconnector://root:MYSQL_PASSWORD@MYSQL_HOST:MYSQL_PORT/MYSQL_DATABASE"
)

engine = create_engine(DATABASE_URL)


def execute_query(query):
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    return df