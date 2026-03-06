import subprocess
import src.fix

flake = subprocess.run(
    ["flake8", "."],
    capture_output=True,
    text=True
)

for linha in flake.stdout.splitlines():
    if linha.strip():
        fixfix8(linha) 

