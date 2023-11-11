
from django.urls import path
from blogapp import views

urlpatterns = [
    path("about",views.contactPage),
    path("contact",views.aboutPage),
    # path("home/<x>/<y>",views.homePage),
    path("hello",views.helloView),
    path("",views.homePage),
    path("userdashboard",views.userDashboard),
    path("createblog",views.createBlog),
    path("edit_blog/<rid>",views.editBlog),
    path("delete_blog/<rid>",views.deleteBLog),
    path("see_detail/<bid>",views.view_detail),
    path("publish/<status>/<rid>",views.is_published),
    path("setcookie",views.setcookies),   
    path("getcookie",views.getcookies),
    path("setsession",views.setsession),
    path("getsession",views.getsession), 
    path("dform",views.djangoForm), 
    path("django_model_form",views.djangoModelForm),
    path("register",views.user_register),
    path("login",views.user_login),
    path("logout",views.user_logout)
]
