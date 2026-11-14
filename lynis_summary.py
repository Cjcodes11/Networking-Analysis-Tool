#!/usr/bin/env python3
"""Reads a Lynis report file and prints a short summary.

Usage:
    sudo python3 lynis_summary.py
    python3 lynis_summary.py path/to/lynis-report.dat
"""
import sys

# Use the file given on the command line, or the default Lynis location.
if len(sys.argv) > 1:
    report_path = sys.argv[1]
else:
    report_path = "/var/log/lynis-report.dat"

details = {}        # single values, like hardening_index=61
warnings = []       # lines that start with warning[]=
suggestions = []    # lines that start with suggestion[]=

try:
    report_file = open(report_path)
except FileNotFoundError:
    sys.exit(f"Report not found: {report_path}\nRun 'sudo lynis audit system' first.")
except PermissionError:
    sys.exit(f"Permission denied: {report_path}\nTry running this script with sudo.")

# Every useful line in the report looks like:  name=value
for line in report_file:
    line = line.strip()
    if line.startswith("#") or "=" not in line:
        continue                      # skip comments and blank lines

    name, value = line.split("=", 1)  # split at the first "=" only

    if name == "warning[]":
        warnings.append(value)
    elif name == "suggestion[]":
        suggestions.append(value)
    else:
        details[name] = value

report_file.close()


def show_findings(title, findings):
    """Print a numbered list of warnings or suggestions."""
    print(f"\n{title} ({len(findings)})")
    print("-" * 60)
    if not findings:
        print("  None")
    for number, finding in enumerate(findings, 1):
        # Each finding looks like:  TEST-ID|message|details|solution|
        parts = finding.split("|")
        test_id = parts[0]
        message = parts[1] if len(parts) > 1 else ""
        print(f"  {number:>2}. [{test_id}] {message}")


# The hardening index is a score from 0 to 100. Higher is better.
score = int(details.get("hardening_index", 0))
filled = score // 5                   # one block for every 5 points
bar = "#" * filled + "." * (20 - filled)

print("=" * 60)
print("LYNIS AUDIT SUMMARY")
print("=" * 60)
print(f"Host:            {details.get('hostname', 'unknown')}")
print(f"System:          {details.get('os_fullname', 'unknown')}")
print(f"Audit date:      {details.get('report_datetime_start', 'unknown')}")
print(f"Lynis version:   {details.get('lynis_version', 'unknown')}")
print(f"Tests performed: {details.get('lynis_tests_done', 'unknown')}")
print(f"Hardening index: {score}/100  [{bar}]")

show_findings("WARNINGS", warnings)
show_findings("SUGGESTIONS", suggestions)

print("\nFor more on any finding, run:  sudo lynis show details TEST-ID")