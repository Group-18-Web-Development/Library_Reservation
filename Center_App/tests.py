from django.test import TestCase
from django.urls import reverse
from Center_App import views
from django.http import HttpRequest
from django.template.loader import render_to_string


# 测试url解析的Html调用
class HtmlTestCase(TestCase):
    # 测试根url是否解析到主页
    def test_homepage_url(self):
        found = reverse('/')  # 返回根目录127.0.0.1:8000的页面
        self.assertEqual(found.func, views.homepage)  # 和homepage函数比较两个页面，homepage.html

    # 测试调用homepage函数返回的页与模板加载的homepage.html是否相等
    def test_homepage_html(self):
        request = HttpRequest()
        response = views.homepage(request)  # HttpRequest调用的页面
        expected_html = render_to_string('main/homepage.html')  # 模板函数返回的页面
        self.assertEqual(response.content.decode(), expected_html)


if __name__ == '__main__':
    TestCase.main()
