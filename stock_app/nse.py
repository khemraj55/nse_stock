import requests

class NseIndia:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def get_stock_info(self, symbol):
        url1 = 'https://www.nseindia.com/api/quote-equity?symbol=' + symbol.replace(' ', '%20').replace('&', '%26') + "&section=trade_info"
        url2 = 'https://www.nseindia.com/api/quote-equity?symbol=' + symbol.replace(' ', '%20').replace('&', '%26')
        response1 = self.session.get(url1, headers=self.headers).json()
        response2 = self.session.get(url2, headers=self.headers).json()
        
        try:
            tc = response1['marketDeptOrderBook']['tradeInfo']['totalMarketCap']
            fc = response1['marketDeptOrderBook']['tradeInfo']['ffmc']
            lp = response2['priceInfo']['lastPrice']
            ma = response2["industryInfo"]["macro"]
            se = response2["industryInfo"]["sector"]
            ind = response2["industryInfo"]["industry"]
            bas = response2["industryInfo"]["basicIndustry"]
            return tc, fc, lp, ma, se, ind, bas
        except KeyError:
            return None, None, None, None, None, None, None
