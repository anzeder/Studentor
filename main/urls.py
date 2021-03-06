from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='main'),
                  path('celebrity', views.celebrity, name='celebrity'),
                  path('about', views.about, name='about'),
                  path('create', views.create, name='create'),
                  path('find_mentor', views.find_mentor, name='find_mentor'),
                  path('register', views.register, name='register'),
                  path('mentor', views.MentorDashboard, name='mentor'),
                  path('mentor_auth', views.MentorRegister, name='mentor_auth'),
                  path('course_reg', views.MentorRegisterCourse, name='course_reg'),
                  path('create_course', views.createCourse, name='create_course')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
