# Forensics-2

> 1. Develop the parser, using both the specification and foo.fpff for reference. stub.py contains the beginnings of a Python parser, if you'd like to develop in Python (2).

My Parser code can be found in the [```stubs.py```](https://github.com/yreiss1/Forensics-2/blob/master/stub.py)``` file located in this repository.

This is my output:
```
------- HEADER -------
MAGIC: 0xbefedade
VERSION: 1
TIMESTAMP: 2003-06-24 12:38:55
AUTHOR: mnthomp
SECTION COUNT: 9

-------  BODY  -------


----- SECTION 1 -----

Type: SECTION_ASCII
Length: 34

SECTION ASCII: i love leaving restaurant reviews!

----- SECTION 2 -----

Type: SECTION_WORDS
Length: 60

Words: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

----- SECTION 3 -----

Type: SECTION_COORDS
Length: 16

Coordinates: (latitude: 25.291332, longitude: -80.3809373)

----- SECTION 4 -----

Type: SECTION_REFERENCE
Length: 4

Reference #: 1

----- SECTION 5 -----

Type: SECTION_ASCII
Length: 37

SECTION ASCII: i wonder when they'll fix their sign?

----- SECTION 6 -----

Type: SECTION_ASCII
Length: 34

SECTION ASCII: i heard their naan is always fresh

----- SECTION 7 -----

Type: SECTION_COORDS
Length: 16

Coordinates: (latitude: 38.9910941, longitude: -76.9328019)

----- SECTION 8 -----

Type: SECTION_PNG
Length: 135811

Creating picture with name: CMSC389R_pic8

----- SECTION 9 -----

Type: SECTION_ASCII
Length: 56

SECTION ASCII: NF2CO4ZANRUWWZJAMEQGMYLDORXXE6JMEBRHK5BAMZXXEIDGN5XWIIIK

----- SECTION 10 -----

Type: SECTION_ASCII
Length: 45

SECTION ASCII: Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


----- SECTION 11 -----

Type: SECTION_DWORDS
Length: 48

Dwords: [4, 8, 15, 16, 23, 42]
```

> 2. Parse foo.fpff, and report the following information:

**_When was ```foo.ffpf``` generated?_**

The file was generated on 06/14/2003 at 12:38:55, I got this time and date from the timestamp data located in the header of the ```foo.fpff``` file. After unpacking the Magic number and Version number, the timestamp was a 4 byte _word_, so inorder to convert the timestamp to datetime format I imported the datetime library and converted the timestamp to a datetime object, which allowed me to aquire the date and time of file creation.


**_Who authored ```foo.fpff```?_**

The author of ```foo.fpff``` is our one and only mnthomp, or by his real name, Mark Thompson. After unpacking the timestamp, the author is the next data provided in the header of the fpff file. Obtaining this data, we recevied the mnthomp22 username, which could only be our good friend Mark Thompson.

**_How many sections does foo.fpff say it has? How many sections are there really?_**

According to the section count provided in the file header there are 9 sections, but when running my code on the ```foo.fpff``` I realized that there was still more data to be parsed after parsing 9 sections, after parsing the remaing data I discovered the additional 2 sections that makes a total of 11 sections.

**_List each section, giving us the data in it and its type._**

Section 1

Type: SECTION_ASCII
Data: ```i love leaving restaurant reviews!```

Section 2

Type: SECTION_WORDS
Data: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

Section 3

Type: SECTION_COORDS
Data: ```(25.291332, -80.3809373)```

These coordinates appear to lead us to location slightly west of Card Sound Road and a resteraunt by the name of Alabama Jacks between Miami and the Florida Keys:

![alt text](https://github.com/yreiss1/Forensics-2/blob/master/location1.png)

Section 4

Type: SECTION_REFERENCE
Data: ```1```

Section 5

Type: SECTION_ASCII
Data: ```i wonder when they'll fix their sign?```

Section 6

Type: SECTION_ASCII
Data: ```i heard their naan is always fresh```

Section 7

Type: SECTION_COORDS
Data: ```(38.9910941, -76.9328019)```

These coordinates appear to lead us to the street right infront of the Food Factory in College Park!

![alt text](https://github.com/yreiss1/Forensics-2/blob/master/location2.png)

Section 8

Type: SECTION_PNG
Data: This picture

![alt text](https://github.com/yreiss1/Forensics-2/blob/master/CMSC389R_pic8.png)

Section 9

Type: SECTION_ASCII
Data: ```NF2CO4ZANRUWWZJAMEQGMYLDORXXE6JMEBRHK5BAMZXXEIDGN5XWIIIK```

Section 10

Type: SECTION_ASCII
Data: ```Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9```

Section 11

Type: SECTION_DWORDS
Data: ```[4, 8, 15, 16, 23, 42]```

**_Report the two flags hidden in foo.fpff, and the one flag on the web referenced by foo.fpff_**

The first flag I obtained from section 9, I realized that there must be more to the data that I recieved after running my code, and realized that flags for these assignments were often encrypted using a base64 encoder, I tried to decode using the same base 64 but did not recieve anything meaningful or substantial, so I thought maybe using a different base decoder would do the trick, and after using the 32 base decoder I recieved: ```it's like a factory, but for food!```
Not sure if this is a flag.... but its something


One flag that I found was hidden in Section 10, I realized that there was probably more to this data, and remembering the use of encryption in other homeworks, I used the same base 32 encryption that I used for the hidden data in section 9, this did not give me anything meaningful or substantial as well, so I reverted back to the base 64 we had been using up till now, using that I recieved the flag:

```CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}```

The second flag I recieved was through parsing the PNG image in section 8, which displayed the 2nd flag: 

```CMSC389R-{c4tsk1ll-m0unt41n5}```


