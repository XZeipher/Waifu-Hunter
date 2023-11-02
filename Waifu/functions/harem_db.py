from Waifu import cusr,DB,app

async def get_users(item):
    try:
        search = await app.get_users(int(item))
    except:
        return item
    return search.mention
async def globrank():
    cusr.execute("SELECT * FROM user_data")
    data = cusr.fetchall()
    sorted_waifu_data = sorted(data, key=lambda x: int(x[-1]), reverse=True)
    formatted_list = [f"{item[1]} • {item[-1]}" for item in sorted_waifu_data]
    top_10_entries = formatted_list[:10]
    return top_10_entries

async def grpharem(chat_id):
    alt = []
    async for members in app.get_chat_members(chat_id):
        cusr.execute("SELECT * FROM user_data WHERE user_id = %s", (str(members.user.id),))
        result = cusr.fetchall()
        if result:
            alt.append(result)
    picture_count = {}
    for user_data_list in alt:
        for item in user_data_list:
            user_id = item[1]
            if user_id in picture_count:
                picture_count[user_id] += 1
            else:
                picture_count[user_id] = 1
    sorted_users = sorted(picture_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return sorted_users
