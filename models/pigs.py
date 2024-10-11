from .base import Base

class Pig(Base, table=True):
    __tablename__ = "pigs"

    house: str
    name: str
    