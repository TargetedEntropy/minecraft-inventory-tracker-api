import os
import sys
import databases
import sqlalchemy


from os import environ, path
from dotenv import load_dotenv

# Load configuration values from the .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Check if we are testing. If so
# we use a fake sqlite db we delete
# if it exists
if "pytest" in sys.modules:
    DB_FILE = "test.db"
    try:
        os.remove(DB_FILE)
    except OSError:
        pass
    DATABASE_URL = "sqlite:///./test.db"
    database = databases.Database(DATABASE_URL, force_rollback=True)
else:
    DATABASE_URL = environ.get("SQLALCHEMY_DATABASE_URI")
    database = databases.Database(DATABASE_URL)

# Create the database engine
engine = sqlalchemy.create_engine(DATABASE_URL)

# Generate the table schema
metadata = sqlalchemy.MetaData()
