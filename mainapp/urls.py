from django.urls import path
from mainapp import views


urlpatterns = [
  path('', views.mainPage, name='main'),
  path('about/', views.aboutPage, name='about'),
  path('course/', views.coursePage, name='course'),
  path('contact/', views.contactPage, name='contact'),
  # path('blog/',views.blogPage, name='blog'),
  path('single/', views.singlePage, name='single'),
  path('teachers/', views.teacherPage, name='teachers'),
  path('students/', views.studentPage, name='students'),
  path('register/', views.registerUser, name='register'),
  path('table/', views.tablePage, name='table'),
  path('create/', views.createPage, name='create'),
  path('login/',views.loginPage, name='login')
]