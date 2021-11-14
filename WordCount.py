def CountWords():
    FileName=input("Enter File Name")
    NumberOfWords=0
    File=open(FileName,'r')
    for line in File:
        words=line.split()
        NumberOfWords=NumberOfWords+len(words)
    print("Number Of Words: ")
    print(NumberOfWords)

CountWords()