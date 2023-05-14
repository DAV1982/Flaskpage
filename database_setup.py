from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Band(Base):
    __tablename__ = 'band'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    members = Column(String(250), nullable=False)
    discography = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Band {self.name!r}>'


engine = create_engine('sqlite:///band-list.db')
Base.metadata.create_all(engine)
