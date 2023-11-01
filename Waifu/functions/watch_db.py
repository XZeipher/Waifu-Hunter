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

from Waifu import cusr , DB
from random import choice

cusr.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        name TEXT NOT NULL,
        anime TEXT NOT NULL,
        rarity TEXT NOT NULL,
        pic TEXT NOT NULL,
        count VARCHAR(255) NOT NULL
    )
""")
DB.commit()

async def insert(user_id,name,anime,rarity,pic,count):
    cusr.execute("INSERT INTO user_data (user_id, name, anime, rarity, pic, count) VALUES (%s, %s, %s, %s, %s, %s)",(str(user_id), name, anime,rarity,pic,str(count),))
    DB.commit()
    return True
async def delete(user_id,name,anime,rarity,pic,count):
    cusr.execute("DELETE FROM user_data WHERE user_id = %s AND name = %s AND anime = %s AND rarity = %s AND pic = %s AND count = %s",(str(user_id), name,anime,rarity, pic,str(count),))
    DB.commit()
    return True
async def updaters(user_id,pic):
    cusr.execute("SELECT count FROM user_data WHERE user_id = %s AND pic = %s",(str(user_id),pic,))
    result = cusr.fetchone()
    if not result:
        return False
    new = int(result[0]) + 1
    cusr.execute("UPDATE user_data SET count = %s WHERE user_id = %s AND pic = %s",(str(new) , str(user_id),pic,))
    DB.commit()
    return True
async def decrease(user_id,pic):
    cusr.execute("SELECT count FROM user_data WHERE user_id = %s AND pic = %s",(str(user_id),pic,))
    result = cusr.fetchone()
    if not result:
        return False
    if int(result[0]) == 0:
        return False
    new = int(result[0]) - 1
    cusr.execute("UPDATE user_data SET count = %s WHERE user_id = %s AND pic = %s",(str(new) , str(user_id),pic,))
    DB.commit()
    return True
async def select(id):
    cusr.execute("SELECT * FROM user_data WHERE id = %s",(id,))
    result = cusr.fetchall()
    if result:
        return result
    return False
