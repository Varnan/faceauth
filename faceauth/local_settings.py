

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


SOCIAL_AUTH_FACEBOOK_KEY = "780160385719192"          # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = "96309406eaf2e99df01dbab1009091be"       # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
                                      'fields': 'id, name, email, picture.type(large), link'
                                    }
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
                                    ('name', 'name'),
                                    ('email', 'email'),
                                    ('picture', 'picture'),
                                    ('link', 'profile_url'),
                                ]