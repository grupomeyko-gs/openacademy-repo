# -*- codig: UTF-8  -*-

import logging

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)
class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to sessions
    '''
    # Seudo-contructor method
    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_12')
        self.course_vauxoo = self.env.ref('__export__.openacademy_course_34_8cd9681d')

    # Generic methods

    # Test methods
    def test_10_instructor_is_attendee(self):
        '''
        Check that raise of 'A session's' instructor can't be an attendee
        '''
        with self.assertRaisesRegexp(
                ValidationError,
                "A session's instructor can't be an attendee",
            ):
            self.session.create({
                'name': 'Session test 1',
                'seats': 1,
                'instructor_id': self.partner_vauxoo.id,
                'attendee_ids': [(6,0,[self.partner_vauxoo.id])],
                'course_id': self.course_vauxoo.id
                })

    def test_20_wkf_done(self):
        '''
        Check that workflow works fine
        '''

        self.session.create({
            'name': 'Session test 1',
            'seats': 1,
            'instructor_id': self.partner_vauxoo.id,
            'attendee_ids': [(6,0,[self.partner_vauxoo.id])],
            'course_id': self.course_vauxoo.id
            })







