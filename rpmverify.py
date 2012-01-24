#!/usr/bin/python

import os, sys, stat, errno, rpm

# Flags that are not defined in rpm-python.
# They are defined in lib/rpmcli.h
# Bit(s) for verifyFile() attributes.

RPMVERIFY_MD5 = 1 # 1 << 0 #
RPMVERIFY_FILESIZE = 2 # 1 << 1 #
RPMVERIFY_LINKTO = 4 # 1 << 2 #
RPMVERIFY_MTIME = 32 # 1 << 5 #

S_IXUSR = 00100
S_IXGRP = 00010
S_IXOTH = 00001

def HasExecuteRights(mode):
	return file_stat[stat.ST_MODE] & S_IXUSR or file_stat[stat.ST_MODE] & S_IXGRP or file_stat[stat.ST_MODE] & S_IXOTH

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
			file_stat = os.stat(files[i])
		except:
			#stat failed, the file does not exist
			continue
	
		if stat.S_ISDIR(file_stat[stat.ST_MODE]):
			#skip directories
			continue
		elif stat.S_ISREG(file_stat[stat.ST_MODE]):
		        #regular file	
			#engage
		
			if not HasExecuteRights(files[i]):
				#skip files with no execution mode. Less FP
				continue
				
			MD5Sums = header[rpm.RPMTAG_FILEMD5S]
        		inodes = header[rpm.RPMTAG_FILEINODES]
			fileSizes = header[rpm.RPMTAG_FILESIZES]
		        verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]

			if not verifyFlags[i] & RPMVERIFY_MD5 and len(MD5Sums[i]) != 0:
				print "file %s failed sha256 sum check %s" %(files[i], MD5Sums[i])
			
		elif stat.S_IFLNK(file_stat[stat.ST_MODE]):
			#soft link

		        verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]
	
			#verify that it still points to the same file
			if verifyFlags[i] & RPMVERIFY_LINKTO:
				print "link %s points to another file" %(files[i])

















