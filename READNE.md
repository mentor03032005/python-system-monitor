# Python System Health Monitor

## Project Description
A Python-based system health monitoring tool that checks important computer resources and generates a system health report.

## Features
- Checks total disk space.
- Displays used and free disk space.
- Calculates folder size.
- Finds the five largest files.
- Monitors CPU usage.
- Monitors RAM usage.
- Displays current system date and time.
- Saves system reports to `health_log.txt`.

## Technologies Used
- Python
- psutil
- os
- datetime

## Requirements
- Python 3 installed.
- psutil library installed.

## Installation

Install the required library:

```bash
pip install psutil
```

## How to Run

Open the project folder in your terminal and run:

```bash
python monitor.py
```

## Output
The program displays system health information in the terminal and saves the report in `health_log.txt`.

## Author
Osonu Afamefuna Jonathan