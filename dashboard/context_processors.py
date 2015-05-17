from django.conf import settings # import the settings file

def dashboard_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MESSAGING_SERVER_URL': settings.MESSAGING_SERVER_URL}