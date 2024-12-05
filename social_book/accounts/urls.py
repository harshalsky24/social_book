from django.urls import path
from . import views

urlpatterns = [
    
    path('logout/',views.logout,name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = "logout"),
    path('authors-and-sellers/',views.authors_and_sellers, name = "authors_and_sellers"),
    path('upload-books/', views.upload_books, name = 'upload_books'),
    path('uploaded-files/', views.uploaded_files, name = 'uploaded_files'),
    path('fetch-books/',views.fetch_books, name = "fetch_books"),
    path('user-files/',views.user_files, name='user-files'),
    path('my-books/', views.my_books_view, name='my_books'),
    path('send-email/', views.send_email, name='send_email'),
]
