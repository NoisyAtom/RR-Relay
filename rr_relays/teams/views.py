from django.http import HttpResponse, Http404
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

        if request.method == "POST":
            data = request.POST
            action = data.get("set_time")
            time_value = data.get("end")

            print(f"The request method is a POST....Follow Button is: {action}")
            print(f"Time value is: {time_value}")

        if request.method == "PUT":
            print("The request method is a PUT....")
        if request.method == "GET":
            print("The request method is a GET....")

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

            if request.method == "POST":
                data = request.POST
                action = data.get("set_time")
                time_value = data.get("end")
                print(f"Time value is: {time_value}")
                runner.end_time = time_value

                print(f"Runner end time is: {runner.end_time}")
                runner.save()

            return render(request, 'set_runner.html', context)

        except ObjectDoesNotExist as no_runner:
            print(f"Error: {no_runner}")
            message = f"There is no runner with that ID."
            #raise Http404(message)
            return HttpResponse(message)

    else:
        # queryset_list = Post.objects.active().order_by('-created')
        message = "Unauthorised User."
        return HttpResponse(message)


def runners(request):


    #queryset_list = Runner.objects.active().order_by('-created')
    all_runners = Runner.objects.all()
    for runner in all_runners:

        if (runner.start_time is not None) and (runner.end_time is not None):
            print("Start time and end time is not none.")

            if runner.start_time <= runner.end_time:
                elapsed_time = runner.end_time - runner.start_time
            else:
                elapsed_time = "Error start time is after end time"
        else:
            elapsed_time = "Not complete"

        print(f"Runner number: {runner.number}  Runner Name: {runner.first_name} - {runner.last_name}."
              f"Start time: {runner.start_time}  End time: {runner.end_time}  -   Elapsed Time: {elapsed_time} ")
        # Lets create a new field for elapsed time and populate it.
        runner.elapsed_time = elapsed_time
        context = {"runners_list": all_runners}

    return render(request, 'runner.html', context)


    #return HttpResponse("NOT IMPLEMENTED")



def teams(request):
    pass
    print("Teams got called")

    return HttpResponse("NOT IMPLEMENTED")
