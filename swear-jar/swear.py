import sys
import os
import subprocess

def censor(file):
    swears = ["shit", "piss", "fuck", "cunt","dick","pussy", "damn", "cocksucker", "motherfucker", "tits", "twat", "bitch", "ass", "faggot", "fag", "dyke", "cock", "asshole", "whore", "fucking", "fucker", "fuckin", "sgsrgdg"]
    length = len(swears)
    # Iterate over text file and if a swear is found, replace all letters but the first two with "*". Output updated file contents to a new "censored" file.
    with open(file, "r") as input:
        with open("censor.txt", "w+") as output:
            for line in input: 
                for word in line.split():
                    for i in range(length):
                        if word == swears[i]:
                            curse = list(word)
                            for j in range(len(curse)):
                                if j <= 1:
                                    output.write(curse[j])
                                else:    
                                    curse[j] = "*"
                                    output.write(curse[j])
                            output.write(" ")
                            break
                        elif i == (length - 1):
                            output.write(word + " ")
                        else:                          
                            continue
            output.seek(0)
            print(output.read())                    
    input.close()
    output.close()
    subprocess.call(["xdg-open", "censor.txt"])

def main():

    swears = ["shit", "piss", "fuck", "cunt","dick","pussy", "damn", "cocksucker", "motherfucker", "tits", "twat", "bitch", "ass", "faggot", "fag", "dyke", "cock", "asshole", "whore", "fucking", "fucker", "fuckin", "sgsrgdg"]
    count = 0
    file = sys.argv[1]
    f = open(file, "r")
    # Iterate over text file and increment counter if a swear word is found
    for line in f: 
        for word in line.split():
            for i in range(len(swears)):
                if word == swears[i]:
                    count += 1
                    i += 1
                else:
                    i += 1
    f.seek(0)                
    og = f.read()      
    if count == 1:
        print("There is 1 swear word in this file\n")
    else:
        print("There are %d swear words in this file.\n" % count)
    print("Press F to display a censored version of the file or press Enter to view the file normally. Press Q to quit\n")
    a = input()
    if a == "Q" or a == "q":
        f.close()
        quit
    elif a == '':
        print(og)
        f.close()
    elif a == "f" or a == "F":
        f.close()
        censor(file)
    else:
        print("invalid entry")

    

if __name__ == "__main__" :
    main()