import os
import webbrowser
# Small console application that calls
# the built-in battery diagnostic
# tool of windows, and opens the diagnostic
# log file automatically.
def batteryReport():
    # CLI command
    os.system('powercfg /batteryreport')
    # Log file is always saved as
    # an html file. opening the log file
    # on default web browser.
    webbrowser.open("battery-report.html")
    return 0

if __name__ == "__main__":
    batteryReport()