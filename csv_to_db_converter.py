import pandas as pd
import sqlite3


def csv_to_sqlite3_converter():
        
        print("CSV to DB converter:")
        print("------------------------------------------------")
        print("""Prerequisites:
                1: Install the sqlite3 and pandas python library:
                    pip install sqlite3
                    pip install pandas
                2:Make sure a table is created in the database
                    matching the CSV data structure.              
                3: Make sure both the CSV file and the DB files are 
                    in the same folder as the csv_to_db_converter.py.
        """)
        print("-------------------------------------------------")

        # Read the CSV file into a pandas DataFrame
        print("Please Enter csv file e.g. data.cvs")
        csvFile = input("> ")
        df = pd.read_csv(csvFile)

        print("Please Enter SQLite3 db file name e.g. data.db")
        dbFile = input("> ")

        # Open a connection to the SQLite3 database
        connection = sqlite3.connect(dbFile)

        print("Please Enter SQLite3 db table name")
        table = input("> ")

        # Write the DataFrame to the SQLite3 database
        df.to_sql(table, connection, if_exists='replace', index=False)

        # Close the connection
        connection.close()





csv_to_sqlite3_converter()