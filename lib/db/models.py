from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///beangrade.db")

Base = declarative_base()
