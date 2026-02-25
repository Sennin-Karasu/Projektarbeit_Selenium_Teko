import sys


def show_help():
    print("Verwendung:")
    print("  python myproject.py title")
    print("  python myproject.py get")
    print("  python myproject.py post")
    print("  python myproject.py list-cookies")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "title":
        print("TODO: title (Selenium Seite öffnen und Titel anzeigen)")

    elif command == "get":
        print("TODO: get (GET Request über Selenium/Browser-Kontext)")

    elif command == "post":
        print("TODO: post (Formular ausfüllen und absenden = POST)")

    elif command == "list-cookies":
        print("TODO: list-cookies (Browser-Cookies anzeigen)")

    else:
        print(f"Unbekannter Befehl: {command}")
        show_help()


if __name__ == "__main__":
    main()