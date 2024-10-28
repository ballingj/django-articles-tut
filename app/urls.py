from django.urls import path
# from app.views import home, create_article  # function based view
from app.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    # path("", home, name="home"),
    # path("articles/create/", create_article, name="create_article"),  # function based view
    path("", ArticleListView.as_view(), name="articles"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article"),
]
  