# -*- codig: UTF-8  -*-
import logging

from psycopg2.errors import CheckViolation, UniqueViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


_logger = logging.getLogger(__name__)
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
        self.course_id = self.create_course('course test', 'description course test', None)

    # Method of class that don't is test
    def create_course(self, course_name, course_description, course_responsible_id):
        # create a course with parameters received
        course_id = self.course.create({
            'name' : course_name,
            'description' : course_description,
            'responsible_id': course_responsible_id
        })
        return course_id

    # Method of test, startswidth 'def test_*(self):'

    # Mute the error odoo.sql_db to avoid it in log
    @mute_logger('odoo.sql_db')
    def test_10_same_name_description(self):
        '''
        Test create a course with same name and description.
        To raise constraint of name diferent from description
        '''
        # Error raised expected with message
        with self.assertRaisesRegexp(
                CheckViolation,
                'new row for relation "openacademy_course" violates check'
                ' constraint "openacademy_course_name_description_check"'
                ):
            # create the course with the same name and descrip to raise error
            self.create_course('test', 'test', None)

    @mute_logger('odoo.sql_db')
    def test_20_two_course_same_name(self):
        '''
        Test to create two courses with the same name.
        To raise constrain of unique name.
        '''
        new_id = self.create_course('test1', 'test_description', None)
        _logger.info('New ID: {}'.format(new_id))

        with self.assertRaisesRegexp(
                UniqueViolation,
                'duplicate key value violates unique constraint '
                '"openacademy_course_name_unique"'
                ):
            new_id2 = self.create_course('test1', 'test_description', None)
            _logger.info('New ID 2: {}'.format(new_id2))

    def test_30_duplicate_course(self):
        '''
        Test to duplicate a course and test and check that works fine.
        '''
        course = self.course_id
        copy_course_id = course.copy()
        _logger.info('Copy Course ID: {}'.format(copy_course_id))
