from django.views import View
from django.shortcuts import render, redirect, reverse
from .models import Bike, Basket, Order, Seat, Frame, Tire
from .forms import BikePurchaseForm


def bikes(request):
    all_bikes = Bike.objects.all()
    bike_count = all_bikes.count()
    all_seats = Seat.objects.all()
    all_frames = Frame.objects.all()
    all_tires = Tire.objects.all()
    return render(request, 'shop/bikes.html', {'all_bikes': all_bikes, 'bike_count': bike_count, 'all_seats': all_seats, 'all_frames': all_frames, 'all_tires': all_tires})


class BikeView(View):
    def get(self, request, pk, *args, **kwargs):
        bike = Bike.objects.filter(id=pk).first()
        basket = Basket.objects.first()
        form = BikePurchaseForm()
        return render(request, 'shop/bikedetails.html', {'bike': bike, 'basket': basket, 'form': form})

    def post(self, request, pk, *args, **kwargs):
        form = BikePurchaseForm(request.POST)
        bike = Bike.objects.filter(id=pk).first()
        basket = Basket.objects.first()
        if form.is_valid():
            order = Order(
                bike=bike,
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                phone_number=form.cleaned_data['phone_number'],
                status='P'
            )
            order.save()

            bike.frame.quantity -= 1
            bike.seat.quantity -= 1
            bike.tire.quantity -= 2
            if bike.has_basket:
                basket.quantity -= 1
                basket.save()

            bike.frame.save()
            bike.seat.save()
            bike.tire.save()

            return redirect(reverse('order_detail', args=[order.pk]))
        return render(request, 'shop/bikedetails.html', {'bike': bike, 'basket': basket, 'form': form})


def order_detail(request, pk):
    order = Order.objects.filter(id=pk).first()
    return render(request, 'shop/order.html', {'order': order})
