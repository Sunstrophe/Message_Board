import psycopg2 as pc2
import os
from dotenv import load_dotenv

load_dotenv()

class DataBase:

    def __init__(self):
        db = self.connect()

    def connect(self):

        return pc2.connect(
            host="localhost",
            dbname=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD)