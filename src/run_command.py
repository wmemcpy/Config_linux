from subprocess import run, PIPE, CalledProcessError
from datetime import datetime


def run_command(command: str, log: bool = False, log_file: str = "log.log"):
    timestamp = datetime.now().strftime('[%H:%M:%S]: ')

    log_message = f"{timestamp} {command}\n"

    if log_file:
        with open(log_file, 'a') as file:
            file.write(log_message)

    try:
        result = run(command, shell=log, check=True, stdout=PIPE, stderr=PIPE, text=True)
        return result.stdout
    except CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
        return None
