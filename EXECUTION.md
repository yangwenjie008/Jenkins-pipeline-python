# Execution Instructions

## Project Overview

This project demonstrates a Jenkins Pipeline as Code solution with:
1. Groovy-based Jenkins job framework definition (Jenkinsfile)
2. Python-based implementation for specific functionality (scripts/)

## Directory Structure

```
.
├── Jenkinsfile              # Main pipeline definition in Groovy
├── README.md                # Project overview
├── EXECUTION.md             # This file
├── config.json              # Jenkins connection configuration
├── requirements.txt         # Python dependencies
├── main.py                  # Main entry point
├── jobs/                    # Job DSL templates
│   └── template.groovy      # Sample job DSL template
└── scripts/                 # Python implementation scripts
    ├── build.py             # Build process implementation
    ├── test.py              # Test process implementation
    ├── deploy.py            # Deployment process implementation
    └── notify.py            # Notification implementation
```

## Setup Instructions

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Update `config.json` with your Jenkins server details:
   ```json
   {
     "jenkins": {
       "url": "http://your-jenkins-server:8080",
       "username": "your-username",
       "password": "your-password"
     }
   }
   ```

## Running the Pipeline

### Method 1: Direct Execution

Run the Python scripts directly to test functionality:

```bash
# Make scripts executable
chmod +x scripts/*.py

# Run individual scripts
python scripts/build.py
python scripts/test.py
python scripts/deploy.py
python scripts/notify.py success
```

### Method 2: Jenkins Pipeline

1. Create a new Pipeline job in Jenkins
2. Configure it to use the Jenkinsfile from SCM
3. Point it to this repository
4. Run the job

### Method 3: Job DSL Template

Use the template in the `jobs/` directory to programmatically create Jenkins jobs:

1. Install the Job DSL plugin in Jenkins
2. Create a seed job that uses the template
3. Run the seed job to create the pipeline job

## Modes of Operation

The `main.py` script supports three modes:

1. **inline**: Pipeline definition embedded directly in job configuration
   ```bash
   python main.py --mode inline
   ```

2. **scm**: Jenkinsfile retrieved from Source Control Management (default)
   ```bash
   python main.py --mode scm
   ```

3. **template**: Generate Jenkinsfile from templates
   ```bash
   python main.py --mode template
   ```

## Customization

1. Modify the `Jenkinsfile` to adjust the pipeline stages
2. Update the Python scripts in `scripts/` to implement your specific functionality
3. Adjust the job DSL template in `jobs/template.groovy` for programmatic job creation