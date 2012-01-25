#!/usr/bin/python

import os, sys, stat, errno, rpm, hashlib

# Flags that are not defined in rpm-python.
# They are defined in lib/rpmcli.h
# Bit(s) for verifyFile() attributes.
#

RPMVERIFY_MD5 = 1 # 1 << 0 #
RPMVERIFY_FILESIZE = 2 # 1 << 1 #
RPMVERIFY_LINKTO = 4 # 1 << 2 #
RPMVERIFY_MTIME = 32 # 1 << 5 #

S_IXUSR = 00100
S_IXGRP = 00010
S_IXOTH = 00001

def HasExecuteRights(mode):
	return file_lstat[stat.ST_MODE] & S_IXUSR or file_lstat[stat.ST_MODE] & S_IXGRP or file_lstat[stat.ST_MODE] & S_IXOTH

def SHA256(filename):
	targetFile = open(filename, "r")
	sha256 = hashlib.sha256()
	sha256.update(targetFile.read())
	targetFile.close()
	return sha256.hexdigest()

transactionSet = rpm.TransactionSet()
headers = transactionSet.dbMatch()

#foreach header in the rpm database
for header in headers:
	#for each file in the rpm header
	files = header[rpm.RPMTAG_FILENAMES]

	for i in range(len(files)):
		#RPMTAG_FILEFLAGS related checks	
		fileFlags = header[rpm.RPMTAG_FILEFLAGS]

		if fileFlags[i] & rpm.RPMFILE_DOC:
			#skip doc files
			continue	
                if fileFlags[i] & rpm.RPMFILE_CONFIG:
                        #skip configuration files, they do change
                        continue
                if fileFlags[i] & rpm.RPMFILE_MISSINGOK:
                        #skip missing file
                        continue
		if fileFlags[i] & rpm.RPMFILE_README:
                        #skip readme file
                        continue

                try:
			file_lstat = os.lstat(files[i])
		except:
			#stat failed, the file does not exist
			continue
		
		if stat.S_ISDIR(file_lstat[stat.ST_MODE]):
			#skip directories
			continue
		elif stat.S_ISREG(file_lstat[stat.ST_MODE]):
		        #regular file	
			#engage
		
			if not HasExecuteRights(files[i]):
				#skip files with no execution mode. Less FP
				continue
				
			MD5Sums = header[rpm.RPMTAG_FILEMD5S]
        		inodes = header[rpm.RPMTAG_FILEINODES]
			fileSizes = header[rpm.RPMTAG_FILESIZES]
		        verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]
			
			if len(MD5Sums[i]) != 0:
				#check sha256 sum
				sha256 = SHA256(files[i])
				if MD5Sums[i] != sha256:
					print "%s SHA256 checksum missmatch inode %i size %i" %(files[i], inodes[i], fileSizes[i])
		elif stat.S_ISLNK(file_lstat[stat.ST_MODE]):
			#handle symbolic links
			continue	
		else:
			print "%s is unknown" %(files[i])

















