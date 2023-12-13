class NSE:
    def __init__(self, dt):
        self.dt = dt
        self.NSE_URL = "https://archives.nseindia.com/content/historical/EQUITIES/%Y/{0}/cm%d{1}%Ybhav.csv.zip"
        self.nse_url = ''

    def url(self):
        # https://archives.nseindia.com/content/historical/EQUITIES/2020/MAY/cm17MAY2022bhav.csv.zip
        month = self.dt.strftime('%b').upper()
        self.nse_url = self.NSE_URL.format(month, month)
        self.nse_url = self.dt.strftime(self.nse_url)
        print(self.nse_url)
    
