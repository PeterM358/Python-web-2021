from django.shortcuts import render


def index(req):
    return render(req, 'main_app/index.html')


def test(req):
    pass

