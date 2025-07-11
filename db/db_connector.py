import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('configs/config.ini')

def get_user_from_db(user_id):
    conn = mysql.connector.connect(
        host=config['DB']['host'],
        user=config['DB']['user'],
        password=config['DB']['password'],
        database=config['DB']['database']
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
