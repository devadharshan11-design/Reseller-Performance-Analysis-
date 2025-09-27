import pandas as pd
from sqlalchemy import create_engine
import os

# --- Configuration ---
PROJECT_PATH = r'D:\SQL PROJECT'
CSV_DIRECTORY = os.path.join(PROJECT_PATH, 'olist_data')

# --- !! IMPORTANT !! ---
# --- Enter Your MySQL Connection Details Here ---
DB_USER = 'root'
DB_PASSWORD = 'Dev_10032005' # Your MySQL password
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'projectmain'

# Create the database connection string
db_connection_str = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

def load_csv_to_mysql(engine):
    """Reads key CSV files and loads them into MySQL database tables."""
    print("--- Starting fast data load into MySQL ---")
    
    files_to_load = {
        'sellers': 'olist_sellers_dataset.csv',
        'orders': 'olist_orders_dataset.csv',
        'order_items': 'olist_order_items_dataset.csv'
    }

    for table_name, file_name in files_to_load.items():
        file_path = os.path.join(CSV_DIRECTORY, file_name)
        df = pd.read_csv(file_path)
        print(f"  - Loading table '{table_name}'...")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, chunksize=10000)
        print(f"  - ✅ Table '{table_name}' loaded successfully.")
    
    print("\n✅ All data has been loaded into the database.")

# --- Main execution block ---
if __name__ == "__main__":
    try:
        # Create a database engine
        engine = create_engine(db_connection_str)
        
        # Load the data
        load_csv_to_mysql(engine)

    except Exception as e:
        print(f"🚨 An error occurred: {e}")