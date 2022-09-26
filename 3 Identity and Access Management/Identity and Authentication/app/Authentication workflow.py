from flask import Flask, request, abort
from functools import wraps
import json
from jose import jwt
from urllib.request import urlopen

#configurations
AUTH0_DOMAIN = 'dev-i15j0m76.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'image'


class AuthError(Exception):

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    #flask request meythods is able to get headers
    auth = request.headers.get('Authorization', None)

    if not auth:
        raise AuthError(
            {
                'code': 'Authorization header missing',
                'description': 'Authorization header is expected'
            }, 401)

    parts = auth.split(" ")
    if parts[0].lower() != 'bearer':
        raise AuthError(
            {
                'code': "Invalid header",
                'description': "Authorization header must start with Bearer"
            }, 401)

    elif len(parts) != 2:
        raise AuthError(
            {
                "code":
                "Invalid header",
                'description':
                "Token not found, Authorization header must be bearer token"
            }, 401)

    token = parts[1]
    return token


def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())

    #GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    #Choosing my key
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError(
            {
                'code': 'invalid header',
                'description': 'Authorization malformed'
            }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            #USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(token,
                                 rsa_key,
                                 algorithms=ALGORITHMS,
                                 audience=API_AUDIENCE,
                                 issuer='https://' + AUTH0_DOMAIN + '/')

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {
                    'code': 'Token Expired',
                    'desciption': 'Token Expired'
                }, 401)

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    'code':
                    'invalid_claims',
                    'description':
                    'Incorrect claims. Please, check the audience and issuer.'
                }, 401)
        except Exception:
            raise AuthError(
                {
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentication token.'
                }, 400)
    raise AuthError(
        {
            'code': 'invalid_header',
            'description': 'Unable to find the appropriate key.'
        }, 400)


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        abort(400)

    if permission not in payload['permissions']:
        abort(403)
    else:
        return True


#implementing permissions, getting token and verifying token.
def requires_auth(permission=''):

    def requires_auth_decor(f):

        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            try:
                payload = verify_decode_jwt(token)
            except:
                abort(401)

            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decor


app = Flask(__name__)


@app.route("/image")
@requires_auth('get:images')
def images(payload):
    print(payload)
    return "Successfull"


if __name__ == '__main__':
    app.run(debug=True)