# Python-tk
Toolkit for my computer made with python(first version)
It is a system health checker which checks the CPU, memory and disk usage, along with displaying the uptime of the computer
It shows warning at 70% usage and critical at 90%

## Requirements:
Python 3.9 
psutil(install it from requirements.txt)

## Setup
Clone the repository:
1.  git clone https://github.com/gursimarchahal25/Python-tk
   cd Python-tk

2. Create and activate a virtual environment:
   
   python3 -m venv virtenv
   source virtenv/bin/activate   # only for mac

3. Install the requirements:
   
   pip install -r requirements.txt

## How to use it
Go in the terminal
python3 system_health_check.py

## How it works
1. psutil` reads CPU, memory, and uptime information from the operating system.
2. shutil.disk_usage` reads disk usage for the main drive.    #'/' on macOS
3. A `get_status` function compares each value against its warning and critical thresholds.
4. If a check fails, the tool prints an error message instead of crashing.

## Output
=== System Health Report ===
CPU              19.9%   OK
Memory           61.0%   OK
Disk (/)         47.2%   OK
Uptime          1d 23h 6m
