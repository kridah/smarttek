# Sensorsystem
 -- obligatorisk oppgave 2 - smartteknologi --
 -- Kristoffer Dahl - kda068 --
 
## Fotopleytsmograf
@fil: hr_reader.py
I denne oppgaven har jeg satt opp en fotopletysmograf (sensoren) hvis formål er å måle endringer i 
fargene gitt i "bloodvessels" i fingeren. 
Når man starter programmet leses spenningsforskjellen sensoren avgir. I mine målinger er forskjellen 
mellom høy og lav ca 1.0 [179.5 - 180.5]. I vedlagt bildefil, average.png, er det gjort en måling over 20 sekunder.
Programmet skriver ut to datafelt. Tid og spenning separert med komma. Dette lagres i en csv-fil.
Det gjøres måling 10 ganger i sekundet.

Gnuplot-skriptet average.gp tar dataene fra csv.filen produsert av hr_reader. 
Det beregnes et gjennomsnitt gitt hver femte måling, og videre lages en ny graf.

## Graf og puls
For å finne puls ser jeg på topper i grafen. Med topper mener jeg punkter i grafen som kommer etter 
et lavpunkt. Målingene vi får ut fra sensoren vil ikke være nøyaktige eller jevne, blant annet fordi
sensoren er følsom i forhold til trykk, lysforhold og temperatur (i fingeren).
Av vedlagt graf teller jeg 18 bølgetopper i tidsintervallet 20 sekunder. Det gir en anslått plus på 54 slag i minuttet.
Om ikke helt nøyaktig, så er det absolutt innen rekkevidde. Min normale hvilepuls ligger i spektret 60 - 80 bpm.

