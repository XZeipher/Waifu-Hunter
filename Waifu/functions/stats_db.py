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
    return

async def add_user(user_id):
    cusr.execute("SELECT * FROM users_db WHERE user_id = %s",(str(user_id),))
    result = cusr.fetchone()
    if not result:
        cusr.execute("INSERT INTO users_db (user_id) VALUES (%s)",(str(user_id),))
        DB.commit()
        return True
    return
