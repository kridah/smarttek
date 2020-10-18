# Sensorsystem
 -- obligatorisk oppgave 2 - smartteknologi --
 -- Kristoffer Dahl - kda068 --
 
## Fotopleytsmograf
@kodefil: hr_reader.py\
@bildefil: average_multi.png\
I denne oppgaven har jeg satt opp en fotopletysmograf (sensoren) hvis formål er å måle endringer i 
fargene gitt i "bloodvessels" i fingeren. 
Når man starter programmet leses spenningsforskjellen sensoren avgir. I mine målinger er forskjellen 
mellom høy og lav i beregnet gjennomsnitt ca 1.0 [179.5 - 180.5].
 
I vedlagt bildefil, average_multi.png, er det gjort en måling over 20 sekunder.
Programmet skriver ut to datafelt. Tid og spenning separert med komma. Dette lagres i en csv-fil.
Det gjøres måling circa 10 ganger i sekundet, gitt ved at sleep(0.1) 
Ved å ta gjennomsnittet reduseres variasjonen mellom bølgetopp og -bunn, samtidig som antall topper og bunner blir mindre. 
Ut fra det tolker jeg det slik at gjennomsnittet fungerer som et filter som tar bort unøyaktigheter i målingene.

Gnuplot-skriptet average.gp tar dataene fra csv-filen produsert av utskriften for hr_reader.py og plotter to datafelt.
Grønn linje viser rådata, mens rød linje viser et gjennomsnitt for hver femte måling.

## Graf og puls
For å finne puls ser jeg på topper i grafen. Med topper mener jeg punkter i grafen som kommer etter 
et lavpunkt. Målingene vi får ut fra sensoren vil ikke være nøyaktige eller jevne, blant annet fordi
sensoren er følsom i forhold til trykk, lysforhold og temperatur (i fingeren).
Av vedlagt graf teller jeg 18 bølgetopper i tidsintervallet 20 sekunder. Det gir en anslått plus på 54 slag i minuttet.
Om ikke helt nøyaktig, så er det absolutt innen rekkevidde. Min normale hvilepuls ligger i spektret 60 - 80 bpm.

## Puls og temperatur
Et godt og nøyaktig oppsett med måling fra fotopletysmograf og temperatursensor viser seg å være vanskeligere å få til
 enn man skulle tro. Det kommer blant annet av at det tar tid før man får lest data fra temperatursensoren, rundt 0,8 sekunder.
 Det gjør det vanskeligere å få hyppige målinger med fotopletysmografen, noe som er nødvendig for gode data. 
 Klarer derfor ikke å lese ut puls fra data i temp_and_hr.png
 
