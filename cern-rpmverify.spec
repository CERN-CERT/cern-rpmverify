Name:		cern-rpmverify
Version:	4.2
Release:	1%{?dist}
Summary:	Logs warnings for modified files of an RPM and the RPM package that they belong
Vendor:		CERN
Group:		Applications/System
License:	GPLv2+
BuildArch:	noarch
URL:		http://www.cern.ch/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tgz

Requires:	python-psutil
%if 0%{?el6}
Requires:	python-argparse
%endif

%description
Checks the integrity of the files installed via RPM by comparing their
integrity to the RPM DB.

%prep

%setup -q

%build
%if 0%{?el6}
sed 's#/usr/bin/env python$#/usr/bin/env python2.6#' -i cern-rpmverify
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/etc/cron.d/
install -m 0700 cern-rpmverify %{buildroot}/usr/bin/
install -m 0644 cern-rpmverify.cron %{buildroot}/etc/cron.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/cern-rpmverify
/etc/cron.d/cern-rpmverify.cron

%changelog
* Wed Dec 06 2017 Vincent Brillault <vincent.brillault@cern.ch> - 4.2
- Fix deprecation warning for SLC6.9 (psutil)
* Fri Jun 13 2014 Vincent Brillault <vincent.brillault@cern.ch> - 4.1
- Improve logging
- PEP8 & other code cleaning
* Thu May 22 2014 Vincent Brillault <vincent.brillault@cern.ch> - 4.0
- Refactor code
- Add nice/ionice options
- Add signature verification
* Thu Jun 28 2012 Remi Mollon <Remi.Mollon@cern.ch> - 3.2
- added cron job
* Wed May 23 2012 Remi Mollon <Remi.Mollon@cern.ch> - 3.1
- changed packaging to be compliant to rpmlint
