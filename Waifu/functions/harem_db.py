from Waifu import cusr,DB,app


async def globrank():
    cusr.execute("SELECT * FROM user_data")
    data = cusr.fetchall()
    sorted_waifu_data = sorted(data, key=lambda x: int(x[-1]), reverse=True)
    formatted_list = [f"{item[1]} - {item[-1]}" for item in sorted_waifu_data]
    top_10_entries = formatted_list[:10]
    return top_10_entries

async def grpharem(chat_id):
    async for members in app.get_chat_members(chat_id):
        cusr.execute("SELECT * FROM user_data WHERE user_id = %s", (str(members.user.id),))
        result = cusr.fetchall()
    sorted_waifu_data = sorted(result, key=lambda x: int(x[-1]), reverse=True)
    formatted_list = [f"{item[1]} - {item[-1]}" for item in sorted_waifu_data]
    top_10_entries = formatted_list[:10]
    return top_10_entries
