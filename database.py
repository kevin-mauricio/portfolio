from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://adso:Manolosyes!!@45.77.161.32:3306/acueducto"
DATABASE_URL = "mysql+pymysql://ubussrypkd1bc5fw:OMCOJoTwwybXjGL9v1Lf@bzeofsifvsjsimbcdgfy-mysql.services.clever-cloud.com:3306/bzeofsifvsjsimbcdgfy"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
