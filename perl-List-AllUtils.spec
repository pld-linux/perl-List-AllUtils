#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	List
%define		pnam	AllUtils
Summary:	List::AllUtils - combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package
Summary(pl.UTF-8):	List::AllUtils - połączenie List::Util, List::SomeUtils oraz List::UtilsBy jednym bałym pakiecie
Name:		perl-List-AllUtils
Version:	0.15
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df17b5e9dbef488c72836298e2da221b
URL:		http://search.cpan.org/dist/List-AllUtils/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-SomeUtils >= 0.50
BuildRequires:	perl-List-UtilsBy >= 0.10
BuildRequires:	perl-Scalar-List-Utils >= 1.45
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Are you sick of trying to remember whether a particular helper is
defined in List::Util, List::SomeUtils or List::UtilsBy? I sure am.
Now you don't have to remember. This module will export all of the
functions that either of those three modules defines.

%description -l pl.UTF-8
Jesteś zmęczony pamiętaniem, czy jakaś funkcja pomocnicza jest
zdefiniowana w List::Util, List::SomeUtils czy List::UtilsBy? Ja tak.
Teraz nie musisz pamiętać. Ten moduł eksportuje wszystkie funkcje
definiowane przez dowolny z tych trzech modułów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/List/AllUtils.pm
%{_mandir}/man3/List::AllUtils.3pm*
