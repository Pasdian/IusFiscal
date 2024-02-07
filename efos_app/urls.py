from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('person/<int:pk>/', views.PersonView.as_view()),
    path('persons/', views.SearchPersonView.as_view()),
    path('person-detail/<int:pk>', views.PersonDetailView.as_view()),
    path('person-details/', views.SearchPersonDetailView.as_view()),
    path('cancellation/<int:pk>', views.CancellationView.as_view()),
    path('cancellations/', views.SearchCancellations.as_view()),
    path('reduction/<int:pk>', views.ReductionView.as_view()),
    path('reductions/', views.SearchReductions.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
