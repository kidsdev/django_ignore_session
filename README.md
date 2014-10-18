ignore django session some url

install

replace MIDDLEWARE_CLASSES in settings.py
MIDDLEWARE_CLASSES = (
    'PATH.django_ignore_session.middleware.MySessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'PATH.django_ignore_session.middleware.MyAuthenticationMiddleware',
    'PATH.django_ignore_session.middleware.MySessionAuthenticationMiddleware',
    'PATH.django_ignore_session.middleware.MyMessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

edit SESSION_IGNORE in django_ignore_session.middleware