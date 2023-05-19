from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return HttpResponse( "Это твой помощник на случай, если ты испытываешь недомогание в какой-либо сфере эмоционального состояния. Здесь ты найдешь вполне примитивные вдохновляющие картинки, мемы, и ,возможно, даже баяны")
def about(request):
    return render(request, 'about.html', {})

def apathy(request):
    return HttpResponse("Текс об апатии")

def apathy(request):
    return render(request, 'apathy.html', {})

def procrastination(request):
    return HttpResponse("Текст о прокрастинации")
def procrastination(request):
    return render(request, 'procrastination.html', {})

def sadness(request):
    return HttpResponse("Текст о грусти")

def sadness(request):
    return render(request, 'sadness.html', {})


def contacts(request):
    return HttpResponse("Нас сложно найти, невозможно забыть, но легко потерять")


def services(request):
    return HttpResponse()


def products(request):
    return HttpResponse()

def products(request):
    return render(request, 'products.html', {})