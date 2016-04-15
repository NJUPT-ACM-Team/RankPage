from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Table, Boolean, Text, ForeignKey, UnicodeText
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    stu_id = Column(String(15))
    name = Column(String(30))
    college = Column(String(40))
    phone = Column(String(20))
    qq = Column(String(15))
    email = Column(String(40))
    account = Column(String(20))
    passwd = Column(String(15))
    hint = Column(Text)
    tried = Column(Boolean, nullable=False, default=False)
    success = Column(Boolean, nullable=False, default=False)
    info = Column(Text)
    sendby = Column(String(40))

    def __repr__(self):
        return "<StuId:%s, Name:%s, Email:%s, Success:%s, Sendby:%s>" % \
            (self.stu_id, self.name, self.email, str(self.success), self.sendby)

class RankPage(Base):
    __tablename__ = 'rankpages'
    id = Column(Integer, primary_key=True)
    html = Column(UnicodeText(length=2**31))
    time = Column(DateTime)
