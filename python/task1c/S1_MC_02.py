def run_command(cmd):
    match cmd:
        case "start":
            return "Starting..."
        case "stop":
            return "Stopping..."
        case "status":
            return "Running"
        case _:
            return "UNKNOWN_COMMAND"

print(run_command("start"))
print(run_command("stop"))
print(run_command("status"))
print(run_command("help"))
