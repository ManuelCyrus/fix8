import subprocess
import fix

flake = subprocess.run(
    ["flake8", "."],
    capture_output=True,
    text=True
)


fix.fix8(flake.stdout)
