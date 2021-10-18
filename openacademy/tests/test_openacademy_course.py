# -*- codig: UTF-8  -*-

from psycopg2.errors import CheckViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger

class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global test to openacademy course model.
    Test create course and trigger constraints.
    '''
    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.variable = 'hello world'
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(self, course_name, course_description, course_responsible_id):
        course_id = self.course.create({
            'name' : course_name,
            'description' : course_description,
            'responsible_id': course_responsible_id
        })
        return course_id

    # Method of test, startswidth 'def test_*(self):'
    @mute_logger('odoo.sql_db')
    def test_01_same_name_description(self):
        '''
        Test create a course with same name and description.
        To test constraint of name diferent from description
        '''
        with self.assertRaisesRegexp(
                CheckViolation,
                'new row for relation "openacademy_course" violates check constraint "openacademy_course_name_description_check"'
                ):
            self.create_course('test','test',None)
