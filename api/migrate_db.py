from sqlalchemy import create_engine

from api.models.task import Base

# root: データベースのユーザー名 (docker-compose -> services -> db -> environment -> MYSQL_ROOT_PASSWORD)
# @db: データベースサーバーのホスト名またはIPアドレス (docker-compose -> services -> db -> container_name)
# 3306: データベースサーバーがリッスンしているポート番号 (docker-compose -> services -> db -> ports)
# todo: 接続するデータベースの名前 (docker-compose -> services -> db -> environment -> MYSQL_DATABASE)
# ?charset=utf8: 接続オプションを指定
DB_URL = "mysql+pymysql://root:root@db:3306/todo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    # テーブルを削除
    Base.metadata.drop_all(bind=engine)
    # テーブルを度作成
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()