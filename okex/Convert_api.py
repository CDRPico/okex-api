from .client import Client
from .consts import *


class ConvertAPI(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        super().__init__(api_key, api_secret_key, passphrase, use_server_time, flag)
    
    def currencies(self):
        return self._request_without_params(GET, CONVERT_CURRENCIES)

    def currency_pair(self, fromCcy, toCcy):
        params = {
            'fromCcy': fromCcy, 
            'toCcy': toCcy, 
        }
        return self._request_with_params(GET, CONVERT_CURRENCY_PAIR, params)

    def quote(self, baseCcy, quoteCcy, side, rfqSz, rfqSzCcy, clQReqId=None, tag=None):
        params = {
            'baseCcy': baseCcy, 
            'quoteCcy': quoteCcy, 
            'side': side, 
            'rfqSz': rfqSz, 
            'rfqSzCcy': rfqSzCcy, 
            'clQReqId': clQReqId, 
            'tag': tag, 
        }
        return self._request_with_params(POST, CONVERT_ESTIMATE_QUOTE, params)

    def trade(self, quoteId, baseCcy, quoteCcy, side, sz, szCcy, clTReqId=None, tag=None):
        params = {
            'quoteId': quoteId,
            'baseCcy': baseCcy,
            'quoteCcy': quoteCcy,
            'side': side,
            'sz': sz,
            'szCcy': szCcy,
            'clTReqId': clTReqId,
            'tag': tag
        }
        return self._request_with_params(POST, CONVERT_TRADE, params)
    
    def history(self, after=None, before=None, limit=None, tag=None):
        params = {
            'after': after,
            'before': before,
            'limit': limit,
            'tag': tag
        }
        return self._request_with_params(GET, CONVERT_HISTORY, params)