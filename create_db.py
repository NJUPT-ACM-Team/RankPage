#!/usr/bin/python3
from rank.database.models import Base
from rank.database import engine

Base.metadata.create_all(engine)
