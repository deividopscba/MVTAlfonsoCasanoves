from urllib import request
from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import familia
from django.shortcuts import render



def familiass(self):
   miFamilia = familia.objects.all()
   data={'miFamilia':miFamilia}
   planilla = loader.get_template('familia.html')
   documento = planilla.render(data)
   return HttpResponse(documento)
   



    











