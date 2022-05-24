# Jiggle Jiggle

A simple Python script for Windows to simulate a key presses progamatically

## How to run

> This is only for Windows users! I expect if you're on a UNIX system to have more freedom than the typical large corp Windows images permits a user

`python jiggle.py --keys <comma seperate list of keys> --sleep <seconds to sleep>`

## Why?

Corporate lockdown can inhibit employees from using popular programs like
`caffeine` to keep their computers awake. If Python is an existing tool in the
stack though then a user can run this script to do basically exactly what
caffeine does! Every minute by default the script will press `F15` which is a
key Windows knows about but is rarely on any keyboards and it doesn't do
anything.


# Credit

Chris Kiehl's [gist](https://gist.github.com/chriskiehl/2906125) is basically
exactly this script, I just added some cli options and removed all the
functionality that is unnecessary for this simple utility
