# APNG-Steganography
Originally created for the "ostrich" challenge in the Nahamcon 2021 CTF
Takes an APNG file and compares each frame to an original picture to locate changed or encrypted pixels,
extracts unicode values from the RGB values of each changed or encrypted pixel, and then
Compiles them all back into characters in a string.
