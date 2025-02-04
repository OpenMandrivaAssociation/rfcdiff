Summary:	Draft Diff Tool
Name:		rfcdiff
Version:	1.41
Release:	3
Group:		Development/Other
License:	GPLv2+
URL:		https://tools.ietf.org/tools/rfcdiff/
Source0:	http://tools.ietf.org/tools/rfcdiff/rfcdiff-%{version}.tgz
Patch0:         rfcdiff-1.41.patch
BuildRequires:	txt2man
Requires:       wdiff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rfcdiff takes two RFCs or Internet-Drafts in text form as input, and
produces output which indicates the differences found in one of various
forms, controlled by a list of options. In all cases, page headers and
page footers are stripped before looking for changes.

%prep
%setup -q
%patch0 -p1

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1/
install %{name} %{buildroot}%{_bindir}
install -m 644 %{name}.1.gz %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc copyright
%{_mandir}/man1/*
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.41-2mdv2012.0
+ Revision: 772321
- Make HTML output to be valid, corrected font, corrected name of temp directory.

* Fri Dec 23 2011 Andrey Ponomarenko <andrey.ponomarenko@rosalab.ru> 1.41-1
+ Revision: 744816
- Initial package.
- Created package structure for rfcdiff.

