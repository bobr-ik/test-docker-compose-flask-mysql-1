from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "db"
    DB_PORT: int = 3306
    DB_USER: str = "bobr2"
    DB_PASS: str = "qwerty123"
    DB_NAME: str = "my_database"

    @property
    def DATABASE_URL_mysql(self):
        # mysql+pymysql://user:password@host:port/dbname
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()