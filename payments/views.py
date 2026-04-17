from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm



def payment_list(request):
    if not request.user.is_authenticated:
        return redirect('logIn')

    payments = Payment.objects.all()

    return render(request, 'payment_list.html', {
        'payments': payments
    })

def create_payment(request):
    if not request.user.is_authenticated:
        return redirect('logIn')

    form = PaymentForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('payment_list')

    return render(request, 'payment_form.html', {
        'form': form
    })


def edit_payment(request, id):
    if not request.user.is_authenticated:
        return redirect('logIn')

    payment = get_object_or_404(Payment, id=id)

    form = PaymentForm(request.POST or None, instance=payment)

    if form.is_valid():
        form.save()
        return redirect('payment_list')

    return render(request, 'payment_form.html', {
        'form': form,
        'payment': payment
    })


def delete_payment(request, id):
    if not request.user.is_authenticated:
        return redirect('logIn')

    payment = get_object_or_404(Payment, id=id)

    if request.method == "POST":
        payment.delete()
        return redirect('payment_list')

    return render(request, 'payment_delete.html', {
        'payment': payment
    })