from .client import Client
from .consts import *


class SubAccountAPI(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag)

    def balances(self, subAcct):
        params = {"subAcct": subAcct}
        return self._request_with_params(GET, BALANCE, params)

    def bills(self, ccy=None, type=None, subAcct=None, after=None, before=None, limit=None):
        params = {"ccy": ccy, 'type': type, 'subAcct': subAcct, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, BILLS, params)

    def delete(self, pwd, subAcct, apiKey):
        params = {'pwd': pwd, 'subAcct': subAcct, 'apiKey': apiKey}
        return self._request_with_params(POST, DELETE, params)

    def reset(self, pwd, subAcct, label, apiKey, perm, ip=None):
        params = {'pwd': pwd, 'subAcct': subAcct, 'label': label, 'apiKey': apiKey, 'perm': perm, 'ip': ip}
        return self._request_with_params(POST, RESET, params)

    def create(self, pwd, subAcct, acctLv, label, Passphrase, perm=None, ip=None):
        params = {
            'pwd': pwd, 
            'subAcct': subAcct, 
            'acctLv': acctLv,
            'label': label, 
            'Passphrase': Passphrase, 
            'perm': perm, 
            'ip': ip
        }
        return self._request_with_params(POST, CREATE, params)

    def view_list(self, enable=None, subAcct=None, after=None, before=None, limit=None):
        params = {'enable': enable, 'subAcct': subAcct, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, VIEW_LIST, params)

    def control_transfer(self, ccy, amt, froms, to, fromSubAccount, toSubAccount):
        params = {'ccy': ccy, 'amt': amt, 'from': froms, 'to': to, 'fromSubAccount': fromSubAccount,
                  'toSubAccount': toSubAccount}
        return self._request_with_params(POST, CONTROL_TRANSFER, params)
