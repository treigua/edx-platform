from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('common.djangoapps', 'course_action_state.managers')

from common.djangoapps.course_action_state.managers import *
