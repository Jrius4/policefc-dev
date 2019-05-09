from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, redirect, get_list_or_404, reverse, get_object_or_404
from .models import SoccerPlayer, ExecutiveTeam,TeamPosition, TechnicalTeam
from django.db.models import Count, Q
from apps.posts.models import Author
from .forms import SoccerPlayersForm,ExecutiveForm


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = SoccerPlayer.objects.all()
    query = request.GET.get('spq')
    if query:
        queryset = queryset.filter(
            Q(full_name_icontains=query) |
            Q(team_positions_icontains=query)
        ).distinct()

    context ={
        'queryset':queryset
    }
    return render(request, 'team/search_soccer_players.html', context)

def player_detail(request, id):
    return render(request, 'team/player_detail.html', {})

def technical_member_detail(request, id):
    return render(request, 'team/technical_member_detail.html', {})


def executive_member_detail(request, id):
    return render(request, 'team/executive_member__detail.html', {})


def player_list(request):
    soccer_player_list = SoccerPlayer.objects.all()
   
    context = {
        'soccer_player_list':soccer_player_list,
    }
    return render(request, 'team/players_list.html', context)

def player(request, id):
    player = get_object_or_404(SoccerPlayer, id=id)
    most_recent = SoccerPlayer.objects.order_by('-timestamp')[:3]
   
    context = {

        'player': player,
        'most_recent': most_recent,
    }
    return render(request, 'team/player_detail.html', context)

def executive(request, id):
    executive = get_object_or_404(ExecutiveTeam, id=id)
    most_recent = ExecutiveTeam.objects.order_by('-timestamp')[:3]
   
    context = {
        'executive': executive,
        'most_recent': most_recent,
    }
    return render(request, 'team/executive_create.html', context)

def create_executive(request):
    title = 'Create Executive'
    form = ExecutiveForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("executive-member",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/executive_create.html", context)

def update_executive(request, id):
    executive = get_object_or_404(ExecutiveTeam, id=id)
    most_recent = ExecutiveTeam.objects.order_by('-timestamp')[:3]
   
    context = {
        'executive': executive,
        'most_recent': most_recent,
    }
    return render(request, 'team/executive_member.html', context)

def technical_team_list(request):
    tech_team_listing = TechnicalTeam.objects.all()
    
    context = {
        'tech_team_listing': tech_team_listing
    }
    return render(request, 'team/technical_team_list.html', context)

def executive_team_list(request):
    executives_listing = ExecutiveTeam.objects.all()
    
    context = {
        'executives_listing': executives_listing
    }
    return render(request, 'team/executive_team_list.html', context)


def create_player(request):
    title = 'Create Player'
    form = SoccerPlayersForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("player-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/player_create.html", context)



def update_player(request, id):
    title = 'Update'
    player = get_object_or_404(SoccerPlayer, id=id)
    form = SoccerPlayersForm(
        request.POST or None,
        request.FILES or None, instance=player)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("player-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/player_create.html", context)


def delete_player(request, id):
    player = get_object_or_404(SoccerPlayer, id=id)
    player.delete()
    return redirect(reverse("team/players_list.html"))