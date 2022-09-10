from re import template
from django.http import HttpResponse
#from django.template import Template, Context
#import pathlib
from django.template import loader

#path = pathlib.Path(__file__).parent.resolve()

def familia(self):
    planilla = loader.get_template('familia.html')
    documento = planilla.render()
    return HttpResponse(documento)




    #familia = open (f'{path}./template/familia.html')
    #planilla = Template(familia.read())
    #familia.close()
    #miContexto = Context()
    #documento = planilla.render(miContexto)
    #return HttpResponse(documento)