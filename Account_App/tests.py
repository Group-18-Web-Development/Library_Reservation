from django.test import TestCase
from Account_App.models import UserProf
from django.contrib.auth.models import User
from django.test import Client


# UsrProf类测试
class AccountTestCase(TestCase):

    def setUp(self):
        test_user = User.objects.create(username='Test_User')
        UserProf.objects.create(user=test_user, icon='static/image/zhangzhe.jpg', credit=5, delete_times=0,
                                introduction='无', name='Test_User', student_number='000001', phone_number='000001')

    def test_account_models(self):
        result = UserProf.objects.get(name="Test_User")
        user = result.user
        self.assertEqual(user.username, 'Test_User')
        self.assertEqual(result.icon, 'static/image/zhangzhe.jpg')
        self.assertEqual(result.credit, 5)
        self.assertEqual(result.delete_times, 0)
        self.assertEqual(result.introduction, '无')
        self.assertEqual(result.name, 'Test_User')
        self.assertEqual(result.introduction, '无', )
        self.assertEqual(result.student_number, '000001')
        self.assertEqual(result.phone_number, '000001')


# 测试登录动作
class LoginTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='Test_User', email='user@email.com', password='123456')

    def test_login_error(self):
        # 错误密码测试
        c = Client()
        response = c.post('/account/login/', {'username': '123', 'password': '123'})
        self.assertEqual(response.status_code, 200)  # HTTP返回码
        self.assertIn(b"Sorry. Your username or password is not right.",
                      response.content)  # 返回整个页面文本，返回的是byte类型，所以文本转成byte

    def test_login_true(self):
        # 正确密码测试
        c = Client()
        response = c.post('/account/login/', {'username': 'Public', 'password': 'qaz131313'})
        self.assertEqual(response.status_code, 302)  # HTTP返回码
        self.assertIn(b"Sorry. Your username or password is not right.",
                      response.content)  # 返回整个页面文本，返回的是byte类型，所以文本转成byte


if __name__ == '__main__':
    TestCase.main()
