from django.shortcuts import render #render para renderizar o template
#from django.http import HttpResponse #HttpResponse ta sendo usado para dar uma resposta em HTML
from .forms import Form 
import math

# Create your views here.

def index (request): #index recebe uma requisição


    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            a = float(form.data['a'])
            b = float(form.data['b'])
            c = float(form.data['c'])

        if a != 0: 
            r = []
            if b*b - 4.0*a*c > 0.0:
                r.append((-b + math.sqrt(b*b - 4.0*a*c))/(2.0*a))
                r.append((-b - math.sqrt(b*b - 4.0*a*c))/(2.0*a))

            if b*b -4.0*a*c == 0.0:
                r.append( (-b+math.sqrt(b*b - 4.0*a*c) )/(2.0*a) )

            context = {
    'form': Form
}

            if b*b - 4.0*a*c > 0.0:
                r = [        (-b + math.sqrt(b*b - 4.0*a*c)) / (2.0*a),        (-b - math.sqrt(b*b - 4.0*a*c)) / (2.0*a)    ]
                context['r'] = r
            elif b*b - 4.0*a*c == 0.0:
                r = [(-b + math.sqrt(b*b - 4.0*a*c)) / (2.0*a)]
                context['r'] = r
            else:
                context['sr'] = True

            return render(request=request, template_name="index.html", context=context)

               

    context = {'form': Form}

    return render(request=request, template_name= 'index.html', context=context)

