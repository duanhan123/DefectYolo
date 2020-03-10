import random
import os

def train_test_split(src,trainTextFile,valTextFile):
	files=os.listdir(src)
	random.shuffle(files)

	trainFiles=files[:281]
	valFiles=files[281:]


	l=len('../')

	with open(trainTextFile,'w+') as f:
		for file in trainFiles: f.write(src[l:]+'/'+file+'\n')

	with open(valTextFile,'w+') as f:
		for file in valFiles: f.write(src[l:]+'/'+file+'\n')


def main():
	train_test_split('../data/images','../data/train.txt','../data/val.txt')

	# trainDest='/home/neymar/Projects/Python/pytorch_custom_yolo_training/images/train'
	# validDest='/home/neymar/Projects/Python/pytorch_custom_yolo_training/images/val'
	# trainTextFile='../data/train.txt'
	# validTextFile='../data/val.txt'

	# tmpSrc='data/images/'
	# l=len(tmpSrc)

	# with open(trainTextFile,'r+') as f:
	# 	for line in f:
	# 		print(line) 
	# 		copyfile('../'+line.strip(),trainDest+'/'+line[l:].strip())

	# with open(validTextFile,'r+') as f:
	# 	for line in f:
	# 		print(line) 
	# 		copyfile('../'+line.strip(),validDest+'/'+line[l:].strip())

if __name__=='__main__': main()