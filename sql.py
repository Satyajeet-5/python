import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = "mysql+aiomysql://root:@localhost:3306/test"

engine = create_async_engine(DATABASE_URL, echo=False)

async def check_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed:", e)
    finally:
        await engine.dispose()  # This line prevents the warning

if __name__ == "__main__":
    asyncio.run(check_connection())
