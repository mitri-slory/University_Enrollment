import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x19\x85\x06\x04\xc4\x0f\x94\x90\xfaQ/e\x0b\xbf\x80\x86'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }

    