import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL,create_engine


load_dotenv()


database_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    database=os.getenv("MYSQL_DATABASE"),
)

engine = create_engine(database_url)


def execute_query(query):
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    return df
