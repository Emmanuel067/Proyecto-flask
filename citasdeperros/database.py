from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
import os

DB_USER = os.environ.get('DB_USER', 'emmanuel')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '16650267-7')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '8686')
DB_NAME = os.environ.get('DB_NAME', 'registro')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

db_session = scoped_session(sessionmaker(bind=engine))

Database = declarative_base()


#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, scoped_session
#from sqlalchemy.orm import declarative_base

# Cambia el puerto en la URL a 8686
#engine = create_engine('postgresql://emmanuel:16650267-7@localhost:8686/registro')

# Utiliza scoped_session para manejar sesiones en contextos de subprocesos
#db_session = scoped_session(sessionmaker(bind=engine))

#Database = declarative_base()
