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
async def update(user_id,pic):
    cusr.execute("SELECT count FROM user_data WHERE user_id = %s AND pic = %s",(str(user_id),pic,))
    result = cusr.fetchone()
    if not result:
        return False
    new = int(result[0]) + 1
    cusr.execute("UPDATE user_data SET count = %s WHERE user_id = %s AND pic = %s",(str(new) , str(user_id),pic,))
    DB.commit()
    return True
