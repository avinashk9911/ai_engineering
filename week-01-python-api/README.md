# GitHub API Client

A Python command-line program that requests public GitHub profile information.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```powershell
pip install -r requirements.txt



## Lesson 7: Environment-Based Configuration and API Key Safety

### What this lesson is about

This lesson introduces environment-based configuration: keeping application settings and secrets outside Python source code.

We used a .env file to store local settings and updated the application to read configuration values safely.

### Why this matters for AI Engineering

AI applications often require sensitive values such as:

- API keys
- Database passwords
- Cloud tokens
- Model-provider credentials

These values must not be written directly in Python files or uploaded to GitHub. Environment-based configuration allows the same codebase to run safely on a local machine, test environment, and production server.

### Concepts learned

- .env file: private local configuration
- .env.example file: safe template showing required configuration
- .gitignore: prevents private files from being committed
- python-dotenv: loads values from .env
- os.getenv(): reads configuration values in Python
- Validation and fallback values: prevents invalid configuration from crashing the application

### Files added or updated

| File | Change |
|---|---|
| .env | Added private local configuration; not committed to Git |
| .env.example | Added safe configuration template; committed to Git |
| .gitignore | Ensures .env is ignored |
| requirements.txt | Added python-dotenv dependency |
| main.py | Loads and validates REQUEST_TIMEOUT_SECONDS |
| README.md | Documented local configuration setup |

### Configuration

Create a .env file locally:

```text
APP_MODE=development
REQUEST_TIMEOUT_SECONDS=10