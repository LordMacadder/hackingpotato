#!/usr/bin/env python

user_submitted = " ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz1234567890"


for char in user_submitted:
  # '<<' is left bit shift
  # '>>' is right bit shift
  # '|' is bit-wise or
  # '^' is bit-wise xor
  # '&' is bit-wise and
  print char + " = " + str((((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )
