CFP
----
Live demo - https://djangocfp.herokuapp.com/

# Features
- Dashboards for Speakers and Event organizers to organize and sort their proposals and events as per their needs.
- Public user profiles
- Saving proposals as Draft
- Bulk submit Draft proposals
- Organizers can search for speakers.
- Leaderboard
- Send event invites and details in mail(Data is sent in ICS format).

# Setup

```
$git clone https://github.com/tapaswenipathak/CFP.git
$cd CFP
$pip install -r requirements.txt

#open users/apps.py file and comment ready() method

$python manage.py makemigrations
$python manage.py migrate

#Then uncomment the lines from apps.py file

$python manage.py runserver
```


