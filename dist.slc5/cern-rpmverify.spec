Name:		cern-rpmverify
Version:	3.1
Release:	1%{?dist}
Summary:	Logs warnings for modified files of an RPM and the RPM package that they belong.
Vendor:		CERN
Group:		System Enviroment/Base
License:	GPLv3
BuildArch:	noarch
URL:		http://www.cern.ch/security
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tgz

%description
Checks the integrity of the files installed via RPM by comparing their integrity to the RPM DB.

%prep

%setup -q

%build

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
