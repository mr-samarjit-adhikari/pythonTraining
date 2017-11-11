
import psycopg2

from configdatabase import get_dbconfig
from connectdatabase import connect_db

def get_vendors():
    """ query data from the vendors table """
    conn = None
    sql = """ SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name """
    try:
        params = get_dbconfig()
        conn = connect_db(**params)

        cur = conn.cursor()
        cur.execute(sql)

        print ("The number of vendors: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_vendors()