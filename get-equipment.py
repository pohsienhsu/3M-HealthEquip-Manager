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
    
    equipId = event['equipId']

    try:
        with conn.cursor() as cursor:
            # Retrieve equipment information from the Equipment table
            select_query = "SELECT * FROM Equipment WHERE equipId = %s"
            cursor.execute(select_query, (equipId,))
            equipment_data = cursor.fetchone()

            if equipment_data is None:
                return {
                    'statusCode': 404,
                    'body': 'Equipment not found'
                }

    except pymysql.MySQLError as e:
        logger.error("ERROR: Unable to retrieve equipment information")
        logger.error(e)
        return {
            'statusCode': 500,
            'body': 'Error retrieving equipment information'
        }
    
    return {
        'statusCode': 200,
        'body': {
            'equipId': equipment_data[0],
            'name': equipment_data[1],
            'description': equipment_data[2],
            'statusId': equipment_data[3],
            'locationId': equipment_data[4]
        }
    }
