from django.dispatch import Signal

user_logged_in = object_viewed_signal = Signal(providing_args=['instance', 'request'])
