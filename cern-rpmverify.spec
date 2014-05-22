Name:		cern-rpmverify
Version:	3.5
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
Requires:	python-argparse

%description
Checks the integrity of the files installed via RPM by comparing their
integrity to the RPM DB.

%prep

%setup -q

%build

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
* Thu Jun 28 2012 Remi Mollon <Remi.Mollon@cern.ch> - 3.2
- added cron job
* Wed May 23 2012 Remi Mollon <Remi.Mollon@cern.ch> - 3.1
- changed packaging to be compliant to rpmlint
