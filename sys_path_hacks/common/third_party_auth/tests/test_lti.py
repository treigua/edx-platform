from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'third_party_auth.tests.test_lti')

from common.djangoapps.third_party_auth.tests.test_lti import *
