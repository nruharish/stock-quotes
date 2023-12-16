import requests
from config import Config


class NSE:
    def __init__(self, dt):
        self.dt = dt
        self.NSE_URL = Config().get_config("downloader")["NSE_URL"]
        self.nse_url = ''

    def url(self):
        # https://archives.nseindia.com/content/historical/EQUITIES/2020/MAY/cm17MAY2022bhav.csv.zip
        month = self.dt.strftime('%b').upper()
        self.nse_url = self.NSE_URL.format(month, month)
        self.nse_url = self.dt.strftime(self.nse_url)

    def download(self):
        with requests.Session() as session:
            session.headers.update({'User-Agent': 'Mozilla/5.0'})
            response = session.get(self.nse_url)
            response.raise_for_status()
            return response
        return None
