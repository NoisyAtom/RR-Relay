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
    print("Index page called")
    # Get fastest 20 teams
    # all_teams = Teams.objects.all()
    first_teams =Teams.objects.all().filter(elapsed_time__isnull=False).order_by('elapsed_time')
    for team in first_teams:
        print(f"Runner: {team.number} Name: {team.name} Time: {team.elapsed_time}")
        et = str(team.elapsed_time)
        team.elapsed_time = et
        print(f"Team: {team.number} Name: {team.name} Time: {team.elapsed_time}")

   


    first_runners = Runner.objects.all().filter(elapsed_time__isnull=False).order_by('elapsed_time')
    for runner in first_runners:
        print(f"Runner: {runner.number} Name: {runner.last_name} Time: {runner.elapsed_time}")
        et = str(runner.elapsed_time)
        runner.elapsed_time = et
        print(f"Runner: {runner.number} Name: {runner.last_name} Time: {runner.elapsed_time}")

    context = {"teams": first_teams[:15],
                "runners": first_runners[:15]}

    return render(request, 'index.html', context)



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
    all_teams = Teams.objects.all()

    print("Set race called..........")

    if request.method == "POST":
        data = request.POST
        time_value = data.get("start")
        button_start = data.get("set_time")
        button_reset = data.get("reset")
        print(f"Time value is: {time_value}")
        print(f"Button start is: {button_start}")
        print(f"Button reset is: {button_reset}")

        if button_start == "on":
            for team in all_teams:
                print(f"Team Runner A number is: {team.runners_A.number}")
                print(f"Team Runner A start time is: {team.runners_A.start_time}")
                datetime_object = parser.parse(time_value)
                first_runner = Runner.objects.get(number=team.runners_A.number)
                first_runner.start_time = datetime_object
                team.runners_A.start_time = datetime_object
                print(f"Team Runner A start time is now: {first_runner.start_time}")
                first_runner.save()

        if button_reset == "on":
            for team in all_teams:
                print(f"Team Runner A number is: {team.runners_A.number}")
                first_runner = Runner.objects.get(number=team.runners_A.number)
                first_runner.start_time = None
                first_runner.save()
                print("Start times reset ........")

    context = {"test": "test"}
    return render(request, 'set_race.html', context)


# Create your views here.


# def _set_team_elapsed_time(last_runner):
#
#     runner_number = last_runner.number
#     team_number = runner_number[1:]
#
#     team = Teams.objects.get(number=team_number)
#     print(f"Team name is: {team.name}")
#     print(f"Runner A elapsed time: {team.runners_A.elapsed_time} Type is: {type(team.runners_A.elapsed_time)}")
#     print(f"Runner B elapsed time: {team.runners_B.elapsed_time} Type is: {type(team.runners_B.elapsed_time)}")
#     print(f"Runner C elapsed time: {team.runners_C.elapsed_time} Type is: {type(team.runners_C.elapsed_time)}")
#     print(f"Runner D elapsed time: {team.runners_D.elapsed_time} Type is: {type(team.runners_D.elapsed_time)}")
#     print(f"Runner E elapsed time: {team.runners_E.elapsed_time} Type is: {type(team.runners_E.elapsed_time)}")
#     print(f"Runner F elapsed time: {team.runners_F.elapsed_time} Type is: {type(team.runners_F.elapsed_time)}")
#
#     accumulated_time = datetime.time("00:00:00")
#     elapsed_times_list = [team.runners_A.elapsed_time, team.runners_B.elapsed_time, team.runners_C.elapsed_time,
#                           team.runners_D.elapsed_time, team.runners_E.elapsed_time, team.runners_F.elapsed_time]
#     for counter, et in enumerate(elapsed_times_list):
#         if et is not None:
#             accumulated_time = accumulated_time + et
#             print(f"Loop: {counter} Accumulated time is: {accumulated_time}")
#
#
#     print(f"Team elapsed time is: {accumulated_time}")
#     team.elapsed_time = accumulated_time
#     team.save()


def find_runner(request, runner_id):

    # Ensure that all characters are upper case.
    runner_id = runner_id.upper()
    elapsed_time = ""

    if request.user.is_staff or request.user.is_superuser:

        #queryset_all_runners = Post.objects.all().order_by('-created')
        try:
            runner = Runner.objects.get(number=runner_id)
            message = f"Runner is: {runner.first_name} {runner.last_name}   " \
                      f"Number: {runner.number}  Age: {runner.age}  " \
                      f"Start time: {runner.start_time}  End time: {runner.end_time}"

            print(f"Message: {message}")

            if request.method == "POST":
                data = request.POST
                time_value = data.get("end")
                print(f"Time value is: {time_value}")
                datetime_object = parser.parse(time_value)
                runner.end_time = tz_lon.localize(datetime_object)

                #runner.end_time = datetime_object
                print(f"The end time type is: {type(runner.end_time)}")

                if runner.start_time is not None:
                    if runner.start_time <= runner.end_time:
                        elapsed_time = runner.end_time - runner.start_time
                        runner.elapsed_time = str(elapsed_time)
                        #_set_team_elapsed_time(runner)
                    else:
                        print(f"Error start time is after end time: {runner.end_time}")
                else:
                    print(f"No start time for runner")
                    elapsed_time = "No start time!"

                print(f"Runners elapsed time is: {runner.elapsed_time}")
                runner.save()

                #_set_runner_next_start(runner)

            if request.method == "GET":
                elapsed_time = runner.elapsed_time
                print(f"Elapsed time in get is: {elapsed_time}")


            context = {"number": runner.number,
                       "name": f"{runner.first_name}   {runner.last_name}",
                       "gender": runner.gender,
                       "age": runner.age,
                       "start_time": runner.start_time,
                       "end_time": runner.end_time,
                       "elapsed_time": elapsed_time}


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

