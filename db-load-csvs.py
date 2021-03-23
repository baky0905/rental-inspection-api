from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pandas as pd
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv(dotenv_path=".env")

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
engine = create_engine(SQLALCHEMY_DATABASE_URI)


def load_csv_to_database(table, list_of_columns):
    """Load csvs from data-init folder to the existing database tables

    Args:
        table (str): name of the csv file
        list_of_columns (list): list of columns that will be uploaded from
        a csv to table in database.
    """
    df = pd.read_csv(f"db-init/{table}.csv")
    try:
        df.filter(list_of_columns).to_sql(
            table,
            schema=None,
            con=engine,
            if_exists='append',
            index=False,
            # index_label='id',
            method=None)
    except Exception as e:
        print(e)


if __name__ == "__main__":

    # category
    load_csv_to_database(
        'category',
        ['name', 'created_at'])

    # vehicle
    load_csv_to_database(
        'vehicle',
        ['make',
         'num_of_doors',
         'horsepower',
         'image_url',
         'created_at',
         'category'])

    # driver
    load_csv_to_database(
        'driver',
        ['name',
         'phone_number',
         'email',
         'username',
         'password',
         'created_at'])

    # check_log_questions
    load_csv_to_database(
        'question',
        ['question',
         'frequency_check',
         'created_at',
         ])

    # check_categories_check
    load_csv_to_database(
        'category_question',
        ['category',
         'question'])

    # check_signature
    load_csv_to_database(
        'signature',
        ['signature',
         'created_at'])

    # import data to check_log
    load_csv_to_database(
        'check_log',
        ['comment'
         'created_at',
         'driver',
         'vehicle',
         'signature'])

    # answer
    load_csv_to_database(
        'answer',
        ['answer',
         'comment',
         'photo_url',
         'created_at',
         'question',
         'check_log'
         ])
