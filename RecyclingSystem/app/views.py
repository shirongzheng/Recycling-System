from django.shortcuts import render, HttpResponse



def index(request):
    # print(request.user)
    return render(request, "app/index.djhtml")

