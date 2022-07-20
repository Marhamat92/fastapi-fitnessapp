####################################################
####################################################
from psycopg2cffi import compat

compat.register()
####################################################
####################################################
# region Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# endregion

# region Engine

engine = create_engine("postgresql://postgres:dD5Yz6xE5m@localhost:5435/fitnessapp", pool_size=2000, max_overflow=0)  # postgresql.conf max_connection=1101
conn = engine.connect()
SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)
Base = declarative_base()
# endregion