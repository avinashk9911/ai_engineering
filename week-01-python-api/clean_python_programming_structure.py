import sys

import requests


def get_github_user(username: str) -> int:
    """Fetch and display public information for a GitHub user."""
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        user_data = response.json()

        print(f"Username: {user_data['login']}")
        print(f"Public repositories: {user_data['public_repos']}")
        print(f"Profile: {user_data['html_url']}")
        return 0

    except requests.exceptions.Timeout:
        print("Error: The request took too long. Please try again.")
        return 1

    except requests.exceptions.HTTPError as error:
        print(f"Error: GitHub returned an error: {error}")
        return 1

    except requests.exceptions.RequestException as error:
        print(f"Error: Unable to connect to GitHub: {error}")
        return 1


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