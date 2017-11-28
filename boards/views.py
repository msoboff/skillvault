from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Sport, Skill

def home(request):
    sports = Sport.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q').lower()
        skills = Skill.objects.filter(
            Q(player_name__icontains=query) | Q(name=query)
        )
        return render(request, 'home.html', {'skills': skills})

def soccer(request):
    sport = Sport.objects.get(name='Soccer')
    skills = Skill.objects.filter(sport=sport)
    return render(request, 'soccer.html', {'skills': skills})

def basketball(request):
    sport = Sport.objects.get(name='Basketball')
    skills = Skill.objects.filter(sport=sport)
    return render(request, 'basketball.html', {'skills': skills})

def futsal(request):
    sport = Sport.objects.get(name='Futsal')
    skills = Skill.objects.filter(sport=sport)
    return render(request, 'futsal.html', {'skills': skills})
