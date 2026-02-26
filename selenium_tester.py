# Standard library: exit codes and command-line arguments
import sys

# Standard library: check if a package is installed without importing it
import importlib.util

# Standard library: run shell commands (used for pip install)
import subprocess

# Standard library: pause execution for a given number of seconds
import time


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

# Selenium: simulate keyboard and mouse actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Selenium: error that occurs when a page cannot be loaded
from selenium.common.exceptions import WebDriverException

# Default URL used when no URL is given by the user
BASE_URL = "https://the-internet.herokuapp.com/"


def show_help():
    # Print all available commands with descriptions and examples
    print("Verwendung: python selenium_tester.py <befehl> [optionen]")
    print()
    print("Befehle:")
    print("  title [url]      Lädt eine Webseite und zeigt den Titel an")
    print("  get [key=value]  Sendet einen GET-Request, optional mit Parametern")
    print("  post [url]       Füllt das Login-Formular aus und sendet es ab")
    print("  list-cookies [url]  Zeigt alle Cookies der Seite an")
    print("  checkbox [url]   Zeigt an, welche Checkboxen auf der Seite ausgewählt sind")
    print("  keypress [text] [url]  Sucht ein Texteingabefeld und tippt den Text ein (Standard: 'Hallo Welt')")
    print("  slider [url]     Bewegt den Slider auf den Maximalwert und gibt ihn aus")
    print()
    print("Beispiele:")
    print("  python selenium_tester.py title")
    print("  python selenium_tester.py title https://example.com")
    print("  python selenium_tester.py get")
    print(f"  python selenium_tester.py get name=max   ->  {BASE_URL}?name=max")
    print("  python selenium_tester.py post")
    print("  python selenium_tester.py list-cookies")
    print("  python selenium_tester.py checkbox")
    print("  python selenium_tester.py keypress Hallo")
    print("  python selenium_tester.py keypress Hallo https://example.com")
    print("  python selenium_tester.py slider")
    print()
    print("Exit-Codes:")
    print("  0  Erfolg")
    print("  1  Website konnte nicht geladen werden")
    print("  2  Unbekannter Befehl oder fehlende Argumente")


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

    except WebDriverException as error:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        print("Details:", str(error).split("\n")[0])
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


def cmd_post(url=None):
    # Use the login page if no URL is given
    if url is None:
        url = BASE_URL + "login"

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

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
        flash_message = driver.find_element(By.ID, "flash").text
        print("Antwort:", flash_message.strip())

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_list_cookies(url=None):
    # Use the default base page if no URL is given
    if url is None:
        url = BASE_URL

    # Open the browser
    driver = create_driver()
    try:
        # Load the page so cookies are set
        driver.get(url)

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


def cmd_checkbox(url=None):
    # Use the checkboxes demo page if no URL is given
    if url is None:
        url = BASE_URL + "checkboxes"

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

        # Find all checkbox input elements on the page
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        # Exit if no checkboxes were found on the page
        if not checkboxes:
            print("Keine Checkboxen auf der Seite gefunden.")
            return

        # Find all checkboxes that are currently checked
        checked = [cb for cb in checkboxes if cb.is_selected()]

        # Print how many checkboxes exist and how many are checked
        print(f"Checkboxen gefunden: {len(checkboxes)}")
        print(f"Ausgewählt: {len(checked)}")

        # Print the index of each checked checkbox (1-based for readability)
        for cb in checked:
            index = checkboxes.index(cb) + 1
            print(f"  Checkbox {index}: ausgewählt")

    except WebDriverException as error:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        print("Details:", str(error).split("\n")[0])
        sys.exit(1)

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_keypress(text=None, url=None):
    # Use default text if none was provided
    if text is None:
        text = "Hallo Welt"

    # Use the key presses demo page if no URL is given
    if url is None:
        url = BASE_URL + "key_presses"

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

        # Search for a text or search input field on the page (covers type='text' and type='search')
        input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='search']")

        # Exit if no input field was found on the page
        if not input_fields:
            print("FEHLER: Kein Texteingabefeld auf der Seite gefunden.")
            sys.exit(1)

        # Type the given text into the first input field found
        input_fields[0].send_keys(text)
        print("Text eingegeben:", text)

        # Wait so the user can see the result in the browser before it closes
        time.sleep(10)

    except WebDriverException as error:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        print("Details:", str(error).split("\n")[0])
        sys.exit(1)

    finally:
        # Always close the browser, even if an error occurred
        driver.quit()


def cmd_slider(url=None):
    # Use the horizontal slider demo page if no URL is given
    if url is None:
        url = BASE_URL + "horizontal_slider"

    # Open the browser
    driver = create_driver()
    try:
        # Load the page
        driver.get(url)

        # Find the range input (the slider element)
        slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")

        # Click to focus the slider, then press End to jump to the maximum value
        ActionChains(driver).click(slider).send_keys(Keys.END).perform()

        # Read the current value displayed next to the slider
        value = driver.find_element(By.ID, "range").text
        print("Slider auf Maximum gesetzt")
        print("Wert:", value)

        # Wait so the user can see the result in the browser before it closes
        time.sleep(10)

    except WebDriverException as error:
        # Page could not be loaded — print error and exit with code 1
        print(f"FEHLER: Website konnte nicht geladen werden: {url}")
        print("Details:", str(error).split("\n")[0])
        sys.exit(1)

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
        # Use the second argument as URL if provided, otherwise use None (default URL)
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_post(url)

    elif command == "list-cookies":
        # Use the second argument as URL if provided, otherwise use None (default URL)
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_list_cookies(url)

    elif command == "checkbox":
        # Use the second argument as URL if provided, otherwise use None (default URL)
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_checkbox(url)

    elif command == "keypress":
        # Use second argument as text if provided, otherwise use default
        text = sys.argv[2] if len(sys.argv) >= 3 else None
        # Use optional third argument as URL
        url = sys.argv[3] if len(sys.argv) >= 4 else None
        cmd_keypress(text, url)

    elif command == "slider":
        # Use the second argument as URL if provided, otherwise use None (default URL)
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_slider(url)

    else:
        # Unknown command — show error, help, and exit with code 2
        print(f"FEHLER: Unbekannter Befehl '{command}'")
        show_help()
        sys.exit(2)


# Entry point: only run main() when this file is executed directly
if __name__ == "__main__":
    main()
