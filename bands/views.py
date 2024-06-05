from django.shortcuts import render, get_object_or_404

from bands.models import Musician


def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {'musician': musician}
    return render(request, "musician.html", data)


def musicians(request):
    musicians = Musician.objects.all().order_by('last_name', 'first_name')
    data = {'musicians': musicians}
    return render(request, "musicians.html", data)