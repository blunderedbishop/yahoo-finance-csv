import datetime
from io import StringIO

import pandas as pd
import requests

class YahooCsv:
    YAHOO_DOWNLOAD_URL = 'https://query1.finance.yahoo.com/v7/finance/download/'
    
    @staticmethod
    def get_csv(symbol, date1, date2, interval="1d", events="history"):

        date1 = datetime.strptime(date1, '%Y%m%d')
        date2 = datetime.strptime(date2, '%Y%m%d')

        date1 = date1.replace(tzinfo=timezone.utc)
        date2 = date2.replace(tzinfo=timezone.utc)
    
        date1 = date1.timestamp()
        date2 = date2.timestamp()

        payload = {'period1': int(date1),
                   'period2': int(date2),
                   'interval': '1d',
                   'events': 'history',
        }

        csv_request = requests.get(YahooCsv.YAHOO_DOWNLOAD_URL+f'{symbol}', params=payload)
        csv_buffer = StringIO(csv_request.text)
        
        csv_dataframe = pd.read_csv(csv_buffer)
        return csv_dataframe
