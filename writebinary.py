from pickle import *
name=open("Sri.txt","wb")
sdata=["kumar","raja"]
cdata=["kumar","ganesh"]

dump=(sdata,name)
dump(cdata,name)
name.close()