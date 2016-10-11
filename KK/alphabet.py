#!/usr/bin/python3
# coding: utf-8
# pylint: disable=E0602,C0103

# Copyright © 2016 Tormod Spire Bahner
# Written by Tormod Spire Bahner <tormod.spire@gmail.com>

alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
print(len(alphabet))

letter = "a"
secret = 3


pos = alphabet.find(letter)


newpos = (pos + secret)

if newpos > 29:
    newpos = newpos - 29


secretletter = alphabet[newpos]


print(3)
