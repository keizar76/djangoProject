from django.urls import path
from . import views
from .views import home,contact,gallery

urlpatterns = [
    #path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    path('', home, name="home"),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
]
