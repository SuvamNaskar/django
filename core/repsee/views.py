from django.shortcuts import render, redirect
from .models import *

def receipes(req):
    if req.method == 'POST':
        data = req.POST
        image = req.FILES.get('image')
        name = data.get('name')
        desc = data.get('desc')

        Receipe.objects.create(
            name = name,
            desc = desc,
            image = image
        )

        return redirect('/receipes')
    
    queryset = Receipe.objects.all()
    context = {'receipes': queryset, 'page': 'Receipes'}

    return render(req, 'receipes.html', context)