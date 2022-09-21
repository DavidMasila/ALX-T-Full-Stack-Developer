import unittest
from unittest.mock import patch
from employee import Employee


class test_employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    #run before the unittests
    def setUp(self):
        self.emp1 = Employee("masila", "david", 450)
        self.emp2 = Employee("antony", "masila", 670)

    #run after every unittest
    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp1.email, "masiladavid@email.com")
        self.assertEqual(self.emp2.email, "antonymasila@email.com")

        #test a change in the attributes of the Employee objects
        self.emp1.first = "jon"
        self.emp2.last = "mutheu"

        self.assertEqual(self.emp1.email, "jondavid@email.com")
        self.assertEqual(self.emp2.email, "antonymutheu@email.com")

    def test_fullname(self):

        self.assertEqual(self.emp1.fullnmae, "masila david")
        self.assertEqual(self.emp2.fullnmae, "antony masila")

        self.emp1.last = "faith"
        self.emp2.first = "veronica"

        self.assertEqual(self.emp1.fullnmae, "masila faith")
        self.assertEqual(self.emp2.fullnmae, "veronica masila")

    def test_apply_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 472.5)
        self.assertEqual(self.emp2.pay, 703.5)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok =True
            mocked_get.return_value.text = "success"

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/david/May')
            self.assertEqual(schedule, 'success')


            mocked_get.return_value.ok =False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/masila/June')
            self.assertEqual(schedule, 'Bad Request')

            


if __name__ == '__main__':
    unittest.main()