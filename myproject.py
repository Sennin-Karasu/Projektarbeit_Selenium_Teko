import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

BASE_URL = "https://the-internet.herokuapp.com/"


def show_help():
    print("Verwendung:")
    print("  python myproject.py title [url]")
    print("  python myproject.py get")
    print("  python myproject.py post")
    print("  python myproject.py list-cookies")


def create_driver():
    options = Options()
    # Optional:
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver


def cmd_title(url=None):
    if url is None:
        url = BASE_URL

    driver = create_driver()
    try:
        try:
            driver.get(url)
        except WebDriverException as e:
            print(f"FEHLER: Website konnte nicht geladen werden: {url}")
            print("Details:", str(e).split("\n")[0])
            sys.exit(1)

        print("URL:", url)
        print("Titel:", driver.title)

    finally:
        driver.quit()

def cmd_get(params=None):
    driver = create_driver()
    try:
        if params:
            url = BASE_URL + "?" + params
        else:
            url = BASE_URL

        try:
            driver.get(url)
        except Exception as e:
            print(f"FEHLER: Website konnte nicht geladen werden: {url}")
            sys.exit(1)

        print("GET geladen")
        print("URL:", driver.current_url)
        print("Titel:", driver.title)

    finally:
        driver.quit()


def cmd_post():
    driver = create_driver()
    try:
        driver.get(BASE_URL + "login")

        # Formularfelder ausfüllen
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Formular absenden (POST)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        print("POST/Formular abgesendet")
        print("Aktuelle URL:", driver.current_url)
        print("Titel:", driver.title)

        # Erfolgsmeldung anzeigen
        flash = driver.find_element(By.ID, "flash").text
        print("Antwort:", flash.strip())

    finally:
        driver.quit()


def cmd_list_cookies():
    driver = create_driver()
    try:
        driver.get(BASE_URL)
        cookies = driver.get_cookies()

        if not cookies:
            print("Keine Cookies gefunden.")
            return

        print("Cookies:")
        for c in cookies:
            name = c.get("name", "")
            value = c.get("value", "")
            domain = c.get("domain", "")
            path = c.get("path", "")
            print(f"- {name}={value} (domain={domain}, path={path})")
    finally:
        driver.quit()


def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(2)

    command = sys.argv[1]

    if command == "title":
        url = sys.argv[2] if len(sys.argv) >= 3 else None
        cmd_title(url)


    elif command == "get":

        params = sys.argv[2] if len(sys.argv) >= 3 else None

        cmd_get(params)

    elif command == "post":
        cmd_post()

    elif command == "list-cookies":
        cmd_list_cookies()

    else:
        print(f"FEHLER: Unbekannter Befehl '{command}'")
        show_help()
        sys.exit(2)

if __name__ == "__main__":
    main()