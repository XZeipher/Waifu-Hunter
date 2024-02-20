from Waifu import cusr , DB

cusr.execute("""
    CREATE TABLE IF NOT EXISTS fragments (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        celestialFragments VARCHAR(255) NOT NULL
    )
""")
DB.commit()

async def add_fragments(user_id,celestialFragments):
    cusr.execute("SELECT celestialFragments FROM fragments WHERE user_id = %s",(str(user_id),))
    result = cusr.fetchone()
    if not result:
        cusr.execute("INSERT INTO fragments (user_id, celestialFragments) VALUES (%s, %s)",(str(user_id),str(celestialFragments),))
        DB.commit()
        return True
    newAmount = int(result[0]) + celestialFragments
    cusr.execute("UPDATE fragments SET celestialFragments = %s WHERE user_id = %s",(str(newAmount) , str(user_id),))
    DB.commit()
    return True

async def rm_fragments(user_id,celestialFragments):
    pass

async def fetch_fragments(user_id):
    cusr.execute("SELECT celestialFragments FROM fragments WHERE user_id = %s",(str(user_id),))
    result = cusr.fetchone()
    if not result:
        return 0
    return int(result[0])
