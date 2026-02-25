# Feature-Dokumentation

## Minimalsystem (Pflicht)

Diese Features gehören zum Minimalsystem und wurden implementiert:

- `title` (Selenium: Webseite laden und Titel anzeigen)
- `get` (GET mit Variablen)
- `post` (POST / Formular absenden)
- `list-cookies` (Cookies anzeigen)
- minimale Dokumentation > Readme.md

## Zusatzfeatures (für zusätzliche Punkte)

| Feature | Implementiert | Datei | Zeilennummern | Kurzbeschreibung |
| --- | --- | --- | --- | --- |
| Optionale URL als Parameter für `title` | Ja | selenium_tester.py | 99-102, 267 | `title` verwendet Standard-URL oder eine per CLI übergebene URL (`python selenium_tester.py title https://example.com`) |
| Client-Fehlerbehandlung bei ungültigem Command | Ja | selenium_tester.py | 288-292 | Ungültige Befehle werden abgefangen, Help angezeigt und Exit-Code 2 zurückgegeben |
| Fehlerbehandlung bei ungültiger Website | Ja | selenium_tester.py | 114-118, 143-146 | Website-Ladefehler werden abgefangen, Fehlermeldung ausgegeben und Exit-Code 1 gesetzt |
| Dynamische GET-Parameter über Client | Ja | selenium_tester.py | 125-130, 272 | GET-Parameter können als CLI-Argument übergeben werden (`python selenium_tester.py get name=max`) |
| Texteingabe in Formularfeld (`keypresses`) | Ja | selenium_tester.py | 210-249 | Sucht erstes `input[type='text']` auf der Seite und tippt den per CLI übergebenen Text ein |

Hinweis: Ohne URL wird weiterhin die Standard-Testseite `https://the-internet.herokuapp.com/` verwendet.

## Verwendete Testseite

- <https://the-internet.herokuapp.com/>
