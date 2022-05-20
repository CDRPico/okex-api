from .client import Client
from .consts import *


class BrokerAPI(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        super().__init__(api_key, api_secret_key, passphrase, use_server_time, flag)
    
    def info(self):
        return self._request_without_params(GET, BROKER_INFO)

    def create_subaccount(self, subAcct, acctLv, label):
        params = {
            'subAcct': subAcct, 
            'acctLv': acctLv,
            'label': label, 
        }
        return self._request_with_params(POST, BROKER_CREATE, params)

    def delete_subaccount(self, subAcct):
        params = {
            'subAcct': subAcct, 
        }
        return self._request_with_params(POST, BROKER_DELETE, params)

    def list_subaccount(self, subAcct=None, page=None, limit=None):
        params = {
            'subAcct': subAcct, 
            'page': page, 
            'limit': limit, 
        }
        return self._request_with_params(GET, BROKER_LIST, params)
    
    def level_subaccount(self, subAcct, acctLv):
        params = {
            'subAcct': subAcct, 
            'acctLv': acctLv, 
        }
        return self._request_with_params(POST, BROKER_LEVEL, params)

    def create_crypto_address(self, subAcct, ccy, chain=None, addrType=None, to=None):
        params = {
            'subAcct': subAcct, 
            'ccy': ccy, 
            'chain': chain,
            'addrType': addrType,
            'to': to,
        }
        return self._request_with_params(POST, BROKER_ADDRESS, params)

    def get_crypto_address(self, subAcct, ccy):
        params = {
            'subAcct': subAcct, 
            'ccy': ccy, 
        }
        return self._request_with_params(GET, BROKER_ADDRESS, params)

    def deposit_history_subaccount(self, subAcct=None, ccy=None, txId=None, state=None,\
         after=None, before=None, limit=None):
        params = {
            'subAcct': subAcct, 
            'ccy': ccy, 
            'txId': txId, 
            'state': state, 
            'after': after, 
            'before': before, 
            'limit': limit, 
        }
        return self._request_with_params(GET, BROKER_HISTORY, params)

    def rebate_history_subaccount(self, subAcct=None, begin=None, end=None, page=None, limit=None):
        params = {
            'subAcct': subAcct, 
            'begin': begin,
            'end': end,
            'page': page,
            'limit': limit, 
        }
        return self._request_with_params(GET, BROKER_REBATE, params)

    def create_keys(self, subAcct=None, label='', passphrase=None, ip=None, perm='read_only'):
        params = {
            'subAcct': subAcct, 
            'label': label,
            'passphrase': passphrase,
            'ip': ip,
            'perm': perm
        }
        return self._request_with_params(POST, BROKER_CREATE_KEYS, params)