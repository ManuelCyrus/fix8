import subprocess
from fix import fix8

flake = subprocess.run(
    ["flake8", "src/test.py"],
    capture_output=True,
    text=True
)

print("Flake8 output:")
print(flake.stdout)

for linha in flake.stdout.splitlines():
    if linha.strip():
        print("Processing:", linha)
        fix8(linha)

