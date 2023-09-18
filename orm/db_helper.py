from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

def opendb():
    engine = create_engine('sqlite:///cardb.sqlite3', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

def save(entry: object):
    try:
        db = opendb()
        db.add(entry)
        db.commit()
        db.close()
        print("Success")
    except Exception as e:
        print(f"Error: {e}")