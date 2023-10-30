from Waifu import *

async def characters(user_id, page, characters_per_page):
    offset = (page - 1) * characters_per_page
    cusr.execute("SELECT * FROM user_data WHERE user_id = %s LIMIT %s OFFSET %s", (str(user_id), characters_per_page, offset))
    result = cusr.fetchall()
    return result

async def is_player(user_id):
    cusr.execute("SELECT * FROM user_data WHERE user_id = %s", (str(user_id),))
    result = cusr.fetchall()
    return result
    
async def char_list(user_id):
    cusr.execute("SELECT * FROM user_data WHERE user_id = %s",(str(user_id),))
    data = cusr.fetchall()
    pics = [item[3] for item in data]
    return pics
