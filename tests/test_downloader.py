from downloader.nse import NSE
import datetime


def test_download_date():
    dt = datetime.datetime.now()
    nse = NSE(dt)
    assert nse.dt == dt


def test_download_url():
    dt = datetime.datetime(2022, 5, 17)
    nse = NSE(dt)
    nse.url()
    assert nse.nse_url == 'https://archives.nseindia.com/content/historical/EQUITIES/2022/MAY/cm17MAY2022bhav.csv.zip'


