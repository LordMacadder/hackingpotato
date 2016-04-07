#!/usr/bin/env python

user_submitted = raw_input("Enter Password: ")

if len(user_submitted) != 10:
  print "Wrong"+str(len(user_submitted))
  exit()


verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
#ub3rs3cr3t



user_arr = []
for char in user_submitted:
  # '<<' is left bit shift
  # '>>' is right bit shift
  # '|' is bit-wise or
  # '^' is bit-wise xor
  # '&' is bit-wise and
  user_arr.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )

print user_arr;
print verify_arr;

if (user_arr == verify_arr):
  print "Success"
else:
  print "Wrong"
