import json
import logging
import pymysql
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    #rds settings
    rds_host = "weatherdata.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    name = "lambda"
    password = "lambda"
    db_name = "weatherview"

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to" + rds_host + " instance.")
        sys.exit()

    #check next DB, same credientials but different DB and host
    rds_host = "transitviewdata.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    db_name = "transitviewdata";

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to " + rds_host + " instance.")
        sys.exit()

    rds_host = "septa-01.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    db_name = "septa01";

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to " + rds_host + " instance.")
        sys.exit()

    rds_host = "septa-02.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    db_name = "septa02";

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to " + rds_host + " instance.")
        sys.exit()

    rds_host = "septa-03.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    db_name = "septa03";

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to " + rds_host + " instance.")
        sys.exit()

    rds_host = "septa-04.ccgbnu8qerao.us-east-1.rds.amazonaws.com"
    db_name = "septa04";

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to " + rds_host + " instance.")
        sys.exit()

    return {
        'statusCode': 200,
        'body': json.dumps('All databases up!')
    }
