#!/usr/bin/env python
import sys
import warnings
import asyncio
from datetime import datetime

from crewaiproject3.crew import Crewaiproject3
# import litellm

# litellm._turn_on_debug()

# ... your LiteLLM/CrewAI code here ...

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#     'interests': 'Data Science, Artificial Intelligence, Machine Learning',
#     'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
#     'experience_level': 'Entry-level',
#     'goals': 'Secure a Data Scientist position at a leading tech company'
#     }
    
#     try:
#         Crewaiproject3().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")
    # try:
    #     result = Crewaiproject3().crew().kickoff(inputs=inputs)
    #     # Access all task outputs
    #     outputs = []
    #     for task_output in result.tasks_output:
    #         outputs.append({
    #             'task': task_output.name,
    #             'output': task_output.raw
    #         })
    #     return outputs
    # except Exception as e:
    #     raise Exception(f"An error occurred while running the crew: {e}")
# def run():
#     """
#     Run the crew and retrieve outputs from all tasks.
#     """
#     inputs = {
#         'interests': 'Data Science, Artificial Intelligence, Machine Learning',
#         'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
#         'experience_level': 'Entry-level',
#         'goals': 'Secure a Data Scientist position at a leading tech company'
#     }

#     try:
       
#         # Collect all task outputs
#         result = Crewaiproject3().crew().kickoff(inputs=inputs)
#         return (result.tasks_output)

#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

# def run():
#     inputs = {
#         'interests': 'Data Science, Artificial Intelligence, Machine Learning',
#         'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
#         'experience_level': 'Entry-level',
#         'goals': 'Secure a Data Scientist position at a leading tech company'
#     }
    
#     try:
#         Crewaiproject3().crew().kickoff(inputs=inputs)
        
        
                
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")
def run():
    """
    Run the crew.
    """
    inputs = {
    'interests': 'Data Science, Artificial Intelligence, Machine Learning',
    'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
    'experience_level': 'Entry-level',
    'goals': 'Secure a Data Scientist position at a leading tech company'
    }
    
    try:
        Crewaiproject3().crew().kickoff(inputs=inputs))
        
        # Access different types of output
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
    'interests': 'Data Science, Artificial Intelligence, Machine Learning',
    'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
    'experience_level': 'Entry-level',
    'goals': 'Secure a Data Scientist position at a leading tech company'
    }
    try:
        Crewaiproject3().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Crewaiproject3().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
    'interests': 'Data Science, Artificial Intelligence, Machine Learning',
    'skills': 'Python, Statistics, Data Analysis, Communication, SQL',
    'experience_level': 'Entry-level',
    'goals': 'Secure a Data Scientist position at a leading tech company'
}
    try:
        Crewaiproject3().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
