from django.urls import path
from . import views

urlpatterns = [
     path('calicut/',views.calicut,name='clt'),
     path('kt5/',views.html5,name='kerala'),
     path('alappi/',views.alappuzha,name='alappi'),
     path('idukki/',views.idukki,name='idk'),
     path('kochi/',views.kochi,name='kochi'),
     path('wayanad/',views.wayanad, name='wayanad')
]





# githob personal access token : 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