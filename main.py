
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.error import TelegramError
import time

# 🔐 Дані доступу
TOKEN = '7345843370:AAH9dlms5hyzCzEYM-j731BlkdCUlak6cdI'
CHANNEL_ID = '-1002503854960'  # ID твого каналу

bot = Bot(token=TOKEN)

def parse_silpo():
    url = 'https://silpo.ua/offers'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.select('div.catalog-item')[:3]  # перші 3 товари

    for item in items:
        try:
            title = item.select_one('.catalog-item__title').get_text(strip=True)
            price = item.select_one('.catalog-item__price-new').get_text(strip=True)
            image_url = item.select_one('img')['src']

            message = f"🛒 {title}\n💸 Ціна: {price}\n🔗 [Сільпо](https://silpo.ua/offers)"

            bot.send_photo(
                chat_id=CHANNEL_ID,
                photo=image_url,
                caption=message,
                parse_mode='Markdown'
            )
            print(f"[✅] Надіслано: {title}")
            time.sleep(2)  # затримка між повідомленнями
        except TelegramError as e:
            print(f"[❌] Помилка Telegram: {e}")
        except Exception as e:
            print(f"[❗] Інша помилка: {e}")

if __name__ == '__main__':
    parse_silpo()
