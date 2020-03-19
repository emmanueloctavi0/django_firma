LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('es', 'Spanish'),
    ('en', 'English'),
)

DATE_INPUT_FORMATS = [
    '%m/%d/%Y',
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
]