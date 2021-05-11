from django.urls import path
from .views import QuestionListView , QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, UserPostListView, PandaProfileView
from . import views



urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('panda/<int:pk>/', PandaProfileView.as_view(), name='panda-profile'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('question/new/', QuestionCreateView.as_view(), name='question-create'),
    path('profile/questions',UserPostListView.as_view(), name = 'user-questions'),
    path('search_title/', views.search_title, name='search-title'),
    path('about/', views.about, name='home-about'),
    path('voteans/', views.voteans, name='voteans'),
    path('voteques/',views.voteques, name = 'voteques')
]

