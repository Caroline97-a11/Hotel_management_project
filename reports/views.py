from django.shortcuts import render
from django.db.models import Sum

from guests.models import Guest
from rooms.models import Room
from payments.models import Payment


def dashboard(request):

    total_guests = Guest.objects.count()
    total_rooms = Room.objects.count()

    payments = Payment.objects.all().order_by('-payment_date')

    total_payments = Payment.objects.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    cash_total = Payment.objects.filter(
        payment_type='Cash'
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    momo_total = Payment.objects.filter(
        payment_type='Mobile'
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    card_total = Payment.objects.filter(
        payment_type='Card'
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    context = {
        'total_guests': total_guests,
        'total_rooms': total_rooms,

        'payments': payments,

        'total_payments': total_payments,
        'cash_total': cash_total,
        'momo_total': momo_total,
        'card_total': card_total,
    }

    return render(request, 'dashboard.html', context)