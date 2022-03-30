from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import Aprel_1, Aprel_2, Dekabr_1, Dekabr_2, Fevral_1, Fevral_2, Mart_1, Mart_2, May_1, May_2, Noyabr_1, Noyabr_2, Oktyabr_1, Oktyabr_2, Sentyabr_1, Sentyabr_2, Yanvar_1, Yanvar_2

# Create your views here.


    

    
class Sentyabr1(ListView):
    template_name ="sentyabr1.html"
    model =  Sentyabr_1
    
class Sentyabr2(ListView):
    template_name ="sentyabr2.html"
    model =  Sentyabr_2
    
class Oktyabr1(ListView):
    template_name ="oktabr1.html"
    model =  Oktyabr_1
    
class Oktyabr2(ListView):
    template_name ="oktabr2.html"
    model =  Oktyabr_2
    
class Noyabr1(ListView):
    template_name ="noyabr1.html"
    model =  Noyabr_1
    
class Noyabr2(ListView):
    template_name ="noyabr2.html"
    model =  Noyabr_2
    
class Dekabr1(ListView):
    template_name ="dekabr1.html"
    model =  Dekabr_1
    
class Dekabr2(ListView):
    template_name ="dekabr2.html"
    model =  Dekabr_2
    
class Yanvar1(ListView):
    template_name ="yanvar1.html"
    model =  Yanvar_1
    
class Yanvar2(ListView):
    template_name ="yanvar2.html"
    model =  Yanvar_2
    
class Fevral1(ListView):
    template_name ="fevral1.html"
    model =  Fevral_1
    
class Fevral2(ListView):
    template_name ="fevral2.html"
    model =  Fevral_2
    
class Mart1(ListView):
    template_name ="mart1.html"
    model =  Mart_1
    
class Mart2(ListView):
    template_name ="mart2.html"
    model =  Mart_2
    
class Aprel1(ListView):
    template_name ="aprel1.html"
    model =  Aprel_1
    
class Aprel2(ListView):
    template_name ="aprel2.html"
    model =  Aprel_2
    
class May1(ListView):
    template_name ="may1.html"
    model =  May_1
    
class May2(ListView):
    template_name ="may2.html"
    model =  May_2
    
    
    
    
    
    