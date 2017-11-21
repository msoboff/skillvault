from django.shortcuts import render, get_object_or_404
from .models import Sport, Skill

def home(request):
    sports = Sport.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q').lower()
        skills = Skill.objects.filter(name=query)
        return render(request, 'home.html', {'skills': skills})



def soccer(request):
    sport = Sport.objects.get(name='Soccer')
    skills = Skill.objects.filter(sport=sport)
    return render(request, 'soccer.html', {'skills': skills})
