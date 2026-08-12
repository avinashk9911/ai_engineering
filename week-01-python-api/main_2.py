import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

def get_request_timeout() -> int:
    """Read and validate the API request timeout from configureation"""
    raw_timeout = os.getenv("REQUEST_TIMEOUT_SECONDS", "10")

    try:
        timeout = int(raw_timeout)
    except ValueError:
        print("Warning: Invalid REQUEST_TIMEOUT_SECONDS. Using 10 Seconds")
        return 10

    if timeout <= 0:
        print("Warnings: Timeout must be grater than zero. Using 10 Seconds")
        return 10

    return timeout

def get_github_user(username: str) -> None: 
    url = f"https://api.github.com/users/{username}"

    try:
        #response = requests.get(url, timeout=10) 
        response = requests.get(url, timeout=get_request_timeout())
        response.raise_for_status() 

        user_data = response.json() 

        print(f"Username: {user_data['login']}")
        print(f"Public repositories: {user_data['public_repos']}")
        print(f"Profile: {user_data['html_url']}")

    except requests.exceptions.Timeout: 
        print("Error: The request took too long. Please try again.")

    except requests.exceptions.HTTPError as error: 
        print(f"Error: GitHub returned an error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Error: Unable to connect to GitHub: {error}")


def main() -> int:
    """Validate command-line input and run the program."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <github_username>")
        return 1

    username = sys.argv[1].strip()

    if not username:
        print("Error: GitHub username cannot be empty.")
        return 1

    return get_github_user(username)


if __name__ == "__main__":
    raise SystemExit(main())