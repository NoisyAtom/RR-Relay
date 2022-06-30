from django.http import HttpResponse
from django.shortcuts import render
from .models import Runner
from django.db.models import ObjectDoesNotExist


def index(request):
    return HttpResponse("Hello, world. You're at the runneymede runners index.")

# Create your views here.


def find_runner(request, runner_id):

    # Ensure that all characters are upper case.
    runner_id = runner_id.upper()

    if request.user.is_staff or request.user.is_superuser:
        #queryset_all_runners = Post.objects.all().order_by('-created')
        try:
            runner = Runner.objects.get(number=runner_id)
            message = f"Runner is: {runner.first_name} {runner.last_name}   " \
                      f"Number: {runner.number}  Age: {runner.age}  " \
                      f"Start time: {runner.start_time}  End time: {runner.end_time}"
            # message = "You are authorised!."
            print(f"Message: {message}")
            context = {"number": runner.number,
                       "name": f"{runner.first_name}   {runner.last_name}",
                       "gender": runner.gender,
                       "age": runner.age,
                       "start_time": runner.start_time,
                       "end_time": runner.end_time}
            return render(request, 'index.html', context)

        except ObjectDoesNotExist as no_runner:
            print(f"Error: {no_runner}")
            message = f"There is no runner with that ID."
            return HttpResponse(message)

    else:
        # queryset_list = Post.objects.active().order_by('-created')
        message = "Unauthorised User."
        return HttpResponse(message)


def set_runner_time(request):
    pass

    return HttpResponse("NOT IMPLEMENTED")
