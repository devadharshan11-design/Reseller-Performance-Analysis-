import pandas as pd
from sqlalchemy import create_engine
import os

# --- Configuration (Same as before) ---
PROJECT_PATH = r'D:\SQL PROJECT'
CSV_DIRECTORY = os.path.join(PROJECT_PATH, 'olist_data')
DB_USER = 'root'
DB_PASSWORD = 'Dev_10032005' # <-- Make sure this is your correct password
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'projectmain'

# Create the database connection string
db_connection_str = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

def load_reviews_table(engine):
    """Loads the order_reviews.csv into a new table in MySQL."""
    table_name = 'order_reviews'
    file_path = os.path.join(CSV_DIRECTORY, 'olist_order_reviews_dataset.csv')
    
    try:
        df = pd.read_csv(file_path)
        print(f"--- Loading '{table_name}' table... ---")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"✅ Success! Table '{table_name}' has been loaded into the database.")
    except Exception as e:
        print(f"🚨 An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    engine = create_engine(db_connection_str)
    load_reviews_table(engine)