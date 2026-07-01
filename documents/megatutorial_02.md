# Industrial Computer Vision

In einer automatisierten Fertigungshalle eine automatische Förderanlage. Diese Transportiert Kisten von einer Fertigungsstation zur nächsten. Da es in diesem Bereich der Anlage immer wieder zu Fehlern kommt, soll eine videogestützte Überwachung installiert werden, die Fehler automatisch erkennt.

## Systemlogik

In der Maschine kommt es regelmäßig zu Blockierungen durch fehlerhaft platzierte Objekte am Förderband. Diese Situation sollen als Fehlerhaft erkannt werden. Außerdem soll erkannt werden, wenn das Förderband überhaupt keine Kisten transportiert, weil das ein Indiz für eine Fehlerhafte Situation im vorderen Teil der Maschine sein kann.

## Daten

Ich habe uns im `data`-Ordner bereits einen Bilddatensatz zusammengestellt. Wir benutzten dazu Bilder aus einer Fertigungsstraße. Diese Bilder zeigen unterschiedliche Situationen, in denen sich das Förderband befinden kann. Wir wollen diese Situationen mit Hilfe von Computer Vision erkennen und automatisch klassifizieren.

## Aufgabenstellung

* [ ] Erstelle eine Lernumgebung, um ein Deep-Learning-Modell zu entwickeln.
* [ ] Entwickle ein Netzlayout, um die Daten zu verarbeiten.
* [ ] Trainiere das Netz.
* [ ] Evaluiere die Ergebnisse deines Trainings.
