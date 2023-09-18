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
    
    data = event['equipment']
    
    with conn.cursor() as cursor:
        try: 
            cursor.execute(equip_table_sql_script)
            add_equip_query = "INSERT INTO Equipment (name, description, status, location) VALUES (%s, %s, %s, %s)"
            cursor.execute(add_equip_query, (
                data['name'],
                data['description'],
                data['statusId'],
                data['locationId']
            ))
            conn.commit()
            logger.info(f"New Equipment: {data['name']} added successfully")
        except pymysql.MySQLError as e:
            logger.error("ERROR: Unable to add new equipment")
            logger.error(e)
            return {
                'statusCode': 500,
                'body': 'Error adding new equipment'
            }
            
    return {
        'statusCode': 200,
        'body': 'New equipment added successfully'
    }
