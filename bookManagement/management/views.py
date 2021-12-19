from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Image
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import re

# Create your views here.
'''
    主页视图
'''
def index(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/index.html', context)

# 用户模型
# -------------------------------------------------------------------------------------------------
'''
    对用户状态进行判断，如果已经登录就跳转首页，反之注册
    # 添加了对method请求方法的处理形式：
        如：用户通过post方式提交表单时产生哈希形式的文件，而某些较复杂情况会产生json文件（该项目暂不考虑此情况）
'''
def sign_up(request):
    if request.user.is_authenticated: # 判断是否登录
        return HttpResponseRedirect(reverse('homepage'))
    # context = {
    #     'active_menu': 'homepage',
    #     'user': None
    # }
    # return render(request, 'management/sign_up.html', context)
    state = None # 用于描述注册的状态
    if request.method == 'POST': #判断post
        # 联立sign_up.html中的require
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')

        ret = re.match("(?!^\\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$)(?!^[_/,\;#]).{8,12}", password)

        if password == '' or repeat_password == '':
            state = 'empty'
        elif len(password) > 12:
            state = 'out_of_range'
        elif not ret:
            state = 'grammar_error'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,\
                                                    email=request.POST.get('email', ''))
                new_user.save()
                state = 'success'
    context = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/sign_up.html', context)

'''
    登陆界面：
        实施了对state的标注等
'''
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            target_url = request.POST.get('next', reverse('homepage')) # 获取next
            return HttpResponseRedirect(target_url)
        else:
            state = 'not_exist_or_password_error'
    context = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/login.html', context)

'''
注销：
    对于注销就不需要创建单独的页面，设置一个块直接返回指定页面即可
'''
def logout(request):
    # respons = HttpResponseRedirect(reverse('homepage'))
    # respons.delete_cookie('name')
    # del request.session['username']
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


'''
修改密码：
    与之前不同的是，添加了@login_required # 告诉程序，使用这个方法是要求用户登录的
    这是一个很多开发者关心的问题：
        服务页面是需要登录后才能访问的，给所有的视图函数都加上is_authenticated进行判断无疑是较高冗余的
        @login_required完美解决了这个问题
'''
@login_required
def change_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')

        ret = re.match("(?!^\\d+$)(?!^[a-zA-Z]+$)(?!^[_#@]+$)(?!^[_/,\;#]).{8,12}", new_password)

        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif len(new_password) > 12:
                state = 'out_of_range'
            elif not ret:
                state = 'grammar_error'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/change_password.html', content)
# -------------------------------------------------------------------------------------------------


# 图书模型
# -------------------------------------------------------------------------------------------------
'''
添加图书：
    类似于上述的修改密码视图，添加了一个判断权限的修饰器
'''
@user_passes_test(lambda u: u.is_staff)
def add_book(request):
    user = request.user
    state = None
    if request.method == 'POST':
        new_book = Book(
            name = request.POST.get('name', ''),
            author = request.POST.get('author', ''),
            category = request.POST.get('category', ''),
            price = request.POST.get('price', ''),
            publish_date = request.POST.get('publish_date', ''),
        )
        new_book.save()
        state = 'success'
    context = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
    }
    return render(request, 'management/add_book.html', context)

'''
图片上传:
    明细：
        要为具体的一本书上传图片，所以需要将图书列表也一起传递到前端
'''
@user_passes_test(lambda u: u.is_staff)
def add_img(request):
    user = request.user
    state = None
    if request.method == 'POST':
        try:
            new_img = Image(
                name=request.POST.get('name', ''),
                description=request.POST.get('description', ''),
                img=request.FILES.get('img', ''), # 上传的文件被保存在FILES中
                book=Book.objects.get(pk=request.POST.get('book', ''))
            )
            new_img.save()
        except Book.DoesNotExist as e:
            state = 'error'
            print(e)
        else:
            state = 'success'
    context = {
        'user': user,
        'state': state,
        'book_list': Book.objects.all(),
        'active_menu': 'add_img',
    }
    return render(request, 'management/add_img.html', context)


'''
图书列表：
    分页
'''
@login_required
def book_list(request, category='all'):
    user = request.user
    category_list = Book.objects.values_list('category', flat=True).distinct() # 去重
    if Book.objects.filter(category=category).count() == 0:
        category = 'all'
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category=category)

    paginator = Paginator(books, 5) # 每页5个对象
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'user': user,
        'active_menu': 'view_book',
        'category_list': category_list,
        'query_category': category,
        'book_list': books
    }
    return render(request, 'management/book_list.html', context)

# 详情
@login_required
def book_detail(request, book_id=1):
    user = request.user
    try:
        book = Book.objects.get(pk=book_id) # 根据id返回书籍信息
    except Book.DoesNotExist:
        return HttpResponseRedirect(reverse('book_list', args=('all', )))
    context ={
        'user': user,
        'active_menu': 'view_book',
        'book': book,
    }
    return render(request, 'management/book_detail.html', context)


#--------------------------------------------------------------------------------------------------
# 杂项
#--------------------------------------------------------------------------------------------------
def log(request):
    user = request.user
    context = {
        'active_menu': 'log',
        'user': user,
    }
    return render(request, 'management/log.html', context)