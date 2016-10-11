#!/usr/bin/python3
# coding: utf-8
# pylint: disable=E0602,C0103,E0012,W0612,W0613

# Copyright © 2016 Tormod Spire Bahner
# Written by Tormod Spire Bahner <tormod.spire@gmail.com>
"""program som krypterer"""
alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def encode(letter, secret):
    """This function encodes a letter"""
    pos = alphabet.find(letter)

    newpos = (pos + secret)

    if newpos >= 29:
        newpos = newpos - 29

    return alphabet[newpos]

def decode(letter, secret):
    """This function decodes a letter"""
    pos = alphabet.find(letter)

    newpos = (pos - secret)

    if newpos >= 29:
        newpos = newpos - 29

    return alphabet[newpos]

print(encode("a", 17))
print(decode("a", 17))

SECRET = 17
message = "Hello world"

output=""

for characther in message:
    if character in alphabet:
        output = output + encode(character, SECRET)

print(output)

SECRET = 17
message = "yvååc kcfåu"
output = ""

for character in message:
    if character in alphabet:
        output = output  + decode(character, secret)
