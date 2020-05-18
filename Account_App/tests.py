from django.test import TestCase
from Account_App.models import UserProf
from django.contrib.auth.models import User


# UsrProf类测试
class AccountTestCase(TestCase):

    def setUp(self):
        test_user = User.objects.create(username='Test_User')
        test_user.save()
        test_UserProf=UserProf.objects.create(user=test_user, icon='static/image/zhangzhe.jpg', credit=5, delete_times=0, \
                                introduction='无', name='Test_User', student_number='000001', phone_number='000001')
        test_UserProf.save()

    def test_account(self):
        result = UserProf.objects.get(name="Test_User")
        user = result.user
        self.assertEqual(user.username,'Test_User')
        self.assertEqual(result.icon,'static/image/zhangzhe.jpg')
        self.assertEqual(result.credit,5)
        self.assertEqual(result.delete_times,0)
        self.assertEqual(result.introduction,'无')
        self.assertEqual(result.name,'Test_User')
        self.assertEqual(result.introduction, '无', )
        self.assertEqual(result.student_number, '000001')
        self.assertEqual(result.phone_number, '000001')


if __name__ == '__main__':
    TestCase.main()
