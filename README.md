# Python-toolkit

-Toolkit for my computer made with python(first version)
It is a system health checker which checks the CPU, memory and disk usage, along with displaying the uptime of the computer.
It shows warning and critical status when usage reaches its threshold.

## Requirements:

-Python 3.9 
-psutil(install it from requirements.txt)

## Setup
1. Clone the repository:

   -git clone https://github.com/gursimarchahal25/Python-tk
   -cd Python-tk

2. Create and activate a virtual environment:
   
   -python3 -m venv virtenv
   -source virtenv/bin/activate (only for mac)

3. Install the requirements:
   
   pip install -r requirements.txt

## How to use it

-Go in the terminal and write the command:
-python3 system_health_check.py

## How it works
1. psutil` reads CPU, memory, and uptime information from the operating system.
2. shutil.disk_usage` reads disk usage for the main drive.    ('/' on macOS)
3. It gives a warning and critical alert when the value reaches its threshold.
3. A `get_status` function compares each value against its warning and critical thresholds.
4. The battery function works in a reverse logic as it shows warning and critical status when the value is low. 
5. If a check fails, the tool prints an error message instead of crashing.

## Output

```
=== System Health Report ===
CPU              24.5%   OK
Memory           67.4%   OK
Disk (/)         49.5%   OK
Uptime          3d 2h 33m
Battery            58%   OK (On battery)
```
## Limitations

- It cannot display the programs with most CPU and memory usage.
- It cannot properly estimate the time left on battery.

## Author

Gursimar Singh Chahal