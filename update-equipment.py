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
    new_status = event['status']

    try:
        with conn.cursor() as cursor:
            # Update equipment status in the Equipment table
            update_query = "UPDATE Equipment SET status = %s WHERE equipId = %s"
            cursor.execute(update_query, (new_status, equipId))
            conn.commit()
            logger.info(f"Equipment status updated successfully: Equipment ID {equipId}")

    except pymysql.MySQLError as e:
        logger.error("ERROR: Unable to update equipment status")
        logger.error(e)
        return {
            'statusCode': 500,
            'body': 'Error updating equipment status'
        }
            
    return {
        'statusCode': 200,
        'body': 'Equipment status updated successfully'
    }
