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

sql_script = """
-- Create the Equipment table
CREATE TABLE Equipment (
    equipId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    status VARCHAR(50),
    location VARCHAR(100)
);

-- Create the Location table
CREATE TABLE Location (
    locationId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255)
);

-- Create the Status table
CREATE TABLE Status (
    statusID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

-- Add any additional tables or constraints as needed
"""

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
