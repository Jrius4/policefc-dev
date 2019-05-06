from django.shortcuts import render



def player_detail(request, id):
    return render(request, 'player_detail.html', {})

def technical_member_detail(request, id):
    return render(request, 'technical_member_detail.html', {})


def executive_member_detail(request, id):
    return render(request, 'executive_member__detail.html', {})


def player_list(request):
    return render(request, 'player_list.html', {})

def technical_team_list(request):
    return render(request, 'technical_team_list.html', {})

def executive_team_list(request):
    return render(request, 'executive_team_list.html', {})

