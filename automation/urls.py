from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('summarize/', views.summarize_text, name='summarize'),
    path('analyze-csv/', views.analyze_csv, name='analyze_csv'), 
    path("draft-email/", views.draft_email, name="draft_email"),


]
