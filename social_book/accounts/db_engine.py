from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/mydb"

engine=create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("SQLAlchemy Engine connected successfully")
    connection.close()
except Exception as e:
    print(f"Error connecting to database:{e}")

