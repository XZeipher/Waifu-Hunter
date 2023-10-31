from Waifu import cursor as cusr, DATABASE as DB


async def waifu_delete(id):
    cusr.execute("SELECT * FROM character_db WHERE id = %s",(id,))
    result = cusr.fetchone()
    if not result:
        return False
    cusr.execute("DELETE FROM character_db WHERE id = %s",(id,))
    DB.commit()
    return True

