# Feature-Dokumentation

## Grundfeatures

| Feature | Zeilennummern | Kurzbeschreibung |
| --- | --- | --- |
| `title` | 101-124 | Webseite laden und Titel anzeigen |
| `get` | 127-152 | GET-Request mit optionalen Query-Parametern |
| `post` | 155-180 | Login-Formular ausfüllen und absenden |
| `list-cookies` | 183-209 | Alle Cookies der Standardseite anzeigen |
| Minimale Dokumentation | - | README.md |

## Zusatzfeatures

| Feature | Zeilennummern | Kurzbeschreibung |
| --- | --- | --- |
| Optionale URL als Parameter für `title` | 99-102, 267 | `title` verwendet Standard-URL oder eine per CLI übergebene URL (`python selenium_tester.py title https://example.com`) |
| Client-Fehlerbehandlung bei ungültigem Command | 288-292 | Ungültige Befehle werden abgefangen, Help angezeigt und Exit-Code 2 zurückgegeben |
| Fehlerbehandlung bei ungültiger Website | 114-118, 143-146 | Website-Ladefehler werden abgefangen, Fehlermeldung ausgegeben und Exit-Code 1 gesetzt |
| Dynamische GET-Parameter über Client | 125-130, 272 | GET-Parameter können als CLI-Argument übergeben werden (`python selenium_tester.py get name=max`) |
| Texteingabe in Formularfeld (`keypress`) | 252-291 | Sucht erstes `input[type='text']` oder `input[type='search']` auf der Seite und tippt den per CLI übergebenen Text ein |
| Checkboxen auslesen (`checkbox`) | 210-249 | Findet alle `input[type='checkbox']` auf der Seite und gibt aus, welche ausgewählt sind; optionale URL als Argument |

Hinweis: Ohne URL wird weiterhin die Standard-Testseite `https://the-internet.herokuapp.com/` verwendet.

## Verwendete Testseite

- <https://the-internet.herokuapp.com/>
