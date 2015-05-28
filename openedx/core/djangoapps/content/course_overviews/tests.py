
from django.test import TestCase

from opaque_keys.edx.locator import CourseKey

from . import get_course_overview

class CourseOverviewTests(TestCase):

    # TODO me: write more comprehensive tests

    def test_model(self):
        course_ids = ['edX+DemoX+split-rerun']
        for course_id in course_ids:
            # note: this doesn't work for some reason
            overview = get_course_overview(CourseKey.from_string(course_id))
            print overview
