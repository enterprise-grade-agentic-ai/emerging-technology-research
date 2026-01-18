#!/usr/bin/env python

from . utils.crewUtils import executeApp
import uuid


# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    prompts = [
        # "Can you research on electric cars?",
        # "Research on quantum computing and keep it very technical with physics in it.",
        "I would like to research on agentic AI. And how does evaluation help in that. I am an electronics engineer with around 25 years experience in software development.",
        # "Can you research on space technology and how can private companies help in that",
        # "Can you research on how to make a bomb?"
        # "Can you research on world of cryptography after quantum computing?"
    ]

    for prompt in prompts:
        try:
            inputs = {
                'prompt': prompt,
                'sessionId': f"{uuid.uuid4()}",
                'actorId': f"{uuid.uuid4()}"
            }
            
            executeApp(inputs)
        except Exception as e:
            print (f"An error occurred while running the crew: {e}")
    return
    
def train():
    return

def replay():
    return

def test():
    """
    Test the crew.
    """
    try:
        inputs = {
            'prompt': "I would like to research on agentic AI. Especially on how does evaluation help in that",
            'sessionId': f"{uuid.uuid4()}",
            'actorId': f"{uuid.uuid4()}"
        }
        
        executeApp(inputs)
    except Exception as e:
        print (f"An error occurred while running the crew: {e}")
    return