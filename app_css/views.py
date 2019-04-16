from django.shortcuts import render,redirect
from ac_citizen.models import CitizenRegister


def activeCity(request):
    del request.session['officer']
    return redirect('index')

def citiActive(request):
    del request.session['ctid']
    del request.session['citizen']
    return redirect('index')


def adminActive(request):
    del request.session['admin']
    return redirect('index')