#!/usr/bin/env python3
"""
Notification script for Jenkins pipeline.
This script handles notifications based on pipeline results.
"""

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: notify.py <success|failure>")
        return 1
    
    status = sys.argv[1]
    
    if status == "success":
        print("Sending success notification...")
        print("Email: Pipeline completed successfully!")
        print("Slack: :white_check_mark: Pipeline succeeded")
        print("Notification sent!")
        return 0
    elif status == "failure":
        print("Sending failure notification...")
        print("Email: Pipeline failed! Check Jenkins for details.")
        print("Slack: :x: Pipeline failed")
        print("Notification sent!")
        return 1
    else:
        print(f"Unknown status: {status}")
        return 1


if __name__ == "__main__":
    sys.exit(main())