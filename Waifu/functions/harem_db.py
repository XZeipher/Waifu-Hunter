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
    combined_data = []
    for group in alt:
        combined_data.extend(group)
    sorted_data = sorted(combined_data, key=lambda x: int(x[-1]), reverse=True)
    formatted_list = [f"{await get_users(item[1])} - {item[-1]}" for item in sorted_data]
    top_10_entries = formatted_list[:10]
    return top_10_entries
