#!/usr/bin/env python3

import requests
import sys

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print('Invalid params')
        sys.exit(0)

    photo_url = sys.argv[1]
    files={'photo':open(photo_url, 'rb')}

    token = "<TELEGRAM_BOT_TOKEN>"
    receiver = "<YOUR_TELEGRAM_ID>"

    resp = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={receiver}",files=files)