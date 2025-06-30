
import requests
from bs4 import BeautifulSoup
import telebot
import time
import sys

# 🔐 Дані доступу
TOKEN = '7345843370:AAH9dlms5hyzCzEYM-j731BlkdCUlak6cdI'
CHANNEL_ID = '-1002503854960'  # ID твого каналу

bot = telebot.TeleBot(TOKEN, parse_mode='Markdown')

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

            message = f"🛒 *{title}*\n💸 Ціна: {price}\n🔗 [Сільпо](https://silpo.ua/offers)"
            bot.send_photo(CHANNEL_ID, photo=image_url, caption=message)
            print(f"[✅] Надіслано: {title}")
            time.sleep(2)
        except Exception as e:
            print(f"[❗] Помилка: {e}")

if __name__ == '__main__':
    print("🚀 Стартує бот...")
    parse_silpo()
    print("✅ Завершено. Вихід.")
    time.sleep(3)
    sys.exit()
