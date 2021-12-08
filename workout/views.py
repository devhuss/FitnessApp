from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm, ContactForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request, 'workout/index.html')


@login_required(login_url='login')
def create_workout(request):
    form = WorkoutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('log')

    context = {'form': form}
    return render(request, 'workout/add.html', context)


@login_required(login_url='login')
def delete_workout(request, id):
    workout_object = Workout.objects.get(id=id)
    workout_object.delete()
    return redirect('log')


@login_required(login_url='login')
def update_workout(request, id):
    workout = Workout.objects.get(id=id)
    form = WorkoutForm(request.POST or None, instance=workout)
    if form.is_valid():
        form.save()
        return redirect('log')

    return render(request, 'workout/update.html', {'form': form})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'workout/contact.html', context)


@login_required(login_url='login')
def log(request):
    workouts = Workout.objects.filter(user=request.user)
    context = {'workouts': workouts}
    return render(request, 'workout/log.html', context)
