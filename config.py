'''Location : /config.py
Load env from ./'env/.env'
has 'get_env_setup' class, returns dict
contains 'database', 'host', 'password', 'user'
'''
import os
from dotenv import load_dotenv
from dotenv import dotenv_values
env_path = os.path.join('env', '.env')
load_dotenv(env_path)

database = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
password = os.getenv("DB_PASSWORD")
user = os.getenv('DB_OWNER')

class get_env_setup:
    @staticmethod
    def get_var():
        database = os.getenv('DB_NAME')
        host = os.getenv('DB_HOST')
        password = os.getenv("DB_PASSWORD")
        user = os.getenv('DB_OWNER')

        env_variable = {
            'database': database,
            'host': host,
            'user': user,
            'password': password
        }

        return env_variable
