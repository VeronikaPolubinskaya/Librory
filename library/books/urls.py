from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list),
    path('detail/<int:book_id>/', views.book_detail),
    path('add/', views.add_book),
    path('update/<int:book_id>/', views.update_book),
    path('delete/<int:book_id>/', views.delete_book),
    path('find/<str:book_name>/', views.find_book_by_name),
]