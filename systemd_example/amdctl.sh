#!/usr/bin/bash
# Script to be executed by a systemd service to change
# cpu voltage and/or clockspeed as desired.
# Please read the amdctl the instructions on how to use
# amdctl on https://github.com/kevinlekiller/amdctl first
# Copy this script to /usr/sbin, rename it (remove "sample" from its name)
# and make it executeable.
# Use this script and the amdctl-*.services/timer to apply
# your tested values automatically on boot and after
# suspend-to-ram/hibernate/hybrid-sleep
# Add your lines with changes to voltages/clocks below, one line
# per P-state.
# Example: /usr/sbin/amdctl -pX -vYY; # lower voltage by ZZZmv from AAAmV -> BBBmv
