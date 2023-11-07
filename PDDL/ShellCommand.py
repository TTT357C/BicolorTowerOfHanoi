import subprocess

"""
ShellCommand class to run shell commands.
The class provides a run method to execute shell commands and return the output.

Methods:
    run: Executes a shell command and returns the output

Args:
    command: The shell command to execute
"""

class ShellCommand:

    def run(self, command):
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
        return result.stdout.decode('ISO-8859-1')

