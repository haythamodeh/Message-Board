from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r"^registerProcess$", views.registerProcess), 
    url(r"^success$", views.success),
    url(r"^loginProcess$", views.loginProcess),   
    url(r"^logout$", views.logout),
    url(r"^postMessageProcess$", views.postMessageProcess),
    url(r"^postCommentProcess$", views.postCommentProcess),
]