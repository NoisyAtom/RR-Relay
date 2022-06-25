# RR-Relay
Web portal to track and display a running relay event. Written using Django and using IoT devices for tracking.

## Descripton
This is a Django web project using python 3.9 and Django 4.0. It is intended to be used to display information on teams and runners during a runners realy event. The system requires the following input:
1. Teams each team has 6 members
2. Team names
3. Runners names
4. Runners birthdays
5. Runners gender
6. Runners fastest 5km time from recent year
7. Logic to ensure that the mixed teams are conform with the requirements of the orginisers
- At least one male runner
- At least one female runner
- No more than 3 senior male runners (aged 18-39)
- remainder will be ladies and veteran male runners
**Those teams will be picked randomly, if you are a RR club member**
8. Running order inside the team
9. Event details.
- Date
- Start
- End
- Location
10. Administrators.
11. Route details, duration.

The portal at it's most basic displays information on a team during an event. It is intended to be run on a remote server at the event. It allows administrators at the event to update, team, runner and time information with no internet connectivity.

To find instructions on installing, setup and running the system please go to the **/documents** folder.
