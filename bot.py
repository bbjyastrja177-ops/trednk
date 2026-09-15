import time
import requests
from datetime import datetime

# 1. إعدادات التوكن والقناة/المستخدم
TELEGRAM_TOKEN = "8510991599:AAHgBYZj6q0uh3EFmCm4swgqWpAn4jRWPl8"
CHAT_ID = "ضع_هنا_معرف_القناة_او_الاي_دي_الخاص_بك"  # مثال للشخصي: "123456789" أو للقناة: "@my_channel"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": 8510991599,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print("خطأ في الإرسال:", e)

def run_trading_bot():
    symbol = "AUDCAD OTC"
    direction = "هبوط 🔴"
    confidence = "83%"
    now = datetime.now().strftime("%H:%M:%S")

    # كليشة التوصية
    signal_msg = f"""<b>BOT.M1👑TRADER👑</b>

<b>توقيت الدخول:</b> {now}
<b>الاتجاه:</b> {direction}
<b>مستوى الثقة:</b> {confidence}
⚠️ <b>الصفقة تحتاج إلى مضاعفة واحدة في حال الخسارة</b>"""

    # إرسال التوصية
    send_telegram_msg(signal_msg)
    print("تم إرسال التوصية إلى تيليجرام!")

    # انتظار دقيقة واحدة (مدة الصفقة)
    time.sleep(60)

    # كليشة النتيجة (يمكنك تغيير النتيجة إلى 'خسارة ❌' حسب التحليل)
    result_msg = f"""<b>#نتيجة الصفقة 📊</b>
<b>الزوج:</b> {symbol}
<b>الاتجاه:</b> {direction}
<b>وقت الدخول:</b> {now}
<b>النتيجة:</b> ربح ✅
<b>مستوى الثقة:</b> {confidence}"""

    # إرسال النتيجة
    send_telegram_msg(result_msg)
    print("تم إرسال النتيجة إلى تيليجرام!")

if __name__ == "__main__":
    run_trading_bot()
