# perfect-lurker
This repository creates a bot in python that connects to twitch's event to register when a lurker clocks in and clocks out


# Steps to reproduce:

```
# Create a virtual environment
python -m venv venv
# Activate the environment
source venv/bin/activate
# Install requirements.txt into the environment
pip install -r requirements.txt
# Run main.py
python main.py

```


# Note:
The link with the scopes for these example might look something like this:
```
<a href="https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=<CALLBACK>k&scope=chat%3Aedit+moderator%3Aread%3Afollowers+channel%3Amanage%3Aredemptions+moderator%3Aread%3Ashoutouts"> Click here</a>
```
