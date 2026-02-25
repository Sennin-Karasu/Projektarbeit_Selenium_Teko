import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://the-internet.herokuapp.com/"


def show_help():
    print("Verwendung:")
    print("  python myproject.py title")
    print("  python myproject.py get")
    print("  python myproject.py post")
    print("  python myproject.py list-cookies")


def create_driver():
    options = Options()
    # Später optional aktivieren, wenn ihr ohne Browserfenster wollt:
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver


def cmd_title():
    driver = create_driver()
    try:
        driver.get(BASE_URL)
        print("Titel:", driver.title)
    finally:
        driver.quit()


def cmd_get():
    driver = create_driver()
    try:
        url = BASE_URL + "?name=max&kurs=http"
        driver.get(url)

        print("GET geladen")
        print("Aktuelle URL:", driver.current_url)
        print("Titel:", driver.title)
    finally:
        driver.quit()


from selenium.webdriver.common.by import By

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

        # Optional: Erfolgsmeldung anzeigen
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
        return

    command = sys.argv[1]

    if command == "title":
        cmd_title()
    elif command == "get":
        cmd_get()
    elif command == "post":
        cmd_post()
    elif command == "list-cookies":
        cmd_list_cookies()
    else:
        print(f"Unbekannter Befehl: {command}")
        show_help()


if __name__ == "__main__":
    main()