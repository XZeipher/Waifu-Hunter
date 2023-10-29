import psycopg2

DB = psycopg2.connect(host='otto.db.elephantsql.com',
                    port='5432',
                    user='xvoyijqi',
                    password='46CquJaKr7qFwJv_GpBB8s7n0HCfi1HG',
                    database='xvoyijqi'
                    )

cusr = DB.cursor()
DB.rollback()
DB.autocommit = True

DATABASE = psycopg2.connect(host='otto.db.elephantsql.com',
                    port='5432',
                    user='sszitcfg',
                    password='0hUnKVnPcZmBIHj3iKA0AHRiddW4lTGt',
                    database='sszitcfg'
                    )

cursor = DATABASE.cursor()
DATABASE.rollback()
DATABASE.autocommit = True
