import os, sys, time, threading, multiprocessing, shutil

class my_dictionary(dict):
 
    # __init__ function
    def __init__(self):
        self = dict()
         
    # Function to add key:value
    def add(self, key, value):
        self[key] = value

# Main Function
timer = my_dictionary()

activeThreads = threading.activeCount()
print("Active Threads = ",activeThreads)

numberOfCores=multiprocessing.cpu_count()
print("Number Of Cores = ",numberOfCores)



totalFiles = 100


from PIL import Image

inputDirName='' #enter address for input dir
outputDirName=''  #enter name for output dir

try:
    # Delete output directory and then create it
    shutil.rmtree("./%s/"%(outputDirName))
    os.mkdir(outputDirName)
except:
    # Create the output directory
    os.mkdir(outputDirName)

def grayscaleConvert(fileName):
    inputfileName=inputDirName+"/"+fileName
    outputFileName="./"+outputDirName+"/"+fileName
    img = Image.open(inputfileName)
    img = img.convert("L")
    img.save(outputFileName)

def timetaken(N):
    startTime=time.time()
    for i in range(totalFiles):
        fN="cat."+str(i+4001)+".jpg" #filename as string
        t = threading.Thread(target=grayscaleConvert , args=(fN,))
        t.start()
        while True:
            if threading.activeCount() - activeThreads + 1 <= N:
                break
            time.sleep(1)
        print ("thread started for ",fN)


    while True:
        if threading.activeCount() == activeThreads:
            break
        else:
            print ("...Thread Left %d..."%(threading.activeCount() - activeThreads))
            time.sleep(1)

    length=str(round(time.time() - startTime,2))

    timer.add(N, length)

for i in range(1,25):
    timetaken(i)

import matplotlib.pyplot as plt

for x, y in timer.items():
    print(int(x),float(y))
    plt.bar(int(x),float(y))

# naming the x axis
plt.xlabel('number of threads')
# naming the y axis
plt.ylabel('time in seconds')
 
# giving a title to my graph
plt.title('multithreading')
 
# function to show the plot

plt.show()
