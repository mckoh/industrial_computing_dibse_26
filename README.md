# Industrial Computing DIBSE (SS26)

In diesem Repository verwalten wir alle Sourcen unseres Sommersemester-Kurses in "Industrial Computing". Unterhalb habe ich euch einige Details zusammengestellt, die für diesen Kurs wichtig sind.

## Python Version

Für die gleichzeitige Nutzung von PyTorch und TensorFlow ist die Wahl der richtigen Python-Version entscheidend, um Abhängigkeitskonflikte zu vermeiden. Die beste Wahl ist aktuell **Python 3.11** oder **Python 3.12**.

Framework | Empfohlene Version | Minimum | Maximum (Stabil)
-- | -- | -- | --
PyTorch (2.10+) | Python 3.11 / 3.12 | 3.10 | 3.14 (Preview)
TensorFlow (2.21+) | Python 3.11 / 3.12 | 3.10 | 3.13

# Virtual Environment

Um sicherzustellen, dass alle Bibliotheken korrekt isoliert installiert werden, nutzen wir eine virtuelle Umgebung mit Python 3.12.

1. **Befehlsmenü öffnen:** Befehlsmenü öffnen: Drücke `Strg + Umschalt + P` (Windows) bzw. `Cmd + Umschalt + P` (Mac).

2. **Befehl suchen:** Tippe `Python: Umgebung erstellen...` (oder `Python: Create Environment...`, falls du ein englischsprachiges VSCode nutzt) und wähle den Punkt aus.

3. **Typ wählen:** Wähle den Typ `Venv` aus.

4. **Interpreter festlegen:** Wähle aus der Liste explizit `Python 3.12` aus.

5. **Abhängigkeiten installieren:** Setze einen Haken bei der Datei `requirements.txt`.

> **Hinweis:** Falls Python 3.12 in Schritt 4 nicht erscheint, klicke auf "Enter interpreter path..." und navigiere zu deinem Installationspfad.