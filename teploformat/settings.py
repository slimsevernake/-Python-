# -*- coding: utf-8 -*-
"""
Django settings for teploformat project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import unicode_literals
import os

from oscar.defaults import *
from oscar import get_core_apps
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0v35y0yuajh))*w**m^f2uj8^xrc52ek=-(l70im7c_o70@hr7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    'debug_toolbar',

    'users',
    'config',
    'website',
    'contacts',

    'compressor',
    'widget_tweaks',
    'modeltranslation',
    'solo',
    'ckeditor',
    'rosetta',
    'parler',
    'embed_video',
    'shop.dashboard.portation',
    'shop.dashboard.site',
] + get_core_apps(['shop.catalogue',
                   'shop.promotions',
                   'shop.dashboard.catalogue',
                   'shop.catalogue.reviews',
                   'shop.dashboard.orders',
                   'shop.dashboard.reviews',
                   'shop.search',
                   'shop.order',
                   'shop.basket',
                   'shop.partner',
                   ])

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'teploformat.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 OSCAR_MAIN_TEMPLATE_DIR
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
                'contacts.processor.show_phone_numbers',
                'contacts.processor.social_networks_ref',
                'contacts.processor.show_work_schedule',
                'config.processor.show_site_email',
                'config.processor.menu_processor',
                'config.processor.show_undercat_block',
            ],
        },
    },
]

WSGI_APPLICATION = 'teploformat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teploformat',
        'USER': 'teploformat',
        'PASSWORD': 'teploformat',
        'HOST': '/run/mysqld/mysqld.sock',
        'ATOMIC_REQUESTS': True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

PARLER_LANGUAGES = {
    None: (
        {'code': 'ru',},
        {'code': 'uk',},
    ),
    'default': {
        'fallback': 'uk',
        'hide_untranslated': False,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}

OSCAR_PRODUCTS_PER_PAGE = 12
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_SEARCH_FACETS = {
    'fields': OrderedDict([
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
    ]),
    'queries': OrderedDict([
    ]),
}

OSCAR_MISSING_IMAGE_URL = os.path.join(MEDIA_URL, 'image_not_found.jpg')

OSCAR_DEFAULT_CURRENCY = 'UAH'

# append group after Dashboard
OSCAR_DASHBOARD_NAVIGATION.insert(1,
                                  {
         'label': _('Contacts'),
         'icon': 'icon-th-list',
         'children': [
             {
                 'label': _('General'),
                 'url_name': 'dashboard:sitecontact-edit',
             },
             {
                 'label': _('Meta Tags'),
                 'url_name': 'dashboard:metatag-list',
             },
             {
                 'label': _('Timetables'),
                 'url_name': 'dashboard:timetable-list',
             },
             {
                 'label': _('Social Net Ref'),
                 'url_name': 'dashboard:socialref-list',
             },
             {
                 'label': _('Flat Pages'),
                 'url_name': 'dashboard:flatpage-list',
             },
             {
                 'label': _('Cities'),
                 'url_name': 'dashboard:city-list',
             },
         ],
     })

# append to Catalogue
OSCAR_DASHBOARD_NAVIGATION[2]['children'] += [
    {
        'label': _('Filter Description'),
        'url_name': 'dashboard:filterdescription-list',
    },
]

# append to Orders
OSCAR_DASHBOARD_NAVIGATION[3]['children'] += [
    {
        'label': _('One-Click Orders'),
        'url_name': 'dashboard:oneclickorder-list',
    },
]

# append to Clients
OSCAR_DASHBOARD_NAVIGATION[4]['children'] += [
    {
        'label': _('Call Requests'),
        'url_name': 'dashboard:callrequest-list',
    },
    {
        'label': _('Contact Messages'),
        'url_name': 'dashboard:contactmessage-list',
    },
    {
        'label': _('Вопросы о товаре'),
        'url_name': 'dashboard:productquestion-list',
    },
    {
        'label': _('Reviews'),
        'url_name': 'dashboard:reviews-list',
    },
    {
        'label': _('Ответы на отзывы'),
        'url_name': 'dashboard:reviewanswers-list',
    },
]

# remove Reviews from Content
del OSCAR_DASHBOARD_NAVIGATION[6]['children'][4]

# append as separate group
OSCAR_DASHBOARD_NAVIGATION += [{
        'label': _('Import/export'),
        'icon': 'icon-refresh',
        'children': [
            {
                'label': _('Import'),
                'url_name': 'dashboard:portation-import',
            },
            {
                'label': _('Export'),
                'url_name': 'dashboard:portation-export',
            },
        ],
    },
]

OSCAR_DASHBOARD_NAVIGATION += [{
    'label': _('Настройки лэндинга'),
    'icon': 'icon-th-list',
    'children': [
        {
            'label': _('Текст 1'),
            'url_name': 'dashboard:textone-list'
        },
        {
            'label': _('Текст 2'),
            'url_name': 'dashboard:texttwo-list'
        },
        {
            'label': _('Текст 3'),
            'url_name': 'dashboard:textthree-list'
        },
        {
            'label': _('Текст 4'),
            'url_name': 'dashboard:textfour-list'
        },
        {
            'label': _('Лэндинг'),
            'url_name': 'dashboard:landingconfig-edit'
        },
        {
            'label': _('Цены на топливо'),
            'url_name': 'dashboard:fuelconfiguration-list'
        },
        {
            'label': _('Преимущества'),
            'url_name': 'dashboard:benefit-list'
        },
        {
            'label': _('Обзоры'),
            'url_name': 'dashboard:overview-list'
        },
        {
            'label': _('Отзывы'),
            'url_name': 'dashboard:review-list'
        },
        {
            'label': _('Блок Доставка и оплата'),
            'url_name': 'dashboard:deliverypay-list'
        }
    ]
}]

THUMBNAIL_PRESERVE_FORMAT = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)
from oscar import OSCAR_MAIN_TEMPLATE_DIR
TEMPLATE_DIRS = (
    location('templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

try:
    from local_settings import *
except ImportError:
    pass
