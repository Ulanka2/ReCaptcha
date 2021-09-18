from django.shortcuts import render, HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Ура! Ты человек..")
        else:
            return HttpResponse("ООПА! Подозревается бот.") 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})



# from rest_framework.response import Response
# from contact.serializers import ContactFormSerializer
# from rest_framework import generics

# class NewsListView(generics.CreateAPIView):
#     serializer_class = ContactFormSerializer
    