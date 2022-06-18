import os

def numberlines():
  fileName = input("What is the input file called? ")
  fileCopy = input("What is the copy file called? ")

  if os.path.exists(fileCopy):
    print("\n" + fileCopy + ": File exists.")
  else:
    print("\nFilename", fileCopy, "has been created.")

  f = open(fileName, 'r')
  c = open(fileCopy, 'w')

  number = 0
  for line in f:
    number += 1
    c.write("%4s %s" % (str(number) + ">", line))
  f.close()
  c.close()

  print("\nContents of", fileName, "have been copied to", fileCopy, "and organized.")