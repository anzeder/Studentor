from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('newProfile', views.get_profile, name='new-profile'),
                  path('mentor-profile', views.get_mentor_profile, name='new-mentor-profile'),
                  path('mentor-profile/week', views.sort_by_week_student, name='week-mm'),
                  path('mentor-profile/nextweek', views.sort_by_next_week_student, name='next-week-mm'),
                  path('mentor-profile/month', views.sort_by_month_student, name='month-mm'),
                  path('vacancy', views.get_vacancy, name='get-vacancy'),
                  path('reg', views.register, name='registration'),
                  path('signin', views.login, name='signin'),
                  path('signout', views.logOut, name='signout'),
                  path('profile', views.profile, name='profile'),
                  path('adminPage', views.showthis, name='admin'),
                  path('updateprofile', views.profile_update, name='update_profile'),
                  path('profile/<int:pk>/', views.profiles, name='profilePlace'),
                  path('profile/<int:pk>/followers/', views.ListFollowers, name='list-followers'),
                  path('profile/<int:pk>/followers/add', views.AddFollower, name='add-followers'),
                  path('profile/<int:pk>/followers/remove', views.RemoveFollower, name='remove-followers'),
                  path('deleted', views.deleted, name='deleted'),
                  path('resetPass', auth_views.PasswordResetView.as_view(template_name="account/passReset.html"),
                       name="reset_password"),
                  path('resetPass_sent',
                       auth_views.PasswordResetDoneView.as_view(template_name="account/resetSend.html"),
                       name="password_reset_done"),
                  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
                       name="password_reset_confirm"),
                  path('resetPass_complete',
                       auth_views.PasswordResetCompleteView.as_view(template_name="account/pass_reset_done.html"),
                       name="password_reset_complete")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
