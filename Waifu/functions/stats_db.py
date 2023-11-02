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

from Waifu import cursor as cusr , DATABASE as DB

cusr.execute("""
    CREATE TABLE IF NOT EXISTS chats_db (
        id SERIAL PRIMARY KEY,
        chat_id VARCHAR(255) NOT NULL
    )
""")
DB.commit()
cusr.execute("""
    CREATE TABLE IF NOT EXISTS users_db (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL
    )
""")
DB.commit()


async def add_chat(chat_id):
    cusr.execute("SELECT * FROM chats_db WHERE chat_id = %s",(str(chat_id),))
    result = cusr.fetchone()
    if not result:
        cusr.execute("INSERT INTO chats_db (chat_id) VALUES (%s)",(str(chat_id),))
        DB.commit()
        return True
    return False

async def add_user(user_id):
    cusr.execute("SELECT * FROM users_db WHERE user_id = %s",(str(user_id),))
    result = cusr.fetchone()
    if not result:
        cusr.execute("INSERT INTO users_db (user_id) VALUES (%s)",(str(user_id),))
        DB.commit()
        return True
    return False
