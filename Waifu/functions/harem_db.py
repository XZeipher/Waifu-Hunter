"""
MIT License

Copyright (c) 2023 XZeipher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
