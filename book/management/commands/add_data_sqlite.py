import pandas as pd
from django.core.management.base import BaseCommand
from book.models import Book
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):
  help = "A command to add data from an Excel file to the database"

  def handle(self, *args, **options):

    print('--> Management Command')

    excel_file = 'books.xlsx'
    df = pd.read_excel(excel_file)
    print(df)
  

    engine = create_engine('sqlite:///db.sqlite3')

    # specify book table via_meta.db_table
    # df.to_sql(Book._meta.db_table, if_exists='replace', con=engine, index=False)
    df.to_sql(Book._meta.db_table, if_exists='append', con=engine, index=True)
