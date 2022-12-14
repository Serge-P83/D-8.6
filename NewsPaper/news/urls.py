from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, NewsSearch
)




urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='delete'),
]
