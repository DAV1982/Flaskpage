from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Band, Base

engine = create_engine('sqlite:///band-list.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)

session = DBsession()

# CREATE
bandOne = Band(title="Imsar", members="Darkus", discography="Karani")
session.add(bandOne)
session.commit()

# READ
all_bands = session.query(Band).all()
first_band = session.query(Band).first()

# UPDATE
editedBand = session.quary(Band).filter_by(id=1).one()
editedBand.title = "Imsar"
session.add(editedBand)
session.commit()

# DELETE
bandToDelete = session.query(Band).filter_by(title='Imsar').one()
session.delete(bandToDelete)
session.commit()
