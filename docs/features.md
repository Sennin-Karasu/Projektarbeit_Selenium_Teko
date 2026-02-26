# Feature-Dokumentation

Standardmäßig verwendet das Tool `https://the-internet.herokuapp.com/` als Zielseite. Alle Befehle akzeptieren eine optionale URL als Parameter.

## Grundfeatures

| Feature | Zeilennummern | Kurzbeschreibung |
| --- | --- | --- |
| `title` | 101-124 | Webseite laden und Titel anzeigen |
| `get` | 127-152 | GET-Request mit optionalen Query-Parametern |
| `post` | 161-190 | Login-Formular ausfüllen und absenden |
| `list-cookies` | 193-223 | Alle Cookies der Seite anzeigen |

## Zusatzfeatures

| Feature | Zeilennummern | Kurzbeschreibung |
| --- | --- | --- |
| Automatische Selenium-Installation (`check_selenium`) | 14-40 | Prüft beim Start ob Selenium installiert ist. Fragt den Nutzer und installiert es bei Bedarf automatisch per pip |
| Optionale URL als Parameter | alle Befehle | Jeder Befehl verwendet eine Standard-URL oder eine per CLI übergebene URL (`python selenium_tester.py title https://example.com`) |
| Client-Fehlerbehandlung bei ungültigem Command | 288-292 | Ungültige Befehle werden abgefangen, Help angezeigt und Exit-Code 2 zurückgegeben |
| Fehlerbehandlung bei ungültiger Website | 114-118, 143-146 | Website-Ladefehler werden abgefangen, Fehlermeldung ausgegeben und Exit-Code 1 gesetzt |
| Dynamische GET-Parameter über Client | 125-130, 272 | GET-Parameter können als CLI-Argument übergeben werden (`python selenium_tester.py get name=max`) |
| Texteingabe in Formularfeld (`keypress`) | 252-291 | Sucht erstes `input[type='text']` oder `input[type='search']` auf der Seite und tippt den per CLI übergebenen Text ein |
| Checkboxen auslesen (`checkbox`) | 210-249 | Findet alle `input[type='checkbox']` auf der Seite und gibt aus, welche ausgewählt sind; optionale URL als Argument |
| Slider auf Maximum (`slider`) | 295-325 | Bewegt den horizontalen Slider per Tastendruck auf den Maximalwert und gibt den angezeigten Wert aus |

## Verwendete Testseite

- <https://the-internet.herokuapp.com/>
