from django.urls import path
from .views import(
    create_contestant_view,
    president_view,
    vice_president_view,
    general_secretary_view,
    assistant_general_secretary_view,
    treasurer_view,
    financial_secretary_view,
    librarian_view,
    sports_director_view,
    pro_view
)

app_name = "vote"
urlpatterns = [
    path('president', president_view, name='president'),
    path('vicepresident', vice_president_view, name='vicepresident'),
    path('generalsecretatry', general_secretary_view, name='generalsecretatry'),
    path('assistantgeneralsecretary', assistant_general_secretary_view, 'assistantgeneralsecretary'),
    path('treasurer', treasurer_view, name='treasurer'),
    path('financialsecretary', financial_secretary_view, 'financialsecretary'),
    path('librarian', librarian_view, name='librarian'),
    path('pro', pro_view, name='pro'),
    path('sportsdirector', sports_director_view, name='sportsdirector')

]