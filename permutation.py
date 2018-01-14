#sponge permutation function
import numpy as np
def concatBinary(*args):
	tempString = "0b"
	for binNum in args:
		tempString=tempString+str(binNum)
	return int(tempString,2)
message = raw_input("Enter the message to submit to the permutation function: ")
messageBytes = map(bin, bytearray(message))
print messageBytes
bytestring = ""
for i in messageBytes:
	bytestring = bytestring+str(i)[2:]
print "Pre pad length: "+str(len(bytestring))
for i in range(0,1600-len(bytestring)):
	bytestring=bytestring+"0"
print "Post pad length: "+str(len(bytestring))
bytestring = "0b"+bytestring
bytes = bin(int(bytestring,2))
stateArray = []
for i in list(bytes)[2:]:
	temp = "0b"+str(i)
	stateArray.append(int(i,2))
print stateArray
threeDimensionalStateArray = []
index = 0
for i in range(0,5):
	twoDimensionalStateArray = []
	for j in range(0,5):
		oneDimensionalStateArray = []
		for k in range(0,64):
			oneDimensionalStateArray.append(stateArray[index])
			index+=1
		twoDimensionalStateArray.append(oneDimensionalStateArray)
	threeDimensionalStateArray.append(twoDimensionalStateArray)
interactiveState = np.array(threeDimensionalStateArray)
print interactiveState.shape
print interactiveState
print bin(0b110010010 << 10)
