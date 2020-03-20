import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xv50rq#cthk#-h9&-$v-wm935kc7**e&w5tdnxars2vx491_gu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

WSGI_APPLICATION = 'wsgi.application'

ROOT_URLCONF = 'urls'