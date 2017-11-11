import psycopg2

from configdatabase import get_dbconfig
from connectdatabase import connect_db


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        params = get_dbconfig()
        conn = connect_db(**params)

        cur = conn.cursor()  #New transaction
        cur.execute(sql, (vendor_name,))
        #Get the vendor ID
        vendor_id = int(cur.fetchone()[0])

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id


def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        params = get_dbconfig()
        conn = connect_db(**params)

        cur = conn.cursor()
        cur.executemany(sql,vendor_list)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one vendor
    insert_vendor("L&T Co.")
    # insert multiple vendors
    insert_vendor_list([
        ('IXIA india Pvt Ltd.',),
        ('HPE india Pvt Ltd',),
        ('CGI India Pvt Ltd',),
    ])