from os import close

import github_activity
from github_activity import GitHubActivity


def print_banner():
    banner = r"""
░██████╗░██╗████████╗██╗░░██╗██╗░░░██╗██████╗░
██╔════╝░██║╚══██╔══╝██║░░██║██║░░░██║██╔══██╗
██║░░██╗░██║░░░██║░░░███████║██║░░░██║██████╦╝
██║░░╚██╗██║░░░██║░░░██╔══██║██║░░░██║██╔══██╗
╚██████╔╝██║░░░██║░░░██║░░██║╚██████╔╝██████╦╝
░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═════╝░

░█████╗░░█████╗░████████╗██╗██╗░░░██╗██╗████████╗██╗░░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██║██║░░░██║██║╚══██╔══╝╚██╗░██╔╝
███████║██║░░╚═╝░░░██║░░░██║╚██╗░██╔╝██║░░░██║░░░░╚████╔╝░
██╔══██║██║░░██╗░░░██║░░░██║░╚████╔╝░██║░░░██║░░░░░╚██╔╝░░
██║░░██║╚█████╔╝░░░██║░░░██║░░╚██╔╝░░██║░░░██║░░░░░░██║░░░
╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░
    """
    print(banner)
    print("Welcome to GitHubActivity 🚀\n")

def input_name():
    while True:
        input_name = input("Enter the GitHub username: ")
        github_acc = GitHubActivity(input_name)
        github_events = github_acc.get_user_events()
        github_acc.parse_data(github_events)
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() == "y":
            pass
        else:
            print("Thanks for using my script! See you next time!")
            break

def main():
    print_banner()
    input_name()

if __name__ == "__main__":
    main()