# r2d2

Reboot of the Cornell Cup R2-D2 Project

## Microcontroller Selection

| Name | Processor | Clock | Memory | Price | Comments |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Arduino Pro Mini | ATmega328 | 16 MHz | 2kb | $10 | Lots of $2 clones on aliexpress, no hardware serial, no microusb |
| Arduino Nano | ATmega328P | 16 MHz | 2kb | $22 | Lots of $3 clones on aliexpress |
| Sparkfun Pro Micro | ATmega32U4 | 16 MHz | 2.5kb | $20 | Lots of $5 clones on aliexpress |
| Teensy LC | ARM Cortex-M0+ | 48 MHz | 8kb | $13 | Multiple serial, high clock speed, good price |
| STM32 F0 Discovery | ARM Cortex-M0 | | 8kb | $8.88 | Not Arduino, requires Keil |

The best option is either the **Nano** or **Pro Micro** board clones from AliExpress. The Pro Mini would require an additional FTDI breakout, the STM32 a whole different toolset. The Teensy LC is slightly expensive, but useful for peripherals that need more processing power.

After investigating costs and shipping, the **Nano** clones are the better option in the interest of time.

## TODO

* Add more test cases for R2 Protocols
* Peripherals
* Central
