from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Room


# I stopped at 1:21:30
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = get_object_or_404(Room, pk=pk)

    context = {"room": room}
    return render(request, 'base/room.html', context)
