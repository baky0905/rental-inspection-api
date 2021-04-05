import pandas as pd
from sqlalchemy import create_engine

from sql_queries import sql_queries
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_LOCAL")
engine = create_engine(SQLALCHEMY_DATABASE_URI)


def load_csv_to_database(table, list_of_columns):
    """Load csvs from data-init folder to the existing database tables

    Args:
        table (str): name of the csv file
        list_of_columns (list): list of columns that will be uploaded from
        a csv to table in database.
    """
    df = pd.read_csv(f"db_init/data/{table}.csv")
    try:
        df.filter(list_of_columns).to_sql(
            table,
            schema=None,
            con=engine,
            if_exists='append',
            index=True,
            index_label='id',
            method=None)
    except Exception as e:
        print(e)


def drop_all_tables():
    """
    https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/
    """
    with engine.connect() as con:
        con.execute(sql_queries.drop_all_tables)


def create_all_tables():
    with engine.connect() as con:
        con.execute(sql_queries.create_all_tables)


if __name__ == "__main__":

    drop_all_tables()

    create_all_tables()

    load_csv_to_database(
        'category',
        ['name',
         'created_at',
         'updated_at',
         ])

    load_csv_to_database(
        'vehicle',
        ['make',
         'num_of_doors',
         'horsepower',
         'image_url',
         'created_at',
         'updated_at',
         'category'])

    load_csv_to_database(
        'driver',
        ['name',
         'phone_number',
         'email',
         'username',
         'password',
         'created_at',
         'updated_at',
         ])

    load_csv_to_database(
        'question',
        ['question',
         'frequency_check',
         'created_at',
         'updated_at',
         ])

    load_csv_to_database(
        'category_question',
        ['category',
         'question'])

    load_csv_to_database(
        'signature',
        ['signature',
         'created_at',
         'updated_at',
         ])

    load_csv_to_database(
        'check_log',
        ['comment'
         'created_at',
         'updated_at',
         'driver',
         'vehicle',
         'signature'])

    load_csv_to_database(
        'answer',
        ['short_answer',
         'comment',
         'photo_url',
         'created_at',
         'updated_at',
         'question',
         'check_log'
         ])
