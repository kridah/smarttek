# Sensorsystem
 -- obligatorisk oppgave 2 - smartteknologi -- \
 -- Kristoffer Dahl - kda068 -- \
 [GitHub-repo for oppgaven](https://github.com/kridah/smarttek/tree/master/sensorsystem)
 
## Fotopleytsmograf
```python
import Adafruit_BBIO.ADC as ADC
from time import sleep

ADC.setup()
timer = 0.0
voltage = 0
while timer <= 20:
    ADC.read("P9_40")
    timer += 0.1
    # skriv ut tid $1 (x) og motstand ($2) (y)
    print("{:.3f}, {:.4f}".format(timer, ((ADC.read("P9_40") * 4096) / 1.8)))
    sleep(0.1)  # millisekunder mellom hver måling
```

I denne oppgaven har jeg satt opp en fotopletysmograf (sensoren) hvis formål er å måle endringer i 
fargene gitt i "bloodvessels" i fingeren. 
Når man starter programmet leses spenningsforskjellen sensoren avgir. I mine målinger er forskjellen 
mellom høy og lav i beregnet gjennomsnitt ca 1.0 [179.5 - 180.5].
 
I vedlagt bildefil, [average_multi.png](https://github.com/kridah/smarttek/blob/master/sensorsystem/HeartRate/average_multi.png),
 er det gjort en måling over 20 sekunder.
Programmet skriver ut to datafelt. Tid og spenning separert med komma. Dette lagres i en csv-fil.
Det gjøres måling circa 10 ganger i sekundet, gitt ved sleep(0.1) 
Ved å ta gjennomsnittet reduseres variasjonen mellom bølgetopp og -bunn, samtidig som antall topper og bunner blir mindre. 
Ut fra det tolker jeg det slik at gjennomsnittet fungerer som et filter som tar bort unøyaktigheter i målingene.

Gnuplot-skriptet average.gp tar dataene fra csv-filen produsert av utskriften for hr_reader.py og plotter to datafelt.
Grønn linje viser rådata, mens rød linje viser et gjennomsnitt for hver femte måling.
[*Figur:* Gjennomsnittsmåling](https://github.com/kridah/smarttek/blob/master/sensorsystem/HeartRate/average_multi.png)

## Tolking av graf
For å finne puls ser jeg på topper i grafen. Med topper mener jeg punkter i grafen som kommer etter 
et lavpunkt. Målingene vi får ut fra sensoren vil ikke være nøyaktige eller jevne, blant annet fordi
sensoren er følsom i forhold til trykk, lysforhold og temperatur (i fingeren).
Av vedlagt graf teller jeg 18 bølgetopper i tidsintervallet 20 sekunder. Det gir en anslått plus på 54 slag i minuttet.
Om ikke helt nøyaktig, så er det absolutt innen rekkevidde. Min normale hvilepuls ligger i spektret 60 - 80 bpm.

## Temperatur
```python
import Adafruit_BBIO.ADC as ADC

# https://elinux.org/EBC_Exercise_31_Dallas_1-Wire

ADC.setup()
pin = "P9_12"
sensor_path = "/sys/class/hwmon/hwmon0/temp1_input"
with open(sensor_path, 'r') as file:
    for temp in file:
        print(float(temp)/1000)
```
DS18B20 er en digital sensor som leses av fra en GPIO-pin på BeagleBone Black. Etter å ha fulgt en guide på elinux.org 
fikk jeg koblet opp sensoren på breadboard, og etterhvert lest data fra filen som sensoren aksesseres gjennom.
Koden er enkel nok. Man leser fra filen, og får et tall som må deles på 1000 for å få temperatur i celsius.
Plot av temperatur finnes i grafen  [*Figur:* Temperatur og "Puls"](https://github.com/kridah/smarttek/blob/master/sensorsystem/temp_and_hr.png)


## Puls og temperatur
```python
import Adafruit_BBIO.ADC as ADC

# måler temperatur ca hvert 0.8 sekund
from datetime import datetime

ADC.setup()

sensor_path = "/sys/class/hwmon/hwmon0/temp1_input"
timestamp = datetime.now().timestamp()
timer = 0
   # hr =  (ADC.read("P9_40") * 4096) / 1.8
with open(sensor_path, 'r') as file:
    for temp in file:
    # skriv ut tid $1 (x) og motstand ($2) (y), temperatur ($3) (y)
        print("{:.3f}, {:.4f}, {}".format(
            datetime.now().timestamp() - timestamp,     # tid mellom hver måling
            ((ADC.read("P9_40") * 4096) / 1.8),
            float(temp) / 1000)
        )
```

Et godt og nøyaktig oppsett med måling fra fotopletysmograf og temperatursensor viser seg å være vanskeligere å få til
 enn man skulle tro. Det kommer blant annet av at det tar tid før man får lest data fra temperatursensoren, rundt 0,8 sekunder.
 Det gjør det vanskeligere å få hyppige målinger med fotopletysmografen, noe som er nødvendig for gode data. 
 Klarer derfor ikke å lese ut puls fra data i grafen:
 [*Figur:* Temperatur og "Puls"](https://github.com/kridah/smarttek/blob/master/sensorsystem/temp_and_hr.png)
 
## Bilder
[*Figur:* Oppsett Fotopletysmograf](https://github.com/kridah/smarttek/blob/master/sensorsystem/oppsett%20ppm.jpg) \
[*Figur:* Oppsett temperatursensor](https://github.com/kridah/smarttek/blob/master/sensorsystem/oppsett%20temp.jpg) \
[*Figur:* Oppsett fotopletysmograf og temperatursensor](https://github.com/kridah/smarttek/blob/master/sensorsystem/oppsett_ppm_temp.jpg) \
[*Figur:* Bruk av komplett oppsett](https://github.com/kridah/smarttek/blob/master/sensorsystem/oppsett%20begge%20sensorer.jpg) \
[*Figur:* Koblingsskjema](https://github.com/kridah/smarttek/blob/master/sensorsystem/koblingsskjema.png)