# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    
    path("", views.Index.as_view(), name="index"),
    path("form/", views.Form.as_view(), name="form"),
    path("icon/", views.Icon.as_view(), name="icon"),
    path("buttons/", views.Button.as_view(), name="buttons"),
    path("typography/", views.Typography.as_view(), name="typography"),
    path("charts/", views.Chart.as_view(), name="charts"),
    path("tables/", views.Table.as_view(), name="tables"),
    path("error/", views.Error.as_view(), name="error"),
    
    path("book_create/", views.BookCreate.as_view(), name="book_create"),
    path("book_list/", views.BookList.as_view(), name="book_list"),
    path("book_detail/<str:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("book_update/<str:pk>/", views.BookUpdate.as_view(), name="book_update"),
    path("book_delete/<str:pk>/", views.BookDelete.as_view(), name="book_delete"),
    path("book_table/", views.BookTable.as_view(), name="book_table"),
    
    path("author_create/", views.AuthorCreate.as_view(), name="author_create"),
    path("author_list/", views.AuthorList.as_view(), name="author_list"),
    path("author_detail/<str:pk>/", views.AuthorDetail.as_view(), name="author_detail"),
    path("author_update/<str:pk>/", views.AuthorUpdate.as_view(), name="author_update"),
    path("author_delete/<str:pk>/", views.AuthorDelete.as_view(), name="author_delete"),
    
    path("user_list/", views.UserList.as_view(), name="user_list"),
    path("user_create/", views.UserCreate.as_view(), name="user_create"),
    path("user_update/<str:pk>/", views.UserUpdate.as_view(), name="user_update"),
    path("user_delete/<str:pk>/", views.UserDelete.as_view(), name="user_delete"),
    

]

