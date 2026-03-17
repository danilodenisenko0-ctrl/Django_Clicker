from django.shortcuts import render, redirect
from .models import Upgrade

def clicker(request):
    if 'score' not in request.session:
        request.session['score'] = 0

    if request.method == 'POST':
        request.session['score'] += 1

    upgrades = Upgrade.objects.all()

    return render(request, 'game/clicker.html', {
        'score': request.session['score'],
        'upgrades': upgrades
    })




def buy_upgrade(request, upgrade_id):
    upgrade = Upgrade.objects.get(id=upgrade_id)

    if request.session.get('score', 0) >= upgrade.price:
        request.session['score'] -= upgrade.price

    return redirect('clicker')