from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Runner, Teams
from django.db.models import ObjectDoesNotExist
from datetime import datetime
from dateutil import parser
import pytz


tz_lon = pytz.timezone("Europe/London")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def timer(request):
    template = loader.get_template('timer.html')
    return HttpResponse(template.render())


def runner(request):
    template = loader.get_template('runner.html')
    return HttpResponse(template.render())


def teams(request):

    # Get all teams
    all_teams = Teams.objects.all()

    for team in all_teams:
        print(f"Team: {team.number}  Name: {team.name}")

    template = loader.get_template('teams.html')
    context = {"teams": all_teams}
    return render(request, 'teams.html', context)
    #return HttpResponse(template.render(context))


def set_race(request):

    context={"name":"christine"}
    template = loader.get_template('set_race.html')
    return HttpResponse(template.render(context))

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

            if request.method == "POST":
                data = request.POST
                action = data.get("set_time")
                time_value = data.get("end")
                print(f"Time value is: {time_value}")
                datetime_object = parser.parse(time_value)
                runner.end_time = tz_lon.localize(datetime_object)

                #runner.end_time = datetime_object
                print(f"The end time type is: {type(runner.end_time)}")

                if runner.start_time <= runner.end_time:
                    elapsed_time = runner.end_time - runner.start_time

                    print(f"OK : {type(elapsed_time)}")
                    print(f"OK2 : {type(runner.end_time)}")
                else:
                    print(f"Error start time is after end time: {runner.end_time}")

                # Now calculate elapsed time
                # if (runner.start_time is not None) and (runner.end_time is not None):
                #
                #     if runner.start_time <= runner.end_time:
                #         runner.elapsed_time = runner.end_time - runner.start_time
                #     else:
                #         print(f"Error start time is after end time: {runner.end_time}")
                # else:
                #     print(f"Error start time is NULL: {runner.start_time}")

                print(f"Runner end time is: {runner.end_time}")
                print(f"Runners elapsed time is: {runner.elapsed_time}")
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

