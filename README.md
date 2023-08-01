# Samsara

### Background/Problem Statement
We’re developing a product that has a GPS receiver. As part of our testing we’ve collected logs of NMEA output. 
An example output log is shown below. The t=n indicates timestamp in seconds for the given NMEA string.

### Deliverable 1:
Write a program that parses this output and provides a plot showing the number of satellites tracked as a function 
of time and outputs time to first fix (TTFF). You’re welcome to use any programming language you’re comfortable with, 
but note that we use Python.

### Solution
File nmea.py contains `class NMEA` which implements: 
* parsing data from `log.txt`
* provides a plot showing the number of satellites tracked as a function of time
* outputs time to first fix (TTFF)

### Deliverable 2:
This stream of NMEA sentences comes in over UART at 9600N1. How would you think about writing a program that parses 
a live stream of NMEA data? What modules would you use? How would you determine the start/end of a GPS scan?

### High level solution
* I'll start with using module `socket`. 
* Async reading stream data from serial port, another thread for parsing and storing data and the separate thread will 
  update plot and calculate data upon user request.
* Parse it and store to `variable` / `file` / `database` (depends on requirements and expected data volume).
* After parsing data the port I can use knowledge of different GPS message types and determine end of the message by
  parameters count and checksum or use regexp. There are also might be possibility of using low level knowledge of 
  packages to find out what is the last message in the chain.
        