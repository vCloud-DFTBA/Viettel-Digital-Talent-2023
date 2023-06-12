from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os


url = URL.create(
    drivername="postgresql",
    username=os.getenv( "POSTGRES_USERNAME", "postgres"),
    password=os.getenv( "POSTGRES_PASSWORD","postgres"),
    host=os.getenv( "POSTGRES_HOST","localhost"),
    database=os.getenv( "POSTGRES_DB","postgres"),
    port=5432
)

ENGINE_DATABASE = create_engine(url)
