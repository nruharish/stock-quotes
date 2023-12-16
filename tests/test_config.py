from config import Config


def test_config():
    config = Config()
    assert config.get_config("downloader")["NSE_URL"] == "https://archives.nseindia.com/content/historical/EQUITIES/%Y/{0}/cm%d{1}%Ybhav.csv.zip"
    print(config.get_config("downloader"))
