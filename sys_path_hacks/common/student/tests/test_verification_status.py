from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'student.tests.test_verification_status')

from common.djangoapps.student.tests.test_verification_status import *
