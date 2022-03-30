from django.urls import path

from probalar_app.models import Aprel_1, Aprel_2, Fevral_1, Mart_1, Mart_2, May_1, May_2, Yanvar_1, Yanvar_2
from .views import Oktyabr1, Oktyabr2, Sentyabr1, Sentyabr2, Noyabr1, Noyabr2,  Dekabr1, Dekabr2,  Yanvar1, Yanvar2, Fevral1, Fevral2, Mart1, Mart2, Aprel1, Aprel2, May1, May2
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="basehome.html"), name = 'base'),
    path('1_kurslar/', TemplateView.as_view(template_name="basemonths1.html"), name = 'basemonths1'),
    path('2_kurslar/', TemplateView.as_view(template_name="basemonths2.html"), name = 'basemonths2'),
    path('1_kurslar/Sentyabr/',  Sentyabr1.as_view(),name = 'sentyabr1'),
    path('2_kurslar/Sentyabr/',  Sentyabr2.as_view(),name = 'sentyabr2'),
    path('1_kurslar/Oktyabr/',  Oktyabr1.as_view(),name = 'oktyabr1'),
    path('2_kurslar/Oktyabr/',  Oktyabr2.as_view(),name = 'oktyabr2'),
    path('1_kurslar/Noyabr/',  Noyabr1.as_view(),name = 'noyabr1'),
    path('2_kurslar/Noyabr/',  Noyabr2.as_view(),name = 'noyabr2'),
    path('1_kurslar/Dekabr/',  Dekabr1.as_view(),name = 'dekabr1'),
    path('2_kurslar/Dekabr/',  Dekabr2.as_view(),name = 'dekabr2'),
    path('1_kurslar/Yanvar/',  Yanvar1.as_view(),name = 'yanvar1'),
    path('2_kurslar/Yanvar/',  Yanvar2.as_view(),name = 'yanvar2'),
    path('1_kurslar/Fevral/',  Fevral1.as_view(),name = 'fevral1'),
    path('2_kurslar/Fevral/',  Fevral2.as_view(),name = 'fevral2'),
    path('1_kurslar/Mart/',  Mart1.as_view(),name = 'mart1'),
    path('2_kurslar/Mart/',  Mart2.as_view(),name = 'mart2'),
    path('1_kurslar/Aprel/',  Aprel1.as_view(),name = 'aprel1'),
    path('2_kurslar/Aprel/',  Aprel2.as_view(),name = 'aprel2'),
    path('1_kurslar/May/',  May1.as_view(),name = 'may1'),
    path('2_kurslar/May/',  May2.as_view(),name = 'may2'),
]
    
