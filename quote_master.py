from downloader.nse import NSE
import datetime


def test_download():
    dt = datetime.datetime(2022, 5, 17)
    nse = NSE(dt)
    nse.url()
    print(nse.download())


test_download()
