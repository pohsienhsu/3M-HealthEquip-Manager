import pymysql
import os
import logging
import sys

# RDS MySQL Configurations
db_host = os.environ["RDS_DB_HOST"]
db_username = os.environ["RDS_DB_USERNAME"]
db_password = os.environ["RDS_DB_PASSWORD"]
db_name = os.environ["RDS_DB_NAME"]

# Loggers
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Connect to the RDS MySQL instance
try:
    conn = pymysql.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        db=db_name,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    
    with conn.cursor() as cursor:
        # Execute the SQL script to create the schema
        cursor.execute(sql_script)
    
    # Commit the changes
    conn.commit()
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to RDS MySQL instance")
    logger.error(e)
    sys.exit()
    
logger.info("SUCCESS: Connection to RDS MySQL instance established successfully")

def lambda_handler(event, context):
    pass
