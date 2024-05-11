from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import Session, as_declarative, declared_attr, mapped_column, sessionmaker
from sqlalchemy.engine import URL
from dotenv import find_dotenv, load_dotenv
import os
import redis

# env variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
User = os.getenv("USER")
Password = os.getenv("PASSWD")
Addr = os.getenv("ADDR")



# url = "postgresql+psycopg2://" + User + ":" + Password + "@" + Addr + ":5432/delavore_db"
url = URL.create(
    drivername="postgresql",
    username=User,
    password=Password,
    host=Addr,
    database="delo",
    port=5432
)

engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# env variables
Host = os.getenv("HOSTRD")
Password = os.getenv("PASSWDRD")
Addr = os.getenv("PORTRD")

rd = redis.Redis(
  host='redis-10914.c1.asia-northeast1-1.gce.redns.redis-cloud.com',
  port=10914,
  password='zAqwgkekQvES0Xigx9rCfQVHsf4en2wW'
)
