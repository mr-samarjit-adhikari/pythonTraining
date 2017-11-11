import psycopg2

from configdatabase import get_dbconfig
from connectdatabase import connect_db
from insertingdata import insert_vendor


def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id
        @return: updated row count
    """
    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s """
    conn = None
    updated_rows = 0
    try:
        params = get_dbconfig()
        conn = connect_db(**params)

        cur = conn.cursor()
        cur.execute(sql, (vendor_name, vendor_id))

        updated_rows = cur.rowcount

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

if __name__ == '__main__':
    # insert one vendor
    vendor_id = insert_vendor("L&T new Co.")
    # update the vendor
    update_vendor(vendor_id,"L&T old Co. ")
