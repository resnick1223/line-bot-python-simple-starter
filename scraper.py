# 引用pyquery
from pyquery import PyQuery


def get_exchange_rate():
    """
    呼叫此方法透過PyQuery取得台幣匯率
    """
    # 透過PyQuery擷取網頁原始碼
    html = PyQuery('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    # 把貨幣名稱取得並整理成list格式
    currency_names = html('div.hidden-phone').text().split()
    # HTML過濾指標
    bid_filter = 'td.rate-content-cash[data-table="本行現金買入"]'
    offer_filer = 'td.rate-content-cash[data-table="本行現金賣出"]'
    # 取得貨幣買價並整理成list格式
    currency_bids = html(bid_filter).text().split()
    # 取得貨幣賣價並整理成list格式
    currency_offers = html(offer_filer).text().split()
    # 把取得的資料整理成dict
    currency = {}
    # 建立價格的索引
    price_idx = 0
    for idx, name in enumerate(currency_names):
        # 如果索引位置是偶數才使用
        if idx % 2 == 0:
            # 將每個貨幣名稱作為Key並以一個字典作為value儲存買價與賣價
            # EX: "美金": { "bids": "30.00", "offers": "30.50" }
            currency[name] = {
                "bids": currency_bids[price_idx],
                "offers": currency_offers[price_idx]
            }
            # 把價格的索引+1供下一個貨幣使用
            price_idx += 1
    # 回傳整理後的匯率字典
    return currency
