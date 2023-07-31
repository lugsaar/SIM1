# SIM1

SIM1 oder Simulation One oder Simone ist der erste Step in dem Projekt, einen Roboter zu bauen, der ein interaktives Gespräch mit einem Moderator führt.

In der fertigen Ausbaustufe wird der Roboter auf Position des Moderatorengesichtes, erkannte Gestik, Keywords oder Sprache mit einer gesprochenen Antwort, Gestik und Mimik reagieren. Die Antwort kann durch AI generiert werden, damit erhält AI einen Avatar.

Simone ist die Basis dazu. Es wird eine Hardware/Software mit Sensoren und Aktuatoren entwickelt. Simone erfasst Vorgänge und gibt Antworten aus.


### Vorgänge sind
- Druck eines Tasters
- Gesten einer Hand
- Keywords
- Spracherkennung


### Antworten sind Einzel- und Sammelreaktionen

#### Einzelreaktionen 
- Einzelbewegungen von Arm und Kopf
- LED-Anzeigen der Augen
- Sprachantwort
- Mundanzeige Sprechen

#### Sammelreaktionen 
- Mundanzeigen wie Lachen, Trauer, Erstaunen, Grübeln
- Mundbewegungen Sprechen
- Aufmerksamkeit
- Jubelarme
- Palmface
- Nicken
- Kopfschütteln
- Schulterzucken


## HARDWARE

- Raspberry Pi 4B

### Sensoren um einen Vorgang zu erfassen
- Taster
- USB-Mikrofon
- USB-Kamera

### Aktuatoren um eine Reaktion darzustellen
- LED Auge links
- LED Auge rechts
- OLED Display als Mund
- Servo Arm rechts
- Servo Arm links
- Servo Pan, Kopf schwenken
- Servo Tilt, Kopf nicken
- USB-Soundkarte für Sprachausgabe



## SOFTWARE SIM1

Der erste Schritt ist der Theatermodus. Es werden vorgefertigte Antworten aus Gestik und Text sukzessiv wiedergegeben.

###  Version 0.1 Theatermodus
- Auslöser der ersten Antwort ist ein Tastendruck
- Auslöser der Folgeantworten sind Tastendruck oder abgelaufene Zeit 
- Nur Einzelreaktionen
- Mundbewegung als simple Balkengrafik
- Inhalte einer Antwort sind mehrere Reaktionen, die gleichzeitig oder sukzessiv abgespielt werden 
- Die in den Antworten auszugebende Sprache liegt als Textfile vor
- Ablage-Format der Antworten: Json



## HARDWARE Sim1 Version 0.1

- Aufbau auf Entwicklungsbord
- Servo Arm links
- Servo Head Pan (Kopf drehen)
- OLED Display 128x64, i2c-Anschluß
- USB-Soundkarte für Sprachausgabe





