# 图书管理系统

## 成果

### 主页1

![image-20211212204852237](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204852237.png)

### 主页2

![image-20211212204319704](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204319704.png)

### 添加图书

![image-20211212204655221](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204655221.png)

### 添加图片

![image-20211212204730357](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204730357.png)

### 图书列表

![image-20211212204756965](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204756965.png)

### 详情

![image-20211212204820741](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212204820741.png)



# -----------------------------------------------------------------------------------

## 项目结构导览

接下来带你看懂项目的文件都是干什么的，黑体是非常重要的

+ bookManagement 项目文件夹
  - analysis 放软工设计文件的
  - bookManagement   django项目核心
    - _ _init__.py
    - asgi.py  与ASGI兼容的web服务器，好像是3.0以后才有的
    - **settings.py 项目设置信息，如：添加应用程序的路径，改变数据库等等**
    - **urls.py 完成网站的路由设置，即url的统一**
    - wsgi 与WSGI兼容的web服务器

  - local 放本地图片或其他文件的
  - management 应用程序核心
    - migrations 数据库变更的记录
    - static 放静态文件的
    - _ _init__.py 
    - admin.py 后台管理
    - apps.py 与应用有关
    - **models.py 应用模型**
    - tests.py 做测试的
    - **views.py 视图**
    - **urls.py 自定义的url**

  - media 放上传的文件的
  - **template 放实例的，比如html文件啥的，自己创的**
  - **manage.py 命令工具**


# -----------------------------------------------------------------------------------

# 单位图书管理系统
## 说明

**编译器**：python3.9.exe

**开发环境**：window10 PyCharm 2021.2

**框架**：django4.0

**其它静态文件**：放在management/static/中

下述设计流程以*《软件工程（第二版）》钱秋乐等著*为基础



## 综述
### 产品定位

内部系统或外部系统

用户数量：小，可以设计较小的缓存机制

系统使用频次：在于系统的可拓展性

### 需求分析

实现一个社团或单位的图书管理系统，就是实现一个系统对图书进行**增删改查**的操作，所以对于该系统来说使用角色就包含管理员（少数几个）和用户

对于用户而言：*主要是对图书进行查询和检索，并且为他们提供常见的登录和注册功能*

对于管理员而言：*除了需要提供一般用户的管理功能以外，还需要提供对图书的增删查改等管理功能*

总结：

+ 用户注册
+ 用户分级
+ 用户登录
+ 书籍信息的添加
+ 书籍信息的修改
+ 书籍信息的删除
+ 书籍信息的分类
+ 书籍信息的查询



### 产品设计的确定

这是一个前后端的web应用，所以在页面设计上需要进行着重考虑

用户角度：*对于非管理而言，就算不登陆也可以查看书籍的具体信息，而管理员则有专门的页面对图书进行管理并且支持登录，而对于某些特殊的需求，例如添加图书时需要提供书的图片等等要考虑好拓展性。*

书籍角度：*书籍的基本信息：书名、作者、分类、ISBN、价格等*

总结：

+ 首页
+ 书籍列表，如搜索结果或分类
+ 书籍的详情页面
+ 登录页面
+ 注册页面
+ 书籍添加页面
+ 书籍修改页面



### 设计排期

整个产品是典型的以数据为中心，并围绕用户和书籍为准的应用，所以在设计的排期上优先考虑设计用户和书籍的模型

总结：

+ 用户和书籍模型
+ 登录和注册功能
+ 实现书籍的增加、删除、修改、搜索的接口
+ 其它页面



# -----------------------------------------------------------------------------------



### 结构化分析与设计

其实这部分做的不太好，尤其是SC图画的很烂，都是跟着课本走的，而且里面很多东西都是旧版的，硬要解释的话就是用的**原型模型**，要跟着用户需求来变化（雾）

DFD是pdlegacyshell16绘制的，其余为draw.io（非常好用），github上应该找得到

#### DFD

##### TOP

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212213734766.png" alt="image-20211212213734766" style="zoom:80%;" />

##### first

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212213821714.png" alt="image-20211212213821714" style="zoom:80%;" />



##### second

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212213917170.png" alt="image-20211212213917170" style="zoom:80%;" />



#### SC

![image-20211212214006990](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212214006990.png)



#### flow

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212214104492.png" alt="image-20211212214104492" style="zoom:67%;" />

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212214140086.png" alt="image-20211212214140086" style="zoom:67%;" />

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211212214155380.png" alt="image-20211212214155380" style="zoom: 67%;" />

# -----------------------------------------------------------------------------------



## 简略的步骤

+ 创建django项目

![image-20211213143713934](C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211213143713934.png)

+ 编写模型models

+ 运行数据库shell接口

  ```
  终端执行：
  python manage.py makemigrations
  python manage.py migrate
  然后就可以开始玩数据库了，不在赘述
  ```

+ 设计management/urls

+ 把management/urls统一到bookManagement/urls中

  ```
  具体代码就不写了去找就行
  
  ```

+ 可以设计页面了（base.html）

  ````
  在此先介绍一下django的模板
  **关于django模板语言**
  
  所谓模板就是一个可以用于生成各种文件类型数据的文本文件（也就是生成各种文件的模板）
  
  不同的是，模板包含了变量{{feature}}（处理对应值）、标签（处理逻辑）、过滤器{{feature | filter}}（内置显示函数，可以简化views）
  
  标签：{% tag %} 标签内容{% endtag %}
  
  ```python
  例：
  {% for book in book_list %}
  	<li>{{book.name}}</li>
  {% endfor %}
  ```
  
  模板继承：block和extends（继承父）
  
  简而言之，模板的出现简化了冗余的操作，使用继承加强可维护性
  ----------------------------------------------------
  
  这个继承学过面向对象的应该都懂吧，所以设计页面时最应该考虑的就时做一个base.html作为通用模板，然后其它的页面继承它就行了，这样代码冗余就会减少很多
  ````

+ 把你写的这个页面添加到视图中management/views中
+ 根据自己写的《设计排期》和《产品设计》就行上述两部的循环编写就行了，就比如注册登录修改密码这几个功能，肯定是先设计注册再设计登录再设计修改密码合理嘛，按这种顺序写！这个时候就涉及DFD和SC的重要性了，你细品

## API

```django
{% csrf_token %} 
如果仔细地观察了代码，会发现几乎每一个出现表单的地方都有这个语句的存在，
其原因：
'''
在django中我们需要在templates的form中加入这串内容，它的作用是当我们get表单页面时，服务器返回页面的同时也会向前端返回一串随机字符，post提交时服务器会验证这串字符来确保用户是在服务端返回的表单页面中提交的数据，防止有人通过例如jquery脚本向某个url不断提交数据，是一种数据提交的验证机制。
'''
```

```django
HttpResponseRedirect
将客户端重定向到新的 URL
详见：https://docs.microsoft.com/zh-cn/dotnet/api/system.web.httpresponse.redirect?view=netframework-4.8

非常重要的东西，把请求变成响应了
```

```python
render
可以算的上是HttpResponseRedirect的升级版，它可以传递一个带着上下文的字典

如主页的视图：
def index(request):
    user = request.user if request.user.is_authenticated else None
    context = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/index.html', context)
比HttpResponseRedirect好的就是，不仅能够完成接下来的渲染，还能把context里的状态给触发了
一般来说context是默认的空字典，而里面的'active_menu'是自己设定的：
<script type="text/javascript">
    $('#{{ active_menu }}').addClass('active');
</script> # 来自base.html

详见：https://www.cnblogs.com/yang-wei/p/9997741.html
```

# 要分享的

## 闲话

​	项目上也说了这是入门级项目，最主要还是让大家读懂程序和搞懂设计流程。

​	先是一段白话，自己在学习的过程中感觉Django最大的优点就是它的MVT模式，**即先编写好模型和构建好视图函数，就可以直接套用模板了，不用再去关心如何控制视图等问题**。而其它的优点则是：1、它是python框架，小白用python做事真的太容易上手了。2、它的ORM模式太香了，你可以不用去担心数据库使用的不好这个问题，因为全程都在使用python语句进行操作。说完这个大家应该有个底了，只要会python就是有手就行了。

​	**MVT模型：**

<img src="C:\Users\huawei\AppData\Roaming\Typora\typora-user-images\image-20211129135915390.png" alt="image-20211129135915390" style="zoom:50%;" />

​	如果像自己写一个的，我建议先认真读一下板块《软件工程设计流程》、《产品设计的确定》、《设计排期》。想要做出这样的系统来，这三步是非常重要的，它决定了你到时候写不写得出来和写出来能不能用。

# -----------------------------------------------------------------------------------

