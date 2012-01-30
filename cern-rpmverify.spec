Name:		cern-rpmverify
Version:	1.0
Release:	1%{?dist}
Summary:	Logs warnings for modified files of an RPM and the RPM package that they belong.
Vendor:		CERN
Group:		System Enviroment/Base
License:	GPLv3
BuildArch:	noarch
URL:		http://www.cern.ch/security
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tool which looks for suspicious files by checking their hash with RPMso

%package cron
Summary:	cern-rpmverify cron job
Group:		System Enviroment/Base
Requires:	cern-rpmverify

%description cron
Cron job for cern-rpmverify

%prep
(cd %{_sourcedir}; tar --exclude .git -chf - *) | tar xf -

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -m 0700 cern-rpmverify %{buildroot}/usr/bin/
mkdir -p %{buildroot}/etc/cron.d
install -m 0640 cern-rpmverify.cron %{buildroot}/etc/cron.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/cern-rpmverify

%files cron
%defattr(-,root,root,-)
/etc/cron.d/cern-rpmverify.cron

%changelog
