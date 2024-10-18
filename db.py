import mysql.connector
from config import Config

def get_db_connection():
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE
    )
    return conn

# Function to insert a rule into the database
def insert_rule(rule_string):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string) VALUES (%s)", (rule_string,))
    conn.commit()
    cursor.close()
    conn.close()

# Function to get all rules from the database
def get_all_rules():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT rule_string FROM rules")
    rules = cursor.fetchall()
    cursor.close()
    conn.close()
    return [rule['rule_string'] for rule in rules]  # Return a list of rule strings
