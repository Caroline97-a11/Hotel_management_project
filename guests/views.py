from django.shortcuts import render, redirect, get_object_or_404
from guests.models import Guest
from guests.forms import GuestForm


def addGuest(request):
    form = GuestForm()

    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestList')

    return render(request, 'add_guest.html', {'form': form})

def guestList(request):
    all_guests = Guest.objects.all()
    context = {
        'guests': all_guests,
        'total_guests': all_guests.count(),
        'checked_in': all_guests.filter(guest_status='checked_in').count(),
        'checked_out': all_guests.filter(guest_status='checked_out').count(),
    }
    return render(request, 'guestList.html', context)

def viewGuest(request, pk):
    guests = get_object_or_404(Guest, id=pk)
    return render(request, 'view_guest.html', {'guests': guests})


def editGuest(request, pk):
    guests = get_object_or_404(Guest, id=pk)

    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guests)
        if form.is_valid():
            form.save()
            return redirect('guestList')
    else:
        form = GuestForm(instance=guests)

    return render(request, 'edit_guest.html', {'form': form, 'guests': guests})


def deleteGuest(request, pk):
    guests = get_object_or_404(Guest, id=pk)

    if request.method == 'POST':
        guests.delete()
        return redirect('guestList')

    return render(request, 'delete_guest.html', {'guests': guests})