#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Ethiopic
Summary:	Regexp::Ethiopic - regular expressions support for Ethiopic script
Summary(pl):	Regexp::Ethiopic - obs³uga wyra¿eñ regularnych dla pisma etiopskiego
Name:		perl-Regexp-Ethiopic
Version:	0.14
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	343e6728a374287cc9c520ecf94a204b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Regexp::Ethiopic module provides POSIX style character class
definitions for working with the Ethiopic syllabary. The character
classes provided by the Regexp::Ethiopic package correspond to inate
properties of the script and are language independent.

%description -l pl
Modu³ Regexp::Ethiopic dostarcza definicje klas znaków w stylu POSIX
dzia³aj±ce z etiopskim pismem sylabicznym. Klasy znaków dostarczone
przez pakiet Regexp::Ethiopic odpowiadaj± w³asno¶ciom pisma i s±
niezale¿ne od jêzyka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
