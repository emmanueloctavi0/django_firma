##
# Logs
##
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[FIEL] %(levelname)s %(name)s %(asctime)s %(module)s %(lineno)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[FIEL] %(levelname)s %(name)s %(asctime)s %(module)s %(lineno)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'firma.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
