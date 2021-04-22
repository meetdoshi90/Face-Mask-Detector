import os


class Config(object):
    BASIC_AUTH_USERNAME = os.environ.get('BAUTH_USER') or 'password'
    BASIC_AUTH_PASSWORD = os.environ.get('BAUTH_PASS') or 'username'
    BASIC_AUTH_FORCE = True
