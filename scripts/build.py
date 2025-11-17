#!/usr/bin/env python3
"""
Build script for Jenkins pipeline.
This script contains the actual implementation of the build process.
"""

import sys
import os
import subprocess


def main():
    print("Starting build process...")
    
    # Example build steps
    try:
        # Create a build directory
        os.makedirs("build", exist_ok=True)
        print("Created build directory")
        
        # Simulate some build process
        with open("build/artifact.txt", "w") as f:
            f.write("This is a sample build artifact\n")
            f.write("Built at: $(date)\n")
            
        print("Build artifact created")
        print("Build completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Build failed with error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())