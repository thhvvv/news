import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    
    SECRET_KEY="8e93322481e9863dc38071ec14aff8bc"
    SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress the warning and avoid overhead
