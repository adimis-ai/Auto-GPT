# Generated by CodiumAI
import time

from autogpt.spinner import Spinner

"""
Code Analysis

Main functionalities:
The Spinner class provides a simple way to display a spinning animation while a process is running. It can be used to indicate that a process is ongoing and to provide visual feedback to the user. The class can be used as a context manager, which means that it can be used with the 'with' statement to automatically start and stop the spinner animation.

Methods:
- __init__(self, message: str = "Loading...", delay: float = 0.1) -> None: Initializes the Spinner class with a message to display and a delay between each spinner update.
- spin(self) -> None: Spins the spinner animation while the process is running.
- __enter__(self): Starts the spinner animation when used as a context manager.
- __exit__(self, exc_type, exc_value, exc_traceback) -> None: Stops the spinner animation when used as a context manager.
- update_message(self, new_message, delay=0.1): Updates the message displayed by the spinner animation.

Fields:
- spinner: An itertools.cycle object that contains the characters used for the spinner animation.
- delay: The delay between each spinner update.
- message: The message to display.
- running: A boolean value that indicates whether the spinner animation is running.
- spinner_thread: A threading.Thread object that runs the spin method in a separate thread.
"""

ALMOST_DONE_MESSAGE = "Almost done..."
PLEASE_WAIT = "Please wait..."


def test_spinner_initializes_with_default_values():
    """Tests that the spinner initializes with default values."""
    with Spinner() as spinner:
        assert spinner.message == "Loading..."
        assert spinner.delay == 0.1


def test_spinner_initializes_with_custom_values():
    """Tests that the spinner initializes with custom message and delay values."""
    with Spinner(message=PLEASE_WAIT, delay=0.2) as spinner:
        assert spinner.message == PLEASE_WAIT
        assert spinner.delay == 0.2


#
def test_spinner_stops_spinning():
    """Tests that the spinner starts spinning and stops spinning without errors."""
    with Spinner() as spinner:
        time.sleep(1)
    assert not spinner.running


def test_spinner_can_be_used_as_context_manager():
    """Tests that the spinner can be used as a context manager."""
    with Spinner() as spinner:
        assert spinner.running
    assert not spinner.running
