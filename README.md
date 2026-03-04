# Projektarbeit_Selenium_Teko

## Beschreibung

Demonstration von HTTP-Konzepten mit Selenium als Browser-Werkzeug. Standardmäßig wird `https://the-internet.herokuapp.com/` als Zielseite verwendet — alle Befehle akzeptieren eine optionale URL als Parameter. Weitere Features sind in [docs/features.md](docs/features.md) dokumentiert.

**Grundfeatures:**

- Webseite laden und Titel anzeigen (Scraping)
- GET Request mit Variablen
- POST Request (Form Submission)
- Cookies anzeigen

## Voraussetzung

- (pip install -r requirements.txt)
- Python mind. 3.11

## Beispielbefehle

```bash
python selenium_tester.py                        # Alle Befehle anzeigen
python selenium_tester.py title                  # Titel der Standardseite anzeigen
python selenium_tester.py title https://example.com  # Titel einer eigenen URL anzeigen
python selenium_tester.py get                    # GET-Request an die Standardseite
python selenium_tester.py get name=max           # GET-Request mit Query-Parameter
python selenium_tester.py post                   # Login-Formular ausfüllen und absenden
python selenium_tester.py list-cookies           # Cookies der Standardseite anzeigen
python selenium_tester.py keypress Hallo         # Text in ein Eingabefeld tippen
python selenium_tester.py checkbox               # Checkboxen der Standardseite auslesen
python selenium_tester.py slider                 # Slider auf Maximum bewegen und Wert ausgeben
```
