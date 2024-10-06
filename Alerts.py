import schedule
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def remind_oil_change():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время заменить масло!')

def remind_air_filter_change():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время заменить воздушный фильтр!')

def remind_oil_filter_change():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время заменить масляной фильтр!')

def remind_fuel_filter_change():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время заменить топливный фильтр!')

def remind_brake_pads_change():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время заменить тормозные колодки!')

def remind_full_to():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время пройти полное ТО!')

def remind_summer_washer_fluid():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время залить летнюю омывайку!')

def remind_winter_washer_fluid():
    updater.bot.send_message(chat_id=CHAT_ID, text='Время поменять летнюю омывайку на зимнюю!')


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('remind_oil', remind_oil_change))
    dp.add_handler(CommandHandler('remind_air_filter', remind_air_filter_change))
    dp.add_handler(CommandHandler('remind_oil_filter', remind_oil_filter_change))
    dp.add_handler(CommandHandler('remind_fuel_filter', remind_fuel_filter_change))
    dp.add_handler(CommandHandler('remind_brake_pads', remind_brake_pads_change))
    dp.add_handler(CommandHandler('remind_full_to', remind_full_to))
    dp.add_handler(CommandHandler('remind_summer_washer_fluid', remind_summer_washer_fluid))
    dp.add_handler(CommandHandler('remind_winter_washer_fluid', remind_winter_washer_fluid))


    schedule.every(8).months.do(remind_brake_pads_change)
    schedule.every(7).months.do(remind_oil_change)  # напоминать через 7 месяцев
    schedule.every(6).months.do(remind_air_filter_change)  # напоминать через 6 месяцев
    schedule.every(8).months.do(remind_oil_filter_change)  # напоминать через 8 месяцев
    schedule.every(12).months.do(remind_fuel_filter_change)  # напоминать через 12 месяцев
    schedule.every(8).months.do(remind_brake_pads_change) #напомнить через 8 месяцев
    schedule.every(48).months.do(remind_full_to) #напомнить через 48 месяцев
    schedule.every().year.at("05:00").do(remind_summer_washer_fluid)  # напоминать в мае
    schedule.every().year.at("11:00").do(remind_winter_washer_fluid)  # напомнить в ноябре

    while True:
        schedule.run_pending()
        time.sleep(1)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()