from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'polls/home.html', context)


def create(request):
    context = {}
    return render(request, 'polls/create.html', context)


def vote(request, id):
    context = {}
    return render(request, 'polls/vote.html', context)


def results(request, id):
    context = {}
    return render(request, 'polls/results.html', context)
