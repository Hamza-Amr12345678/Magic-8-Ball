import random

responses=[
    "Yes, definitly!"
    "No, not now."
    "Ask again later"
    "It is certain"
    "very doubtful"
    "Outlook is good"
    "Better not tell you now"
    "concentrate and ask again"
]

def get_random_response():
    return random.choice(responses)