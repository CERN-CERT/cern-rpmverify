#!/usr/bin/python

import os, sys, stat, errno, rpm, rpmverify

# Flags that are not defined in rpm-python.
# They are defined in lib/rpmcli.h
# Bit(s) for verifyFile() attributes.
#

RPMVERIFY_MD5 = 1 # 1 << 0 # /*!< from %verify(md5) */
RPMVERIFY_FILESIZE = 2 # 1 << 1 # /*!< from %verify(size) */
RPMVERIFY_LINKTO = 4 # 1 << 2 # /*!< from %verify(link) */
RPMVERIFY_MTIME = 32 # 1 << 5 # /*!< from %verify(mtime) */

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
			stat_result = os.stat(files[i])
		except:
			#stat failed, the file does not exist
			continue
	
		if stat.S_ISDIR(stat_result[stat.ST_MODE]):
			#skip directories
			continue
		elif stat.S_ISREG(stat_result[stat.ST_MODE]):
		        #regular file	
			#engage
	
			MD5Sums = header[rpm.RPMTAG_FILEMD5S]
        		inodes = header[rpm.RPMTAG_FILEINODES]
			fileSizes = header[rpm.RPMTAG_FILESIZES]
		        verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]

			if verifyFlags[i] & RPMVERIFY_MD5:
				print "file %s failed sha256 sum check %s" %(files[i], MD5Sums[i])
			
		elif stat.S_IFLNK(stat_result[stat.ST_MODE]):
			#soft link

		        verifyFlags = header[rpm.RPMTAG_FILEVERIFYFLAGS]

			#verify that it still points to the same file
			if verifyFlags[i] & RPMVERIFY_LINKTO:
				print "soft link %s points to another file" %(files[i])
		else:
			print "%s is unknown" %(files[i])




















