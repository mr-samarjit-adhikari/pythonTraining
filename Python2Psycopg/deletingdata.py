
import psycopg2

from configdatabase import get_dbconfig
from connectdatabase import connect_db

def delete_vendor(vendor_id):
    """ delete data from the vendors table
        @:return : updated row
    """
    conn = None
    rows_deleted = 0
    sql = """ DELETE FROM vendors WHERE vendor_id=%s """
    try:
        params = get_dbconfig()
        conn = connect_db(**params)

        cur = conn.cursor()
        cur.execute(sql,(vendor_id,))
        rows_deleted = cur.rowcount

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    delete_vendor(5)