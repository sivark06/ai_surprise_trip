#!/usr/bin/env python
import sys
from surprise_travel.crew import SurpriseTravelCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'origin': 'Kochi, KOC',
        'destination': 'CO, KPM',
        'age': 26,
        'hotel_location': 'Tirunagar',
        'flight_information': 'INDIGO 1234, leaving at JULY 30th, 2024, 10:00',
        'trip_duration': '10 days'
    }
    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    print(result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'origin': 'Kochi, KOC',
        'destination': 'Kondampatti, KPM',
        'age': 26,
        'hotel_location': 'RIGHT GRAND CITY',
        'flight_information': 'INDIGO 1234, leaving at JULY 30th, 2024, 10:00',
        'trip_duration': '10 days'
    }
    try:
        SurpriseTravelCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")