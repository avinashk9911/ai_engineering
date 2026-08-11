# import sys
# import requests


# def get_github_user(username: str) -> None: # This function takes a GitHub username as an argument and prints the user's login, public repositories, and profile URL.
#     url = f"https://api.github.com/users/{username}"

#     try:
#         response = requests.get(url, timeout=10) #requests.get(...) sends a request to GitHub. # timeout=10 prevents the program from waiting forever.
#         response.raise_for_status() # response.raise_for_status() turns failed responses, such as 404 Not Found, into a manageable error.

#         user_data = response.json() # response.json() converts the JSON data into a Python dictionary.

#         print(f"Username: {user_data['login']}")
#         print(f"Public repositories: {user_data['public_repos']}")
#         print(f"Profile: {user_data['html_url']}")

#     except requests.exceptions.Timeout: # requests.exceptions.Timeout is raised when the request takes too long.
#         print("Error: The request took too long. Please try again.")

#     except requests.exceptions.HTTPError as error: # requests.exceptions.HTTPError is raised when the request returns an HTTP error.
#         print(f"Error: GitHub returned an error: {error}")

#     except requests.exceptions.RequestException as error:
#         print(f"Error: Unable to connect to GitHub: {error}")


# #get_github_user("avinashk9911")
# #get_github_user("This user does not exist 9900011")

# if len(sys.argv) != 2: # len(sys.argv) returns the number of command-line arguments passed to the script.
#     print("Usage: python main.py <github_username>") # If the number of arguments is not 2, print the usage message.
# else:
#     get_github_user(sys.argv[1]) # If the number of arguments is 2, get the GitHub username from the command-line argument and call the get_github_user function.


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


if _name_ == "_main_":
    raise SystemExit(main())