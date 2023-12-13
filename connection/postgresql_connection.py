import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection parameters
dbname = "telecom"
user = "postgres"
password = "12345"
host = "localhost"
port = "5432"

# Construct the SQLAlchemy connection string
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    # Create a SQLAlchemy engine
engine = create_engine(connection_string)

    # Use Pandas to read SQL query results into a DataFrame
query = "SELECT * FROM xdr_data;"

df = pd.read_sql(query, engine)

telecomdata = df.to_csv('./data/telecom.csv')
