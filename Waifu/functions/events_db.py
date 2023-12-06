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

from Waifu import cursor,DATABASE,cusr,DB

cusr.execute("""
    CREATE TABLE IF NOT EXISTS winter_event (
        id SERIAL PRIMARY KEY,
        data TEXT NOT NULL
    )
""")
DB.commit()
cusr.execute("""
    CREATE TABLE IF NOT EXISTS gban_db (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        username TEXT NOT NULL,
        reason TEXT NOT NULL
    )
""")
DB.commit()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS winter_characters (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        anime TEXT NOT NULL,
        rarity TEXT NOT NULL,
        pic TEXT NOT NULL
    )
""")
DATABASE.commit()

async def gban_check(user_id):
    cusr.execute("SELECT * FROM gban_db WHERE user_id = %s",(str(user_id),))
    results = cusr.fetchone()
    if results:
        return {"user_id":int(results[1]) , "username":results[2],"reason":results[3]}
    return False

async def add_gban(user_id,username,reason):
    cusr.execute("INSERT INTO gban_db (user_id,username,reason) VALUES (%s,%s,%s)",(str(user_id),username,reason,))
    DB.commit()
    return True

async def rm_gban(user_id):
    cusr.execute("DELETE FROM gban_db WHERE user_id = %s",(str(user_id),))
    DB.commit()
    return True

    

async def winter_check():
    cusr.execute("SELECT * FROM winter_event WHERE data = %s",("True",))
    results = cusr.fetchone()
    if not results:
        return False
    return True
async def winter_on():
    cusr.execute("INSERT INTO winter_event (data) VALUES (%s)",("True",))
    DB.commit()
    return True
async def winter_off():
    cusr.execute("DELETE FROM winter_event WHERE data = %s",("True",))
    DB.commit()
    return True

