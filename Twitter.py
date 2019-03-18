import string
import operator
import sys
import pdb

FILE_PATH=''
N=0
def inputPath():
    INPUTFILE = input("Input File location ")
    FILE_PATH = INPUTFILE+ '.txt'
    z=input("No. of record: ")
    N=int(z)
    return FILE_PATH,z
    
def Most_Number_of_Tweets(FILE_PATH,z):
    N=int(z)
    with open (FILE_PATH, encoding = "latin-1") as myFile:
        twitter=myFile.readlines()
    arr = {}
    for dat in twitter:
       
        temp = dat.split()
        if temp[0] in arr:
            arr[temp[0]] +=1
        else:
            arr[temp[0]] = 1
    arr = sorted(arr.items(), key = operator.itemgetter(1), reverse = True)
 
    outputFile = open('/Users/pratikkontamwar/Most_Number_of_Tweets.txt', 'w', encoding = "utf-8")
    outputFile.write( z + " users whose tweet count is most: \n")
    for i in range (0,N):
        outputFile.write("User " + arr[i][0] + " tweeted for" + str(arr[i][1]) + " times" + "\n")
        
    outputFile.close
    
def n_Count_of_retweet(FILE_PATH,z):
    N=int(z)
    with open (FILE_PATH, encoding = "latin-1") as myFile:
        twit=myFile.readlines()

    g = {}
    for dat in twit:
  
        temp = dat.split()
        #pdb.set_trace()
        #print(len(temp))
        y = len(temp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += temp[x] + " "
        tweet += " ::::;:::: " + temp[0]
  
        if tweet not in g:
            g[tweet] = int(temp[-1])
    #pdb.set_trace()
    outputFile = open('/Users/pratikkontamwar/n_Count_of_retweet.txt', 'w', encoding = "utf-8")
    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)
    outputFile.write(z + "users whose tweets have max retweet: " + "\n\n")

    for x in range (0, N):
        outputFile.write("\n Tweet: " +
                      g[x][0].split("::::;::::")[0]  + "\n\n")

def n_users_tweeted_per_hour(FILE_PATH,z):
    N=int(z)
    with open (FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    g = {}
    for dat in data:
        temp = dat.split()
        fileTemp2 = temp[1].split(":")
        twitTemp = temp[0] + " " + fileTemp2[1]
        if twitTemp in g:
            g[twitTemp]+=1
        else:
            g[twitTemp]=1
    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)

    g2={}
    totalUsersIn = 0
    for dat in g:
        totalUsersIn+=1
        if(dat[0].split()[1]) in g2:
            g2[dat[0].split()[1]]+=1
        else:
            g2[dat[0].split()[1]]=1
    g2 = sorted(g2.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = N*len(g2)
    outputFile = open('/Users/pratikkontamwar/n_users_tweeted_per_hour.txt', 'w', encoding = "utf-8")
   
    outputFile.write(z + " users who have tweeted the most in everyhour: " + "\n\n")
    for x in range (0,len(g2)):
   
        mSearch = N
        
       
        for dat in g:
            if mSearch == 0:
                break
            if dat[0].split()[1] == g2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n\n")
                
                mSearch-=1
    outputFile.close
    


def n_number_of_Followers_tweeted(FILE_PATH,z):
    N=int(z)
    with open (FILE_PATH, encoding = "latin-1") as myFile:
        twitter=myFile.readlines()

    arr = {}
    for dat in twitter:
        temp = dat.split()
        if temp[0] not in arr:
            arr[temp[0]] = int(temp[-2])

    arr = sorted(arr.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open('/Users/pratikkontamwar/n_number_of_Followers_tweeted.txt', 'w', encoding = "utf-8")
    outputFile.write(z + "users whoo have the maximum followers: " + "\n\n")

    for i in range (0, N):
        outputFile.write(str(i+1) + ". Username: " + arr[i][0] + " -> Follower count: " + str(arr[i][1]) + "\n\n")
    outputFile.close
    
f,z=inputPath()
n_Count_of_retweet(f,z)
Most_Number_of_Tweets(f,z)
n_number_of_Followers_tweeted(f,z)
n_users_tweeted_per_hour(f,z)
