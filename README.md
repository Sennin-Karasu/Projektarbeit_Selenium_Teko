# Projektarbeit_Selenium_Teko

## Beschreibung

Demonstration von HTTP-Konzepten mit Selenium als Browser-Werkzeug. Weitere Features sind in [docs/features.md](docs/features.md) dokumentiert.

- Webseite laden und Titel anzeigen (Scraping)
- GET Request mit Variablen
- POST Request (Form Submission)
- Cookies anzeigen

## Voraussetzung

- (pip install -r requirements.txt)
- Python mind. 3.11

## Beispielbefehle

```bash
python selenium_tester.py          # Alle Befehle anzeigen
python selenium_tester.py title
python selenium_tester.py get name=max
python selenium_tester.py list-cookies
python selenium_tester.py keypress Hallo
```
