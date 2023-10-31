from Waifu import cursor as cusr, DATABASE as DB


async def waifu_delete(id):
    try:
        cusr.execute("DELETE FROM character_db WHERE id = %s",(id,))
        DB.commit()
        return True
    except:
        return False
