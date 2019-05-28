"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

lines = open('foo.txt')
for line in lines:
    print(line)
lines.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

sonnet = open("bar.txt", "w")
sonnet.write("Shall I compare thee to a summer’s day?\n")
sonnet.write("Thou art more lovely and more temperate.\n")
sonnet.write("Rough winds do shake the darling buds of May,\n")
sonnet.write("And summer’s lease hath all too short a date.\n")
sonnet.write("Sometime too hot the eye of heaven shines,\n")
sonnet.write("And often is his gold complexion dimmed;\n")
sonnet.write("And every fair from fair sometime declines,\n")
sonnet.write("By chance, or nature’s changing course, untrimmed;\n")
sonnet.write("But thy eternal summer shall not fade,\n")
sonnet.write("Nor lose possession of that fair thou ow’st,\n")
sonnet.write("Nor shall death brag thou wand'rest in his shade,\n")
sonnet.write("When in eternal lines to Time thou grow'st.\n")
sonnet.write("So long as men can breathe, or eyes can see,\n")
sonnet.write("So long lives this, and this gives life to thee.\n")
sonnet.close()

sonnet_lines = open("bar.txt")
for line in sonnet_lines:
    print(line)
sonnet_lines.close()
