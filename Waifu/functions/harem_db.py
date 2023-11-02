from Waifu import cusr,DB,app


async def globrank():
    cusr.execute("SELECT * FROM user_data")
    data = cusr.fetchall()
    count = {}
    alt = []
    for item in data:
        user_id = item[1]
        if user_id in count:
            count[user_id] += 1
        else:
            count[user_id] = 1
    sorted_users = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]
    return sorted_users

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
