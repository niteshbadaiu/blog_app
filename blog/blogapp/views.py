from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Blog,Student
import datetime
from django.contrib.auth.forms import AuthenticationForm
from blogapp.forms import StudentFormClass,StudentModelFormsClass,UserRegister
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def aboutPage(request):
    print("about page")
    # return HttpResponse("This is about view")
    return redirect("/contact")
def contactPage(request):
    print("contact page")
    return HttpResponse("This is contact view")

# def homePage(request,x,y):
#     print("Value of x :",x)
#     print("Value of y :",y)
#     return HttpResponse("Value of x and y:"+x+" "+y)
def helloView(request):
    context={}
    context["uname"]="nitesh"
    context["x"]=100
    context["y"]=1000
    context["l"]=[1,2,3,4,"uh"]
    return render(request,"hello.html",context)

#blog app view function start
def homePage(request):
    b=Blog.objects.filter(is_published=True)# for Blogs which are published
    context={}
    context["blog"]=b
    return render(request,'home.html',context)

def userDashboard(request):
    print("Logged in user:",request.user)
    print("Logged in user id:",request.user.id)
    print("Logged in user firstname:",request.user.first_name)
    print("Logged in user lastname:",request.user.last_name)
    # b=Blog.objects.all()
    # print(b)
    # for x in b:
    #     print(x)
    #     print(x.id)
    #     print(x.title)
    #     print(x.cat)
    #     print(x.details)
    #     print(x.created_at)
    #     print()
    b=Blog.objects.filter(uid=request.user.id)
    context={}
    context["blogs"]=b
    return render(request,'dashboard.html',context)

def createBlog(request):
    print("Method used:",request.method)
    if request.method=="GET":
        print("In GET Section")
        return render(request,'create_blog.html')
    else:
        print("In POST section")
        btitle=request.POST["title"];
        bdetails=request.POST["details"];
        bcat=request.POST["cat"];
        # print("Title:",btitle)
        # print("Details:",bdetails)
        # print("Category:",bcat)
        b=Blog.objects.create(title=btitle,details=bdetails,cat=bcat,created_at=datetime.datetime.now(),uid=request.user.id)
        b.save()
        # return HttpResponse("Data inserted successfully")
        return redirect("/userdashboard")
    
def editBlog(request,rid):
    # print("ID to be edited :"+rid)
    if request.method=="GET":
        b=Blog.objects.filter(id=rid)
        context={}
        context["blog"]=b
        return render(request,"edit_blog.html",context)
    else:
        #fetch new edited data from form
        utitle=request.POST["title"]
        udet=request.POST["details"]
        ucat=request.POST["cat"]

        # print("Edited title",utitle)
        # print("Edited details",udet)
        # print("Edited Category",ucat)
        b=Blog.objects.filter(id=rid)
        b.update(title=utitle,details=udet,cat=ucat)
        return redirect("/userdashboard")

def deleteBLog(request,rid):
    # print("ID to be deleted :"+rid)
    b=Blog.objects.filter(id=rid)
    # print(b)
    b.delete()
    return redirect("/userdashboard")

def view_detail(request,bid):
    # print("Id :",bid)
    b=Blog.objects.filter(id=bid)
    # print(b)
    context={}
    context["blog"]=b
    return render(request,"blog_details.html",context)

def is_published(request,status,rid):
    # print(status,rid)
    b=Blog.objects.filter(id=rid)
    # print(b)
    context={}
    context["blog"]=b
    if status=='P':
        b.update(is_published=True)
        context["pmessage"]='Blog Published'
    else:
        b.update(is_published=False)
        context["umessage"]='Blog Unpublished'
    return render(request,"blog_details.html",context)

# Cookies eg
def setcookies(request):
    res=render(request,"set_cookies.html")
    print("Response object:",res)
    res.set_cookie('name','NSH')
    return res

def getcookies(request):
    cdata=request.COOKIES['name']
    print("Cookie data:",cdata)
    context={}
    context['cookiedata']=cdata
    return render(request,'getcookies.html',context)


# Sessions
def setsession(request):
    request.session["learning"]='session and cookies'
    return render(request,'set_session.html')

def getsession(request):
    sdata=request.session['learning']
    print("data in session",sdata)
    context={}
    context["data"]=sdata
    return render(request,'get_session.html',context)



# django form eg
def djangoForm(request):
    context={}
    if request.method=="GET":
        s=StudentFormClass()
        # print(s)
        context["form"]=s
        return render(request,"student_form.html",context)
    else:
        n=request.POST["name"]
        r=request.POST["rno"]
        p=request.POST["percent"]
        # print(n,r,p)
        s=Student.objects.create(name=n,rno=r,p=p)
        return HttpResponse("data inserted")

def djangoModelForm(request):
    context={}
    if request.method=="GET":
        mform=StudentModelFormsClass()
        print(mform)
        context["mform"]=mform
        return render(request,"student_model_form.html",context)
    else:
        pass


def user_register(request):
    context={}
    if request.method=="GET":
        regfm=UserRegister()
        # print(regfm)
        context['rfm']=regfm
        return render(request,"register.html",context)
    else:
        print("POST")
        # print(request.POST)
        dregfm=UserRegister(request.POST)
        # print(dregfm)
        dregfm.save()
        return render(request,"register_success.html")
    
# login
def user_login(request):
    context={}
    loginfm=AuthenticationForm()
    context["lgfm"]=loginfm
    if request.method=="GET":
        return render(request,"login.html",context)
    else:
        uname=request.POST["username"]
        upass=request.POST["password"]
        # print(uname,upass)
        u=authenticate(username=uname,password=upass)
        # print("returned values by authenticate:",u)
        # print("id:",u.id)
        # print("password:",u.password)
        # print("is super user:",u.is_superuser)
        # print("email:",u.email)
        if u is not None:
            login(request,u)
            return redirect("/userdashboard")
        else:
            context["errmsg"]="invalid username and password!!!!"
            return render(request,"login.html",context)


def user_logout(request):
    logout(request)
    return redirect("/login")

# if statement
#     {% if cond %}
#     {% endif %}

#     {% if cond %}
#     {% else %}
#     {% endif %}

#     {% if cond %}
#     {% elif %}
#     {% else %}
#     {% endif %}

