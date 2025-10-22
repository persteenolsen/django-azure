# example/urls.py
from django.urls import path

from example.views.alpha import index

from example.views.alpha import about

from example.views.alpha import me

from example.views.beta import blog

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

]