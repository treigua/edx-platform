from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'student.message_types')

from common.djangoapps.student.message_types import *
