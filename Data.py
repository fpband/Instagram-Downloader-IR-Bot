from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 سلام {} خوش آمدی.😍❤️

⁦<b>✴️⁩ من ربات کاربردی اینستاگرام دانلودر هستم.</b>

I can download profile pictures, videos, images and reels from instagram along with post caption.
You can also authorize me to download private posts.

Use below buttons to learn more.

Maintenance and Hosted by <b> @IRBotsUpdate</b>
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="↩ بازگشت به منوی اصلی", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 More Bots and Support Channel 🤖", url="https://t.me/IRBotsUpdate")],
        [
            InlineKeyboardButton("📲 راهنمای ربات", callback_data="help"),
            InlineKeyboardButton("📍 درباره ی من", callback_data="about")
        ],
        [InlineKeyboardButton("⭕ کانال پشتیبانی ⭕", url="https://t.me/SeriesPlus1")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp AnAccount`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 
 **🤖 <b>Bot :** [Instagram Downloader IR Bot](https://t.me/igdlirbot)</b>\n
 **👲 <b>Developer :** [LhRfi](https://telegram.me/lhrfi)</b>\n
 **👥 <b>Channel :** [IRBotsUpdate](https://telegram.me/IRBotsUpdate)</b>\n
 **❄️ <b>Credits :** Everyone in this journey</b>\n
 **🍴 <b>Source :** [Click Here](https://github.com/StarkBotsIndustries/InstagramBot) </b>\n
 **📝 <b>Language :** [Python3](https://python.org)</b>\n
 **📚 <b>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</b>\n
 **🌟 <b>Server :** [Heroku](https://heroku.com)</b>\n

    """
