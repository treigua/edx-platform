from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'xblock_django.management')

from common.djangoapps.xblock_django.management import *
