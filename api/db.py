from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQLのdockerコンテナに対して接続するセッションを作成
# user : docker-compose -> services -> db -> environment -> MYSQL_USER
# password : docker-compose -> services -> db -> environment -> MYSQL_PASSWORD
# db : docker-compose -> services -> db -> container_name
# todo : docker-compose -> services -> db -> environment -> MYSQL_DATABASE
# ?charset=utf8: 接続オプションを指定
ASYNC_DB_URL = "mysql+aiomysql://user:password@db:3306/todo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

# DBへのアクセス
async def get_db():
    async with async_session() as session:
        yield session