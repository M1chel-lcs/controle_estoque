from mysql.connector import connect
from config import DB_CONFIG

def conectar():
    return connect(**DB_CONFIG)
