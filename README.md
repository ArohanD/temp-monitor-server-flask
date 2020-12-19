# Creating a Networked System Temperature Monitor Display on the Raspberry Pi

![](https://raw.githubusercontent.com/ArohanD/temp-monitor-server-flask/main/pics/IMG_0135.jpg)
![](https://raw.githubusercontent.com/ArohanD/temp-monitor-server-flask/main/pics/IMG_0134.jpg)

## Outline

- Pic with explanation
- Warnings
- Building Flask with Open Hardware Monitor
- Building Frontend Svelte and Electron
    - Warn that Electron is not necessary
- Set up autoload script on pi
- Helpful cli things
    - Open gifs

Has your PC maxed out on RGB? Do you think RGB is tasteless? What do you do when you realize that the process of building your PC was a lot more fun than spending 20-30 minutes staring at your steam Library before closing steam and hopping on YouTube?

If you're still seeking the thrill of building/customizing your PC and looking for ways not to break the bank, this project might be for you.

Inspired by the [NZXT Kraken](https://www.nzxt.com/products/kraken-z63), I wanted to create a way to display system stats (or [gifs](https://d1sxg8jua9jde6.cloudfront.net/wp-content/uploads/2020/01/nzxt-kraken-z-3-cooler-animated-gif-1024x576.jpg)) inside of my PC, but I didn't want to jump into water-cooling just yet. I also wanted it to be wireless as I have enough issues with cable management, and I didn't want the system to be "a part of" my PC in any way. It's not nearly as elegant as NZXT's tech, but it definitely scratched the PC building itch I had, and mostly with some parts I had lying around the house.

In **Part 1**, we're going to be building a temperature reader for Windows in Python, and then creating a web-server in Flask to host an API (and optionally a static site)  that will provide system stats. I'm only covering CPU and GPU temps in this tutorial, but you can easily modify it to get the stats you want.  In **Part 2**, we'll build a reactive GUI in Svelte to display data from this API, and then use Electron to build a Linux binary to run the site as a Linux application on any arm7l devices, like a Raspberry Pi. 

## Materials

Everything on this list can be substituted, and I'd encourage you to see what's lying around the house. 

### Server

- Windows PC
    - If you want monitor system stats for Mac or Linux, you can modify the `sys_monitor.py` file to use a library like [pyspectator](https://pypi.org/project/pyspectator/).
- You'll need to be on your private network you trust, like your home network.

### Display

- Raspberry Pi
    - To build and run as an application on Electron, it'll need to run on armv7 or higher architecture, one of the following models: Pi4 (any config), Pi3 (any config), Pi2 (Model B). You should also be able to use any other [SBC](https://en.wikipedia.org/wiki/Single-board_computer) that [Electron](https://www.electron.build/cli.html#targetconfiguration) has a configuration for.
    - If you don't have a board that Electron can compile too, I'll show you how to configure the server to host a static site, and how to configure your SBC visit and boot this site fullscreen on load. I ended up doing this as I used a Pi Zero W which runs armv6 to keep things compact. This method will also let you view your GUI on any device on your network.
    - If you're new to using the Pi, I'd recommend getting a [full starter kit](https://vilros.com/collections/raspberry-pi-4/products/vilros-raspberry-pi-4-model-b-complete-starter-kit-with-clear-transparent-case-and-built-in-fan), which comes with a compatible power supply and hdmi adapter.
- A Screen
    - I ended up going with iUnker's 2.8 inch screen but it involved some soldering and [manual configuration](https://www.amazon.com/gp/customer-reviews/R2DVAJIA0JZ7JT/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&ASIN=B07H8ZY89H). Alternatively you can use DuPont cables on the Pi5 to get the screen running, which I did before soldering to make sure everything worked.
- SD Card
- Flashing Software - I like the official [Pi Imager](https://www.raspberrypi.org/software/) and [Balena Etcher](https://www.balena.io/etcher/)
- USB/Bluetooth keyboard and mouse

# Building the Apps

Back-End Server: https://github.com/ArohanD/temp-monitor-server-flask

Front-End App: https://github.com/ArohanD/temp-monitor-svelte

## 1. Setting up your PC

We're going to use [package] to read system stats on windows, but in order for the package to perform reads, we'll need to install [Open Hardware Monitor](https://openhardwaremonitor.org/downloads/). Once you've downloaded installer, open the app and you should see this:

[Pic]

The OHM is just a windows executable, and it's going to be a pain to start it up manually every-time you turn your computer on. It's a pretty lightweight app so you can have it run automatically on startup when windows starts:

1. first
2. second
3. third

## Configuring the Flask Server

## Setting up the RasberryPi

### For ARMv7+ Models (2B, 3 or 4)

### For ARMv6


