Summary:	Draft Diff Tool
Name:		rfcdiff
Version:	1.41
Release:	%mkrel 1
Group:		Development/Other
License:	GPLv2+
URL:		http://tools.ietf.org/tools/rfcdiff/
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