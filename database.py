"""
MIT License

Copyright (c) 2023 XZeipher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
