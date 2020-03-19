# debug toolbar
def show_toolbar(request):
    return os.getenv('SHOW_TOOLBAR_CALLBACK')

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}