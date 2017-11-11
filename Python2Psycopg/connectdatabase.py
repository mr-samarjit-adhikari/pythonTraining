from configdatabase import get_dbconfig
import psycopg2


def connect_db(**kwargs):
    try:
        dbconn = psycopg2.connect(database=kwargs['database'],user=kwargs['user'],
                                  password=kwargs['password'],host=kwargs['host'])
    except Exception as e:
        raise e

    return dbconn


if __name__ == '__main__':
    try:
        dbparams = get_dbconfig()
        connect_db(**dbparams)
        print ("Successfully connected to database.")
    except Exception as e:
        print ("Unable to connect database. Error(%s)"%(str(e)))