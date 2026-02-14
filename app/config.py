class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/transactions"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://localhost:6379/0"
