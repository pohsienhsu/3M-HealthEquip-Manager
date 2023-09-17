import pymysql
import os
import logging
import sys

# import dotenv
# dotenv.load_dotenv()

# RDS MySQL Configurations
db_host = os.environ["RDS_DB_HOST"]
db_username = os.environ["RDS_DB_USERNAME"]
db_password = os.environ["RDS_DB_PASSWORD"]
db_name = os.environ["RDS_DB_NAME"]

# Loggers
logger = logging.getLogger()
logger.setLevel(logging.INFO)

equip_table_sql_script = """
CREATE TABLE IF NOT EXISTS Equipment (
    equipId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    status VARCHAR(50),
    location VARCHAR(100)
);
"""

location_table_sql_script = """
CREATE TABLE IF NOT EXISTS Location (
    locationId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255)
);
"""

status_table_sql_script = """
CREATE TABLE IF NOT EXISTS Status (
    statusID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);
"""


# Connect to the RDS MySQL instance
try:
    conn = pymysql.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        db=db_name
    )
    
    # Commit the changes
    conn.commit()
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to RDS MySQL instance")
    logger.error(e)
    sys.exit()
    
logger.info("SUCCESS: Connection to RDS MySQL instance established successfully")

def lambda_handler(event, context):
    
    with conn.cursor() as cursor:
        cursor.execute(equip_table_sql_script)
        conn.commit()
        logger.info("Table Equipment has been created successfully")
        
    with conn.cursor() as cursor:
        cursor.execute(location_table_sql_script)
        conn.commit()
        logger.info("Table Location has been created successfully")
        
    with conn.cursor() as cursor:
        cursor.execute(status_table_sql_script)
        conn.commit()
        logger.info("Table Status has been created successfully")
    
    print(event)
    print(context)
    
    return "Function Execution successful"
