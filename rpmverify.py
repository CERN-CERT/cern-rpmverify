#!/usr/bin/python

import os, sys, stat 
import rpm

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
                        #skip doc file
                        continue

                stat_result = os.stat(files[i])

		if stat.S_ISDIR(stat_result[stat.ST_MODE]):
			#skip directories
			continue
		elif stat.S_ISREG(stat_result[stat.ST_MODE]):
		        #regular file	
	
			MD5sums = header[rpm.RPMTAG_FILEMD5S]
        		inodes = header[rpm.RPMTAG_FILEINODES]
        		verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]

			#engage
		
		elif stat.S_IFLNK(stat_result[stat.ST_MODE]):
			#soft link
			print "%s is a softlink" %(files[i])
		else:
			print "%s is unknown" %(files[i])












