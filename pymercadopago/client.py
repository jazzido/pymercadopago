import requests
import time

class UnauthorizedException(Exception):
    def __init__(self, message, error):
        Exception.__init__(self, message)
        self.error = error

class 

class NotAuthenticatedException(Exception):
    pass

class NotImplementedException(Exception):
    pass

URL_AUTH = 'https://api.mercadolibre.com/oauth/token'
URL_PAYMENT_INFO = 'https://api.mercadolibre.com/collections/notifications/%s'

class Client(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self._authenticatedOn = None

    def authenticate(self):
        r = requests.post(
            URL_AUTH,
            params={
                'grant_type': 'client_credentials',
                'client_id': self.client_id,
                'client_secret': self.client_secret
                },
            headers={
                'Accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded'
                })

        if r.status_code == 200:
            self.access_token  = r.json['access_token']
            self.token_type    = r.json['token_type']
            self.refresh_token = r.json['refresh_token']
            self.scope         = r.json['scope']
            self.expires_in    = r.json['expires_in']

            self._authenticatedOn = time.time()
            
            return self.access_token
            
        elif r.status_code == 400:
            raise UnauthorizedException(r.json['message'], r.json['error'])

        # unknown error
        raise Exception("Server responded with: %s: %s" % (r.status_code, r.teext,))

    def isAuthenticated(self):
        return self._authenticatedOn is not None \
            and time.time() - self._authenticatedOn < self.expires_in

    def create_preference(self, preference):
        raise NotImplementedException

    def get_preference(self, preference_id):
        raise NotImplementedException

    def update_preference(self, preference_id, data):
        if not self.isAuthenticated()
            raise NotAuthenticatedException("Not yet authenticated or authentication expired")

        raise NotImplementedException
       
                          

    def get_payment(self, payment_id):
        if not self.isAuthenticated():
            raise NotAuthenticatedException("Not yet authenticated or authentication expired")

        # https://api.mercadolibre.com/collections/notifications/transaction-id?access_token=tu-access-token
        r = requests.get(
            URL_PAYMENT_INFO % payment_id,
            params={
                'access_token': self.access_token
                },
            headers={
                'Accept': 'application/json',
                })

        if r.status_code == 200:
            return r.json
        
