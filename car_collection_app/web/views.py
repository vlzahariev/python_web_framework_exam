from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection_app.web.models import Profile, Car


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    user = get_profile()

    context = {
        'user': user,
    }

    return render(request, 'common/index.html', context)


def create_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


def edit_profile(request):
    user = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=user)
    else:
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    user = get_profile()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=user)
    else:
        form = ProfileDeleteForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profile/profile-delete.html', context)


def details_profile(request):
    user = get_profile()
    car = Car.objects.all()
    car_price_count = 0
    for cars in car:
        car_price_count += cars.price

    name = ''
    if user.first_name:
        name += user.first_name
    if user.last_name:
        name += ' ' + user.last_name

    context = {
        "user": user,
        'car_price_count': car_price_count,
        'name': name,
    }
    return render(request, 'profile/profile-details.html', context)


def catalogue(request):
    user = get_profile()
    car = Car.objects.all()
    car_count = Car.objects.count()
    context = {
        "user": user,
        'car': car,
        'car_count': car_count,
    }
    return render(request, 'common/catalogue.html', context)


def create_car(request):
    if request.method == "GET":
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == "GET":
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car
    }
    return render(request, 'car/car-details.html', context)
