import requests

def joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        json_data = requests.get(url).json()

        setup = json_data.get("setup", "Could not fetch a joke.")
        punchline = json_data.get("punchline", "Sorry, no punchline available.")
        return setup, punchline
    except Exception as e:
        return "Sorry, I couldn't fetch a joke right now.", str(e)
