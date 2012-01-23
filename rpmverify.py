#!/usr/bin/python

import os, sys, stat 
import rpm

transactionSet = rpm.TransactionSet()
headers = transactionSet.dbMatch()

for header in headers:
	files = header[rpm.RPMTAG_FILENAMES]
	MD5sums = header[rpm.RPMTAG_FILEMD5S]
	flags = header[rpm.RPMTAG_FILEFLAGS]
	inodes = header[rpm.RPMTAG_FILEINODES]
	print inodes

	for i in range(len(files)):
		stat_result = os.stat(files[i])		
		
		if stat.S_ISDIR(stat_result[stat.ST_MODE]):
			#skip directories
			continue
		elif stat.S_ISREG(stat_result[stat.ST_MODE]):
			print "%s with MD5 sum %s" %(files[i], MD5sums[i])
		else:
			print "Skipping %s. Unknown file" %(files[i])
	break
