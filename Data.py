from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 سلام {} خوش آمدی.😍❤️

⁦<b>✴️⁩ من ربات کاربردی اینستاگرام دانلودر هستم.😎</b>

🎭 میتوانید با استفاده از این ربات
عکس پروفایل و دانلود پست های اینستاگرام را
به راحتی دانلود کنید.🥰

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="↩ بازگشت به منوی اصلی", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 سازنده ربات", url="https://t.me/FarshidBand")],
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
**📍 درباره ی من** 

 **🤖 <b>نام ربات :** [اینستاگرام دانلودر](https://t.me/ir_instagrambot)</b>\n
 **👲 <b>سازنده ربات :** [FﾑRSHIの-BﾑŊの](https://telegram.me/farshidband)</b>\n
 **📢 <b>کانال پشتیبانی :** [Series+](https://telegram.me/SeriesPlus1)</b>\n
 
    """
