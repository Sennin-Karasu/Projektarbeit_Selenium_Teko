# Standard library: exit codes and command-line arguments
import sys

# Standard library: check if a package is installed without importing it
import importlib.util

# Standard library: run shell commands (used for pip install)
import subprocess


def check_selenium():
    # Check if selenium is already installed
    if importlib.util.find_spec("selenium") is not None:
        return  # Already installed — nothing to do

    # Selenium not found — ask the user whether to install it now
    print("Selenium ist nicht installiert.")
    answer = input("Möchten Sie Selenium jetzt installieren? (j/n): ").strip().lower()

    if answer != "j":
        # User declined — cannot continue without Selenium
        print("Selenium wird benötigt. Programm wird beendet.")
        sys.exit(1)

    # Install selenium using the same Python that is running this script
    # sys.executable ensures the correct interpreter is used on all operating systems
    print("Installiere Selenium...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "selenium"])

    if result.returncode != 0:
        # Installation failed — show manual fallback instruction
        print("Installation fehlgeschlagen. Bitte manuell ausführen: pip install selenium")
        sys.exit(1)

    # Installation successful — script must be restarted so the import works
    print("Selenium wurde installiert. Bitte das Programm neu starten.")
    sys.exit(0)


# Run the check before importing Selenium — otherwise Python crashes on the import below
check_selenium()


# Selenium: browser automation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Selenium: find elements on the page by ID, CSS, etc.
from selenium.webdriver.common.by import By

# Selenium: error that occurs when a page cannot be loaded
from selenium.common.exceptions import WebDriverException

# Default URL used when no URL is given by the user
BASE_URL = "https://the-internet.herokuapp.com/"


def show_help():
    # Print all available commands to the console
    print("Verwendung:")
    print("  python myproject.py title [url]")
    print("  python myproject.py get")
    print("  python myproject.py post")
    print("  python myproject.py list-cookies")


def create_driver():
    # Create Chrome browser options
    options = Options()
    # Optional: run browser without a visible window
    # options.add_argument("--headless=new")

    # Start Chrome with the given options and return the driver
    driver = webdriver.Chrome(options=options)
    return driver


def cmd_title(url=None):
    # Use the default URL if the user did not provide one
    if url is None:
        url = BASE_URL

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

        # Print the URL and page title
        print("URL:", url)
        print("Titel:", driver.title)

    except WebDriverException as e:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        print("Details:", str(e).split("\n")[0])
        sys.exit(1)

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_get(params=None):
    # Build the URL: append query parameters if provided, otherwise use base URL
    if params:
        url = BASE_URL + "?" + params
    else:
        url = BASE_URL

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

        # Print the final URL (may differ due to redirects) and page title
        print("GET geladen")
        print("URL:", driver.current_url)
        print("Titel:", driver.title)

    except WebDriverException:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        sys.exit(1)

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_post():
    # Open the browser
    driver = create_driver()
    try:
        # Navigate to the login page
        driver.get(BASE_URL + "login")

        # Fill in the username and password fields
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Click the submit button to send the form (POST request)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Print the result URL and page title after login
        print("POST/Formular abgesendet")
        print("Aktuelle URL:", driver.current_url)
        print("Titel:", driver.title)

        # Read and print the flash message shown after login
        flash = driver.find_element(By.ID, "flash").text
        print("Antwort:", flash.strip())

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_list_cookies():
    # Open the browser
    driver = create_driver()
    try:
        # Load the page so cookies are set
        driver.get(BASE_URL)

        # Get all cookies from the browser for this page
        cookies = driver.get_cookies()

        # If no cookies were found, say so and stop
        if not cookies:
            print("Keine Cookies gefunden.")
            return

        # Print each cookie with its name, value, domain and path
        print("Cookies:")
        for cookie in cookies:
            name   = cookie.get("name", "")
            value  = cookie.get("value", "")
            domain = cookie.get("domain", "")
            path   = cookie.get("path", "")
            print(f"- {name}={value} (domain={domain}, path={path})")

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def main():
    # Show help if no command was given
    if len(sys.argv) < 2:
        show_help()
        sys.exit(2)

    # Read the command from the first argument
    command = sys.argv[1]

    if command == "title":
        # Use the second argument as URL if provided, otherwise use None (default URL)
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_title(url)

    elif command == "get":
        # Use the second argument as query parameters if provided
        params = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_get(params)

    elif command == "post":
        cmd_post()

    elif command == "list-cookies":
        cmd_list_cookies()

    else:
        # Unknown command — show error, help, and exit with code 2
        print(f"FEHLER: Unbekannter Befehl '{command}'")
        show_help()
        sys.exit(2)


# Entry point: only run main() when this file is executed directly
if __name__ == "__main__":
    main()
