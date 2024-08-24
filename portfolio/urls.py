from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='home'),  # 'home' is used as the name here
    path('brief-summary/', views.brief_summary, name='brief_summary'),
    path('skills/', views.skills, name='skills'),
    path('completed-projects/', views.completed_projects, name='completed_projects'),
    path('ongoing-projects/', views.ongoing_projects, name='ongoing_projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('contact-list/', views.contact_list, name='contact_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),  # Assuming you have a signup view
]

