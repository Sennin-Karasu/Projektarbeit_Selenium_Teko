# Feature-Dokumentation

## Minimalsystem (Pflicht)
Diese Features gehören zum Minimalsystem und wurden implementiert:

- `title` (Selenium: Webseite laden und Titel anzeigen)
- `get` (GET mit Variablen)
- `post` (POST / Formular absenden)
- `list-cookies` (Cookies anzeigen)
- minimale Dokumentation > Readme.md 

## Zusatzfeatures (für zusätzliche Punkte)

| Feature                                        | Implementiert | Datei | Zeilennummern          | Kurzbeschreibung |
|------------------------------------------------|---|---|------------------------|---|
| Optionale URL als Parameter für `title`        | Ja | myproject.py | ca. 22-32, ca. 103-106 | `title` verwendet Standard-URL oder eine per CLI übergebene URL (`python myproject.py title https://example.com`) |
| Client-Fehlerbehandlung bei ungültigem Command | Ja | myproject.py | 86-110 | Ungültige Befehle werden abgefangen, Help angezeigt und Exit-Code 2 zurückgegeben |
|                                                |    |              |                        |                                                                                                                   |
|                                                |    |              |                        |                                                                                                                   |
|                                                |    |              |                        |                                                                                                                   |
|                                                |    |              |                        |                                                                                                                   |
| Fehlerbehandlung bei ungültiger Website | Ja | myproject.py | xx-yy | Website-Ladefehler werden abgefangen, Fehlermeldung ausgegeben und Exit-Code 1 gesetzt |



Hinweis: Ohne URL wird weiterhin die Standard-Testseite `https://the-internet.herokuapp.com/` verwendet.

## Verwendete Testseite
- https://the-internet.herokuapp.com/