from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'third_party_auth.samlproviderdata')

from common.djangoapps.third_party_auth.samlproviderdata import *
