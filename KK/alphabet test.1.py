#!/usr/bin/python3
# coding: utf-8
# pylint: disable=E0602,C0103

# Copyright © 2016 Tormod Spire Bahner
# Written by Tormod Spire Bahner <tormod.spire@gmail.com>
"""program som krypterer"""
alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

secret = 17
secretletter = "r"


pos = alphabet.find(secretletter)


newpos = pos - secret


if newpos < 0:
    newpos = newpos + 29

letter = alphabet[newpos]


print(letter)
