# CircuitPython code for the DeskPi PicoMate

## i2C

This setup uses two I2C buses.

* I2C0 for the OLED
* I2C1 for the other for the sensors.

## pc gadget usage

Portions of the Picomate also work when the Pico is loaded with U2IF peripheral firmware

### Host Python / Blinka software installation

Blinka is a set of CircuitPython libraries that lets you run CircuitPython on a laptop or desktop that communicates over a link to a CircuitPython device

Install the adafruit libraries on your host python environment.

```bash
# setting up windows environment for Blinka
pip3 install hidapi
pip3 install adafruit-blinka
```

If its been a while you may wish to update

```bash
# setting up windows environment for Blinka
pip3 install --upgrade hidapi
pip3 install --upgrade adafruit-blinka
```

### UTIF setup

Some of these work with U2IF.  You'll need to tell Blinka you are using U2IF

> If you are using U2IF then
> MANDATORY
> Linux export BLINKA_MCP2221=1
> Powershell $env:BLINKA_MCP2221=1
> or
>   Linux export BLINKA_U2IF=1
>   Powershell $env:BLINKA_U2IF=1
>
