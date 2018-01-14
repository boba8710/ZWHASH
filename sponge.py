import argparse
import string
import random, time
def oldstringXOR(s1,s2):
	
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
def stringXOR(s1,s2):
	s1 = '0b1'+s1
	s2 = '0b1'+s2
	i1 = int(s1,2)
	i2 = int(s2,2)
	finint = i1^i2
	finout = bin(finint)[3:]
	while(True):
		if len(finout) != len(s1):
			finout = '0'+finout
		else:
			break
	return finout[3:]
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
def pad(s1,i1):
	while(True):
		if len(s1)%i1 != 0:
			s1 = s1+'0'
		else:
			return s1
def spongehash(msg,rlen,hashlen):
	if hashlen>1600:
		return "error: requested larger hashsize than state"
	msg=''.join(format(ord(x), 'b') for x in msg)
	state = "0"*1600
	msg = msg+'1'
	msg = pad(msg,rlen)
	it = 1
	while(True):
		capacity = state[rlen:]
		rp = stringXOR(state[:rlen],msg[:rlen*it])
		state = rp+capacity
		for stateit in range(0,24):
			state = permute(state)
		if(rlen*it == len(msg)):
			break
		it+=1
	return state[:hashlen]
	
#parser = argparse.ArgumentParser(description='Hash an input message')
#parser.add_argument('message', metavar='inMsg',help='The message to be hashed')
#args = parser.parse_args()

#inMsg = args.message
#digestLen = 256

	
print(hex(int(spongehash(raw_input("inmsg: "),400,256),2)))[:-1]