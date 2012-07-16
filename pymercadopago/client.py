import requests

class UnauthorizedException(Exception):
    def __init__(self, message, error):
        Exception.__init__(self, message)
        self.error = error
        

class Client(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self._authenticated = False

    def authenticate(self):
        r = requests.post(
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

            self._authenticated = True

            return self.access_token
            
        elif r.status_code == 400:
            raise UnauthorizedException(r.json['message'], r.json['error'])


    def create_preference(self, preference):
        pass

    def get_preference(self, preference_id):
        pass

    def notification(self, payment_id):
        pass

        

            

    
