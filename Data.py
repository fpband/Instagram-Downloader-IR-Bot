from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
<b>👋 سلام {} خوش آمدی.</b>\n
<b>🎌 من ربات کاربردی دانلودر اینستاگرام هستم.</b>

🎭 میتوانید با استفاده از این ربات
عکس پروفایل و دانلود پست های اینستاگرام را به راحتی دانلود کنید.😎

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
🔺 **دانلود عکس و ویدیو های اینستاگرام**
• برای دریافت پست های اینستاگرام فقط کافیه لینک اشتراک گذاری پست مورد نظر را به ربات ارسال نمایید.

🔺 ** دانلود عکس پروفایل **
• برای دریافت عکس پروفایل کاربر ، ابتدا /dp را تایپ کرده سپس نام کاربری اینستاگرامی موردنظر خود تایپ و ارسال کنید. مثال 👇<b>\n→ /dp user_id  ←</b>\n✓ بجای کلمه user_id نام کاربری مورد نظرتون را ارسال کنید.\n\n<b>❌ فعلا امکان دانلود استوری و ویدیوی ig فراهم نیست.\n\n✅ @IR_InstagramDlBot </b>

"""

    # About Message
    ABOUT = """
**💼درباره ی من** 

 **🤖 <b>نام ربات :** [اینستاگرام دانلودر](https://t.me/ir_instagramdlbot)</b>\n
 **🔧 <b>سازنده ربات :** [FﾑRSHIの-BﾑŊの](https://telegram.me/farshidband)</b>\n
 **📢 <b>کانال پشتیبانی :** [Series+](https://telegram.me/SeriesPlus1)</b>\n
 
    """
