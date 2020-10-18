# Temperatursensor med BeagleBone Black

[Basert på denne guiden](https://elinux.org/EBC_Exercise_31_Dallas_1-Wire)

## Du trenger:
 - BeagleBone Black Rev. C
 - Internett-tilkobling
 - DS18B20 temperatursensor
 - Resistor (anbefalt 4,7k ohm). Her 1k ohm
 - 5 ledninger med han-pin

Alle tilkoblinger er gitt i forhold til den flate siden på temperatursensoren.

Koble temperatursensoren til breadboard. Her har vi brukt P9-siden på BBB. Koble sort ledning i P9_1 på BBB og på negativ-siden på breadboard. Rød ledning kobler du i P9_3, og på positiv-side på breadboard. Koble en resistor mellom positiv og og kolonne a. Bruk en orange ledning for p koble mellom resistor og midt-pinnen til temperatursensoren. Bruk en til orange ledning for å koble mellom midterste pinne og P9_12 på BBB. En ny rød ledning kobles mellom positiv pol og 3.3V-polen på sensoren. Denne er på høyre side når du ser mot den flate siden.
Jording kobles til den venstre polen.

PS: Hvis du kobler feil, så vil temperatursensoren bli glovarm. Vær forsiktig!

Start opp BBB
```sh
 /lib/firmware
```
 Her finner du en liste over enheter som er forhåndsprogramert til å fungere med BBB. Vi er ute etter BB-W1-P9.12-00A0-dtbo

```sh
 ls /lib/firmware/BB-W1-P9.12-00A0.dtbo
 cd /opt/source/bb.org-overlays/

 git pull
```
Kommandoene over henter ned en oppdatert oversikt over tilbehør.

```sh
cd src/arm
ls *W1*
>BB-W1-P9.12-00A0.dts
less *W1*
```
less-kommandoen skriver ut innholdet i dts-skriptet.

Rediger så filen /boot/uEnv.txt med Nano, vi eller lignende.
```sh
nano /boot/uEnv.txt
# Finn linjen med #uboot_overlay_addr4=/lib/firmware/<file0>.dtbo
# Endre til. Husk å fjerne # foran for å avkommentere linjen.
uboot_overlay_addr4=/lib/firmware/BB-W1-P9.12-00A0.dtbo
```

Start beaglebone på nytt.
```sh
sudo reboot
```
