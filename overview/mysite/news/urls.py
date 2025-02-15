from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>', views.month_archive),
    # path('articles/<int:year>/<int:month>/<int:pk>/', views.archive_detail),
]