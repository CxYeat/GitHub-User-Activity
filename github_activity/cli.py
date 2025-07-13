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
    print("Welcome to GitHubActivity \n")

def input_name():
    while True:
        username = input("Enter the GitHub username: ")
        github_acc = GitHubActivity(username)
        try:
            github_events = github_acc.get_user_events()
            github_acc.parse_events(github_events)
        except Exception as e:
            print(f" Error: {e}")
            retry = input("Try another username? (y/n): ")
            if retry.lower() == "y":
                continue
            else:
                print("Bye!")
                break
        else:
            cont = input("Do you want to check another user? (y/n): ")
            if cont.lower() == "y":
                continue
            else:
                print("Thanks for using GitHubActivity!")
                break

def main():
    print_banner()
    input_name()

if __name__ == "__main__":
    main()