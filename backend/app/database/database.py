from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/fintrack_db"

engine = create_engine(DATABASE_URL)

sessionLoval=sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)
Base =declarative_base()