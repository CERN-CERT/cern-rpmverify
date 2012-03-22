name      = cern-rpmverify

srcrpm: archive slc5 slc6

slc5:
	rpmbuild --define "_sourcedir ${PWD}" --define "_srcrpmdir ${PWD}" --define 'dist .slc5' -bs $(name).spec

slc6:
	rpmbuild --define "_sourcedir ${PWD}" --define "_srcrpmdir ${PWD}" --define 'dist .slc6' -bs $(name).spec

archive: 
	rm -f $(name).tar.gz
	tar --exclude .git --exclude *.rpm --exclude $(name).spec -zchf $(name).tar.gz *
