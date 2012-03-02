name      = cern-rpmverify

srcrpm: archive
	rpmbuild --define "_sourcedir ${PWD}" --define "_srcrpmdir ${PWD}" -bs $(name).spec

archive: 
	rm -f $(name).tar.gz
	tar --exclude .git --exclude *.rpm --exclude $(name).spec -zchf $(name).tar.gz *
