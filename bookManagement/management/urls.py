'''
URL为该系统的访问入口
设计URL模型对URL地址表达式和python视图处理函数间进行映射

细明：
    主页  注册  登录  注销  修改密码    添加书籍（管理员）   添加照片（管理员）   书籍细明
'''
from django.urls import path, re_path
from management import views

urlpatterns = [
    # (字符串， 调用视图函数， url-name)
    path('', views.index, name='homepage'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_img/', views.add_img, name='add_img'),
    path('log/', views.log, name='log'),
    # /<路径转换>/
    path('book_list/<str:category>/', views.book_list, name='book_list'),
    re_path(r'^book_detail/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
]