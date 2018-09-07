# IOS Device Upgrade
This repository contains the Ansible script for upgrading various Cisco IOS devices to a target version.
The target version is defined in /inventory/network/software.yml, which contains reference to unique hardware 
models. Each hardware model is mapped to a particular target IOS version. In addition to the version, the 
image filename, image size, and image checksum are included. 

The main playbook: network-upgrade.yml follows this logic:
- Obtain the hardware model and current IOS version of the device.
- Lookup the target version in software.yml based on obtained hardware model.
- If the version on the device matches the target version, the rest of the playbook is skipped for that device.
- If the image file is not already staged:
-   a) Check for available space.
-   b) Copy image via HTTP from my server (prefix defined in software.yml) to flash.
- Calculate a checksum against the file in flash.
- Compare checksum to known checksum (defined in software.yml).
- Display a bunch of gathered data.
- Output the gathered data to a file.
- Activate image file (method depends on hardware model).
- Reload the switch.
- Wait for port 22 to accept connections again.
- Have the upgraded device ping a known good IP and validate results.
- Assert that the new version of the device matches the target version


