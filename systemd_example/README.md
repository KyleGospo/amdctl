1. Copy the sample script to /usr/sbin and make it executable with `sudo chmod +x /usr/sbin/amdctl.sh`

2. Edit the script and fill in your tested values for voltage/clockspeed for each P-state.

3. Copy amdctl-boot.timer, amdctl-boot.service and amdctl-after-suspend.service to
    /usr/lib/systemd/system

4. Enable amdctl-boot.timer with
    `systemctl enable amdctl-boot.timer`

5. Enable amdctl-after-suspend.service with
    `systemctl enable amdctl-after-suspend`

6. Reboot

