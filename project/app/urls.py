from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.InsertPageViews, name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/", views.Showpage, name="showpage"),
    path("editpage/<int:pk>",views.Editpage,name="editpage"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),
 ]
