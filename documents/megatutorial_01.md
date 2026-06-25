# Industrial Predictive Maintenance

In einer automatisierten Fertigungshalle steht eine hydraulische Großstanze. Um ungeplante Stillstände zu vermeiden, überwacht das IoT-System der Maschine drei binäre Sensoren:

* Hohe Temperatur ($X_1$): 1 = Die Betriebstemperatur liegt über dem kritischen Schwellenwert von 85°C.
* Öldruck-Warnung ($X_2$): 1 = Der Hydrauliköldruck ist außerhalb des optimalen Bereichs.
* Vibrationsanomalie ($X_3$): 1 = Die Schwingungssensoren melden unnormale mechanische Vibrationen.

## Systemlogik

Die Maschine ist robust gebaut. Wenn nur ein einzelner Sensor anschlägt, kann das System dies kurzzeitig kompensieren (kein Ausfall). Sobald jedoch mindestens zwei Faktoren gleichzeitig auftreten (z. B. Hitze und Druckabfall oder Hitze und Vibration), überhitzt das System oder nimmt Schaden, was zu einem automatischen Not-Aus (Maschinenausfall = 1) führt. Einzige Ausnahme: Wenn alle drei Sensoren gleichzeitig anschlagen (1,1,1), greift sofort die absolute Kernschmelz-Sicherung.

## Daten

| Datensatz-ID | Hohe Temperatur ($X_1$) | Öldruck-Warnung ($X_2$) | Vibrationsanomalie ($X_3$) | **Maschinenausfall ($Y$)** | Beschreibung / Zustand |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | 0 | 0 | 0 | **0** | Normalbetrieb. Alles läuft perfekt. |
| **2** | 0 | 0 | 1 | **0** | Leichte Vibration. Gelbe Warnung, aber Maschine läuft weiter. |
| **3** | 0 | 1 | 0 | **0** | Öldruck schwankt minimal. System kompensiert. |
| **4** | 0 | 1 | 1 | **1** | **Ausfall:** Druckabfall + Vibration führen zu mechanischer Blockade. |
| **5** | 1 | 0 | 0 | **0** | Maschine ist heißgelaufen, läuft aber stabil im Toleranzbereich. |
| **6** | 1 | 0 | 1 | **1** | **Ausfall:** Hitze + Vibrationen beschädigen die Lager. Not-Aus. |
| **7** | 1 | 1 | 0 | **1** | **Ausfall:** Hitze + falscher Öldruck zerstören den Schmierfilm. Not-Aus. |
| **8** | 1 | 1 | 1 | **1** | **Ausfall:** Kritischer Systemfehler auf allen Ebenen. Sofortiger Shutdown. |

## Aufgabenstellung

* [ ] Führe auf den Daten (oberhalb) eine Feature-Extraction durch.
* [ ] Erstelle eine Lernumgebung, um ein Deep-Learning-Modell zu entwickeln.
* [ ] Entwickle ein Netzlayout, um die Daten zu verarbeiten.
* [ ] Trainiere das Netz.
* [ ] Evaluiere die Ergebnisse deines Trainings.
