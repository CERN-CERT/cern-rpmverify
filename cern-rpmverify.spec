Name:		cern-rpmverify
Version:	3.0
Release:	1%{?dist}
Summary:	Logs warnings for modified files of an RPM and the RPM package that they belong.
Vendor:		CERN
Group:		System Enviroment/Base
License:	GPLv3
BuildArch:	noarch
URL:		http://www.cern.ch/security
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0: 	cern-rpmverify.tar.gz

%description
Tool which looks for suspicious files by checking their hash with RPMso

%prep
#(cd %{_sourcedir}; tar --exclude .git -chf - *) | tar xf -
tar zxf %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -m 0700 cern-rpmverify %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/cern-rpmverify

%changelog
