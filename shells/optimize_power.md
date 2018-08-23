# Optimize power for Ubuntu 16.04

## Install 

```shell

sudo apt install powertop
sudo apt install tlp tlp-rdw

```
## Configure tlp

**tlp** comes with pre-configured settings for general users, just run `sudo tlp start`. 

## Configure powertop

Run this command to calibrate powertop `sudo powertop --calibrate`. Then, run `sudo powertop --auto-tune` to tune powertop. 

After that, edit/create and edit `/etc/systemd/system/powertop.service` in **sudo** mode and paste below lines in the file:

```bash
[Unit]
Description=Powertop tunings

[Service]
ExecStart=/usr/bin/powertop --auto-tune
RemainAfterExit=true

[Install]
WantedBy=multi-user.target

```

sudo systemctl enable powertop.service
