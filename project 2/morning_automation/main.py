import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone': '7204213592', # krishna dai ko number
        'message' : '',
        'key' : 'textbelt'

    })
    print(resp.json())

# schedule.every().day.at('14:45').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)