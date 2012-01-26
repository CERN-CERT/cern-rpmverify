#!/usr/bin/python

import os, sys, subprocess, re, rpm

out = subprocess.Popen(["rpm", "-V", "--all"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

output = out.communicate()[0]

configPattern = re.compile("^[SM5DLUGTP\.]*.*c \/", re.DOTALL)
missingPattern = re.compile("^missing")
checksumPattern = re.compile("^.*5.*(?P<file> \/.*)", re.DOTALL)

failedChecksumFiles = []

for line in output.split('\n'):
	line = line.strip()
	if configPattern.match(line):
		#skip configuration files
		continue
	elif missingPattern.match(line):
		#skip missing files
		continue
	elif checksumPattern.match(line):
		#checksum failure. report
		failedChecksumFiles.append(checksumPattern.search(line).group(1).strip())

#Get the rpm package names that these files belong to

transactionSet = rpm.TransactionSet()
headers = transactionSet.dbMatch()

for header in headers:
	for filename in header[rpm.RPMTAG_FILENAMES]:
		if filename in failedChecksumFiles:	
			print "File %s from package %s-%s-%s has been modified" %(filename, header[rpm.RPMTAG_NAME], 
								header[rpm.RPMTAG_VERSION], header[rpm.RPMTAG_RELEASE])

