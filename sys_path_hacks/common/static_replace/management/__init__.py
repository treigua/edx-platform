from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'static_replace.management')

from common.djangoapps.static_replace.management import *
