import glob
import os
import os.path
import oracledb
import pandas as pd
from data_login import p_username, p_password, p_dns, p_port

# Get the latest downloaded file in directory
list_of_files = glob.glob('C:\\Users\\USER\\Desktop\\belajar\\ProjectDAS\\downloaded_files\\*csv')
newest_file = max(list_of_files, key=os.path.getctime, default=None)

# Establishing Database Connection
con = oracledb.connect(user=p_username, password=p_password, dsn=p_dns, port=p_port)
print('Do we have a good connection :', con.is_healthy())
print('Are we using a Thin connection :', con.thin)
print('Database Version :', con.version)

with con.cursor() as cur:
    with open(newest_file, 'r') as csv_file:
        csv_reader = pd.read_csv(csv_file, dtype=object, delimiter=',')
        data = [tuple(x) for x in csv_reader.values]

        sql = """
        INSERT INTO BC_USER.PJJ_DAS
        (
            YEAR,
            MONTH,
            REPORTER,
            TRADE_DIRECTION,
            TRADE_PARTNER,
            HS4_CODE,
            USD,
            PRIMARY_QUANTITY,
            UNIT_PRICE,
            PRIMARY_UNITS
        ) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)
        """

        try:
            cur.execute("TRUNCATE TABLE BC_USER.PJJ_DAS")
            cur.executemany(sql, data)
            con.commit()
        except:
            con.rollback()


# # Print Data Table
# with con.cursor() as cursor:
#     for row in cursor.execute('select * from bc_user.pjj_das'):
#         print(row)

# Ending Database Connection
cur.close()
con.close()