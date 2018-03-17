#!/usr/bin/env python2

import sys
import struct
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xbefedade
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff")

# Normally we'd parse a stream to save memory, but the RCFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as rcff:
    data = rcff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

index = 24;
magic, version, timestamp, author, count = struct.unpack("<LLL8sL", data[0:index])


if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.fromtimestamp(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d\n" % int(count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual RCFF body. Good luck!

print("-------  BODY  -------\n")
sect_count = 1
while (index < len(data)):
	
	print("\n----- SECTION " + str(sect_count) + " -----\n")
	sType,sLength = struct.unpack("<LL", data[index:index+8])

	
	index += 8


	if (sType == 1):
		val = data[index:index+sLength]
		print("Type: SECTION_ASCII")
		print("Length: %d\n" % sLength)

		print("SECTION ASCII: " + val)
		index += sLength
		
	elif (sType == 2):
		val = data[index:index+sLength]
		print("Type: SECTION_UTF-8")
		print("Length: %d\n" % sLength)

		print("UTF-8: " + val)
		index += sLength

	elif(sType == 3):
		words = sLength / 4
		wordsArray = []

		for i in range(0,words):
			word = struct.unpack("<L", data[index:index+4])[0]
			wordsArray.append(word)
			index += 4

		print("Type: SECTION_WORDS")
		print("Length: %d\n" % sLength)
		print("Words: " + str(wordsArray))

	elif(sType == 4):

		words = sLength / 8
		wordsArray = []

		for i in range(0,words):
			word  = struct.unpack("<Q", data[index:index+8])[0]
			wordsArray.append(word)
			index += 8


		print("Type: SECTION_DWORDS")
		print("Length: %d\n" % sLength)
		print("Dwords: " + str(wordsArray))

	elif (sType == 5):

		doubles = sLength / 8
		doubleArray = []

		for i in range(0,doubles):
			double = struct.unpack("<d", data[index:index+8])[0]
			doublesArray.append(double)
			index += 8

		print("Type: SECTION_DOUBLES")
		print("Length: %d\n" % sLength)
		print("Doubles: " + str(doublesArray))

	elif (sType == 6):

		latitude,longitude = struct.unpack("<dd", data[index:index+16])
		index += 16
		print("Type: SECTION_COORDS")
		print("Length: %d\n" % sLength)
		print("Coordinates: (latitude: "  + str(latitude) + ", longitude: " + str(longitude) + ")")

	elif (sType == 7):

		word = struct.unpack("<L", data[index:index+4])[0]
		print("Type: SECTION_REFERENCE")
		print("Length: %d\n" % sLength)
		print("Reference #: " + str(word))
		index += 4

	elif (sType == 8):

		pic = data[index:index+sLength]
		filename = "CMSC389R_pic" + str(sect_count)
		print("Type: SECTION_PNG")
		print("Length: %d\n" % sLength)
		print("Creating picture with name: " + filename)
		file = open(filename, "w")
		file.write("\x89\x50\x4e\x47\x0d\x0a\x1a\x0a")
		file.write(pic)
		index += sLength

	else:

		print("Wrong Section Type!")


	sect_count = sect_count + 1




