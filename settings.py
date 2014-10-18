MIDDLEWARE_CLASSES = (
    'PATH.django_ignore_session.middleware.MySessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'PATH.django_ignore_session.middleware.MyAuthenticationMiddleware',
    'PATH.django_ignore_session.middleware.MySessionAuthenticationMiddleware',
    'PATH.django_ignore_session.middleware.MyMessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
