from config import Config


def test_config():
    config = Config()
    assert config.get_config("downloader")["NSE_URL"] == "https://archives.nseindia.com/content/historical/EQUITIES/%Y/{0}/cm%d{1}%Ybhav.csv.zip"
    assert config.get_config("main")["QUOTE_START"] == "01/01/2018"
    print(config.get_config("downloader"))
