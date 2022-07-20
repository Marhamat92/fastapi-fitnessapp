####################################################
####################################################
import importlib

from psycopg2cffi import compat

compat.register()
####################################################
####################################################


import warnings
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, MetaData
from sqlalchemy import exc as sa_exc
from sqlalchemy import pool

config = context.config

fileConfig(config.config_file_name)

# region SAWarnig Disable
##########################################
## SAWarnig Disable
warnings.catch_warnings()
warnings.simplefilter("ignore", category=sa_exc.SAWarning)
## SAWarnig Disable
##########################################
# endregion


# region Import Models
import sys

sys.path.append('.')
import models

# endregion


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m


target_metadata = combine_metadata(
    models.Base.metadata

)


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        context.execute("truncate table alembic_version")
        with context.begin_transaction():
            context.run_migrations()
        context.execute("truncate table alembic_version")


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

import os, glob

files = glob.glob('alembic/versions/*')
for f in files:
    try:
        os.remove(f)
    except:
        pass