from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from bands.models import Musician, Band, Venue, Room

DEFAULT_PAGE_NUMBER = 1
DEFAULT_PAGE_SIZE = 2
MAX_PAGE_SIZE = 100


def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {"musician": musician}
    return render(request, "musician.html", data)


def musicians(request):
    all_musicians = Musician.objects.all().order_by("last_name", "first_name")

    page_num = request.GET.get("page", DEFAULT_PAGE_NUMBER)
    page_num = int(page_num)
    page_size = request.GET.get("size", DEFAULT_PAGE_SIZE)
    page_size = int(page_size)

    paginator = Paginator(all_musicians, page_size)

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    if page_size < 2:
        page_size = 1
    elif page_size > MAX_PAGE_SIZE:
        page_size = MAX_PAGE_SIZE

    page = paginator.page(page_num)
    data = {
        "musicians": page.object_list,
        "page": page,
        "page_size": page_size,
    }

    return render(request, "musicians.html", data)


def bands(request):
    all_bands = Band.objects.all().order_by("name")
    data = {"bands": all_bands}
    return render(request, "bands.html", data)


def band(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    data = {"band": band}
    return render(request, "band.html", data)


def venues(request):
    all_venues = Venue.objects.all().order_by("name")
    data = {"venues": all_venues}
    return render(request, "venues.html", data)
