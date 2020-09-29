"""
Utility library for working with the edx-organizations app
"""


from django.conf import settings
from django.db.utils import DatabaseError
from organizations import api as organizations_api
from organizations.exceptions import InvalidOrganizationException


# We re-export these functions from the Organizations API without modification.
add_organization_course = organizations_api.add_organization
add_organization_course = organizations_api.add_organization_course
get_organization = organizations_api.get_organization
get_organization_courses = organizations_api.get_organization_courses
get_course_organizations = organizations_api.get_course_organizations


def get_organization_by_short_name(organization_short_name):
    """
    Client API operation adapter/wrapper
    """
    try:
        return organizations_api.get_organization_by_short_name(organization_short_name)
    except InvalidOrganizationException:
        return None


def get_organizations():
    """
    Client API operation adapter/wrapper
    """
    # Due to the way unit tests run for edx-platform, models are not yet available at the time
    # of Django admin form instantiation.  This unfortunately results in an invocation of the following
    # workflow, because the test configuration is (correctly) configured to exercise the application
    # The good news is that this case does not manifest in the Real World, because migrations have
    # been run ahead of application instantiation and the flag set only when that is truly the case.
    try:
        return organizations_api.get_organizations()
    except DatabaseError:
        return []


def get_course_organization_id(course_id):
    """
    Returns organization id for course or None if the course is not linked to an org
    """
    course_organization = get_course_organizations(course_id)
    if course_organization:
        return course_organization[0]['id']
    return None


def organization_strictness_enabled(course_id):
    """
    Returns whether
    """
    return bool(settings.get('STRICT_ORGANIZATIONS'))
