from datetime import datetime
from subprocess import run, PIPE, CalledProcessError


def run_command(command: str, log_file: str = "log.log"):
    timestamp = datetime.now().strftime('[%H:%M:%S]: ')

    log_message = f"{timestamp} {' '.join(command)}\n"

    if log_file:
        with open(log_file, 'a') as file:
            file.write(log_message)
        file.close()

    try:

        result = run(command, shell=True, stdout=PIPE, stderr=PIPE, check=True, encoding='utf-8')
        return result.stdout


    except CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
        return None
