from django.shortcuts import render, redirect
from django.http import HttpResponse
from cccmv.mitgliederverwaltung.models import Mitglied
# Create your views here.



def index(request):
    return redirect('cccmv.mitgliederverwaltung.views.listMember')


def listMember(request):
    context = {
        'memberlist': Mitglied.objects.all()
    }
    return render(request, 'mitgliederverwaltung/member_list.html', context)


def showMember(request, memberId):
    return HttpResponse("Hello single member %s" % memberId)


def deleteMember(request, memberId):
    return HttpResponse("Hello delete Member %s" % memberId)


def createMember(request):
    return HttpResponse("Hello create Member")
