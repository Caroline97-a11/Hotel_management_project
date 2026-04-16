from django.shortcuts import render, redirect
from .models import RoomType, Room
from .forms import RoomTypeForm,RoomForm

# Create your views here.

def createCategory(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('CategoryList')
    else:
        form = RoomTypeForm()

    return render(request, 'roomCategory.html', {'form': form})

def createRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('roomsList')
    else:
        form = RoomForm()

    return render(request, 'room.html', {'form': form})

def CategoryList(request):
    room_category = RoomType.objects.all()

    context = {
        'roomCategory': room_category,
    }

    return render(request, 'roomCategoryList.html', context)


def roomsList(request):
    all_rooms = Room.objects.all()
    context = {
        'rooms': all_rooms,
        'total_rooms': all_rooms.count(),
        'occupied_rooms': all_rooms.filter(room_status='Not_available').count(),
        'available_rooms': all_rooms.filter(room_status='Available').count(),
      
    }

    return render(request, 'roomList.html', context)

def roomDetail(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'roomDetail.html', {'room': room})

def editRoom(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('roomsList')
    else:
        form = RoomForm(instance=room)

    return render(request, 'editRoom.html', {'form': form})

def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('roomsList')

    return render(request, 'deleteRoom.html', {'room': room})