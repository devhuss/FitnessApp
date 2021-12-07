from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm, ContactForm
from django.contrib.auth.decorators import login_required


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Query the to-do table and get the todos specific for the user
    return render(request, 'workout/index.html')


@login_required(login_url='login')
def create_workout(request):
    form = WorkoutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'workout/add.html', context)


@login_required(login_url='login')
def search_workout(request):
    search_term = request.GET.get('search-term') or ''
    # query the database to find records that match with two criteria: user (user_id), and contains the search term
    workouts = Workout.objects.filter(user=request.user, workout__icontains=search_term)
    context = {'workouts': workouts, 'search_term': search_term}
    return render(request, 'workout/index.html', context)


@login_required(login_url='login')
def delete_workout(request, id):
    workout_object = Workout.objects.get(id=id)
    workout_object.delete()
    return redirect('log')


@login_required(login_url='login')
def update_workout(request, id):
    task = Workout.objects.get(id=id)
    form = WorkoutForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('log')

    return render(request, 'workout/update.html', {'form': form})


@login_required(login_url='login')
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'workout/contact.html', context)


@login_required(login_url='login')
def goals(request):
    return render(request, 'workout/goals.html')


@login_required(login_url='login')
def log(request):
    workouts = Workout.objects.filter(user=request.user)
    context = {'workouts': workouts}
    return render(request, 'workout/log.html', context)
#
#
# def complete_workout(request, id):
#     workout_object = Workout.objects.get(id=id)
#     workout_object.complete = True
#     workout_object.save()
#
#     return redirect('index')
