def stringXOR(s1,s2):
	ls1 = list(s1)
	ls2 = list(s2)
	retString = ""
	if len(ls1) > len(ls2):
		while(True):
			if len(ls1) != len(ls2):
				ls2.append('0');
			else:
				break
	else:
		while(True):
			if len(ls1) != len(ls2):
				ls1.append('0');
			else:
				break
	for i in range(0,len(ls1)):
		if((ls1[i] == '0' and ls2[i] == '1') or (ls1[i] == '1' and ls2[i] == '0')):
			retString = retString + '1'
		else:
			retString = retString + '0'
	return retString
def stringAND(s1,s2):
	ls1 = list(s1)
	ls2 = list(s2)
	retString = ""
	if len(ls1) > len(ls2):
		while(True):
			if len(ls1) != len(ls2):
				ls2.append('0');
			else:
				break
	else:
		while(True):
			if len(ls1) != len(ls2):
				ls1.append('0');
			else:
				break
	for i in range(0,len(ls1)):
		if((ls1[i] == '1' and ls2[i] == '1')):
			retString = retString + '1'
		else:
			retString = retString + '0'
	return retString
def stringOR(s1,s2):
	ls1 = list(s1)
	ls2 = list(s2)
	retString = ""
	if len(ls1) > len(ls2):
		while(True):
			if len(ls1) != len(ls2):
				ls2.append('0');
			else:
				break
	else:
		while(True):
			if len(ls1) != len(ls2):
				ls1.append('0');
			else:
				break
	for i in range(0,len(ls1)):
		if((ls1[i] == '1' or ls2[i] == '1')):
			retString = retString + '1'
		else:
			retString = retString + '0'
	return retString
def stringNOT(s1):
	ls1 = list(s1)
	retString = ""
	for i in range(0,len(ls1)):
		if(ls1[i] == '0'):
			retString = retString + '1'
		elif(ls1[i] == '1'):
			retString = retString + '0'
	return retString
def stringADD(s1, s2):
	s1 = '0b'+s1
	s2 = '0b'+s2
	i1 = int(s1,2)
	i2 = int(s2,2)
	outInt = i1+i2
	outStr = bin(outInt)
	return outStr[2:]
def stringMULT(s1, s2):
	s1 = '0b'+s1
	s2 = '0b'+s2
	i1 = int(s1,2)
	i2 = int(s2,2)
	outInt = i1*i2
	outStr = bin(outInt)
	return outStr[2:]
def stringROT(s1, i1):

	slfs1 = s1[:i1%len(s1)]
	slbs1 = s1[i1%len(s1):]
	return slbs1+slfs1
def permute(state):
	statelen = len(state)
	'''
	Sorry about the variable names. You write like an asshole at 1:30 am.
	state is a binary string of length statelen bits
	stateR1 is the first half of the state. R2 is the second. the R stands for row for some reason.
	stateR2 is preserved. 
	stateR1 is further split and arranged into a 3d construction of 
	(LxHxD) 2x2x(statelen/80) with L being Length, H being Hieght and D being Depth
	__________
	|    |	  |
	|  1 |  2 |     front view of the state. It extends 10 cells into the screen.
	|____|____|     the numbers give the stick number (that's what the S1, S2, S3, S4 mean in stateR1S[N])
	|    |    |
	|  3 |  4 |
	|____|____|
	'''
	storedstate = state
	stateR1 = state[:statelen/2]
	stateR2 = state[statelen/2:]
	stateR1S1 = stateR1[:statelen/8]
	stateR1S2 = stateR1[statelen/8:statelen/4]
	stateR1S3 = stateR1[statelen/4:statelen*3/8]
	stateR1S4 = stateR1[statelen*3/8:statelen/2]
	stateR1S1P = stringXOR(stringROT(stateR1S1,int(stateR1S1,2)), stateR1S2) #rotate each state row by its int value and xor it with its reading-wise neighbor (left to right, top to bottom looping)
	stateR1S2P = stringXOR(stringROT(stateR1S2,int(stateR1S2,2)), stateR1S3)
	stateR1S3P = stringXOR(stringROT(stateR1S3,int(stateR1S3,2)), stateR1S4)
	stateR1S4P = stringXOR(stringROT(stateR1S4,int(stateR1S4,2)), stateR1S1)
	stateR1S1 = stateR1S1P
	stateR1S2 = stateR1S2P
	stateR1S3 = stateR1S3P
	stateR1S4 = stateR1S4P
	lstateR1S1 = list(stateR1S1)
	lstateR1S2 = list(stateR1S2)
	lstateR1S3 = list(stateR1S3)
	lstateR1S4 = list(stateR1S4)
	lstateR1S1P = [None]*(statelen/8)
	lstateR1S2P = [None]*(statelen/8)
	lstateR1S3P = [None]*(statelen/8)
	lstateR1S4P = [None]*(statelen/8)
	for i in range(0, len(lstateR1S1)):    #travelling down the 2x2x10 state, twist each 2x2 'face' alternatingly counterclockwise or clockwise
		if i % 2 == 1:
			lstateR1S1P[i] = lstateR1S2[i]
			lstateR1S2P[i] = lstateR1S4[i]
			lstateR1S3P[i] = lstateR1S1[i]
			lstateR1S4P[i] = lstateR1S3[i]
		else:
			lstateR1S1P[i] = lstateR1S3[i]
			lstateR1S2P[i] = lstateR1S1[i]
			lstateR1S3P[i] = lstateR1S4[i]
			lstateR1S4P[i] = lstateR1S2[i]
	stateR1S1 = "".join(lstateR1S1P)
	stateR1S2 = "".join(lstateR1S2P)
	stateR1S3 = "".join(lstateR1S3P)
	stateR1S4 = "".join(lstateR1S4P)
	stateR1S1P = stateR1S3[::-1]		#similarly using the 2x2x10 state, rotate both the left 2x1x10 'sheet' vertically
	stateR1S3P = stateR1S1[::-1]
	stateR1S3P = stateR1S4[::-1]		#then do the bottom sheet (this one is 1x2x10) horizontally
	stateR1S4P = stateR1S3[::-1]
	stateR1S1 = stateR1S1P
	stateR1S2 = stateR1S2P
	stateR1S3 = stateR1S3P
	stateR1S4 = stateR1S4P
	stateR1S1P = stringXOR(stringROT(stateR1S1,int(stateR1S1,2)), stateR1S2)#one more XOR block
	stateR1S2P = stringXOR(stringROT(stateR1S2,int(stateR1S2,2)), stateR1S3)
	stateR1S3P = stringXOR(stringROT(stateR1S3,int(stateR1S3,2)), stateR1S4)
	stateR1S4P = stringXOR(stringROT(stateR1S4,int(stateR1S4,2)), stateR1S1) 
	stateR1S1 = stateR1S1P
	stateR1S2 = stateR1S2P
	stateR1S3 = stateR1S3P
	stateR1S4 = stateR1S4P
	stateR1 = stateR1S1+stateR1S2+stateR1S3+stateR1S4 #finalize the new stateR1
	state = stateR1+stringXOR(stateR1,stateR2) #concatenate with the stateR1 XOR stateR2
	state = stringXOR(state,storedstate) #finally, xor the resulting permuted state with the stored state
	#print state
	return state
#A couple of testing states
#state = '00101100101111010101100100100011000101000010101101011010111111111101110100111110' #80 bit random state
#state = '00101100101111010101100100100011000101000010101101011010111111111101110100111110'*20 #1600 bit semiordered state
#state = '0111100111011111101101111011000100100011111011101011110011001010101111111011110111010000010000111001001000011011100000101011000011001100101110000101000000010011110011000111011010100011000000101100010011111001000001001101101101101111110110000000011001010111011000101101010010011010000000000111000010110101100010010111001101100111110011001101100100011101100111100000011101111111001101110100010010110100000111110010010000011000000110000111001111101010001101011010110110001010010000111010000010001100111100000110100101100011000011100001011100001000000010000100011000000011100000001100101100110110001110001001011111111011100111100110111101110110000000101011111110010101100100101100100111101110110110010110001110100100001110110010101110010111110111110010011010111110010111111110010010101111001001110101111100011000100111000011011100110001110000011110101000001111111000111001110111010101000010010010111001000011101111000010101001000010100101010110011010101011011100101110010110011011011001000000011110000111111010000101101100011110100011101000111011010100110010100000111111010101110110010101000101110110010101010111011011001010010010110100100011000110100101001001101000101001110010110000010001111010100101111001111000111111111111100000110100010001111010010001011101000000101111011100011000010111000001111010001001001110001001101110100110110100110111111001111010001111011101001111111011111111000000101001100000110100010011010010100101110011010010101010101111110101100000000011000001010011000111001101010001110101110100101101010000011001110100111101101101100010000110110000111101111000111110111100100011100110'
#1600 bit random state
#state = '11101110111011101110111011101110111011101110111011101110111011101110111011101110' #80 bit ordered state
inMsg = raw_input('Message: ')
digestLen = int(raw_input('How long of a digest: '))
inMsg = ''.join(format(ord(x), 'b') for x in inMsg)
while(True):
	if len(inMsg)%1600!=0:
		inMsg=inMsg+'0'
	else:
		break
state = inMsg
#print state
storedstate = state
for i in range(0,40):
	state = stringXOR(state,permute(state))
#print state
lstoredstate = list(storedstate)
lstate = list(state)
counter = 0
for i in range(0,len(lstoredstate)):
	if lstate[i] == lstoredstate[i]:
		counter+=1
'''
print "Unchanged bits: "+str(counter)
print "Changed bits: "+str(len(lstoredstate)-counter)
print "For a total change of: " +str(100-(100*counter/len(lstoredstate))) +"%"
'''
digest = str('0x'+format(long(state[:digestLen],2),'02x'))
print digest
#note: permute function bitchange is approaching 50%!!!