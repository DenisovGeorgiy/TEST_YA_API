import unittest
import Ya_Disk


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(Ya_Disk.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(Ya_Disk.create_folder('test_passed'), 409)

    def tearDown(self):
        Ya_Disk.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()