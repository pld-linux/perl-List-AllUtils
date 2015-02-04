#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	List
%define		pnam	AllUtils
%include	/usr/lib/rpm/macros.perl
Summary:	List::AllUtils - combines List::Util and List::MoreUtils in one bite-sized package
Summary(pl.UTF-8):	List::AllUtils - połączenie List::Util oraz List::MoreUtils w jednym bałym pakiecie
Name:		perl-List-AllUtils
Version:	0.09
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e2dfeeef80c4e1952443c6b7d48583c
URL:		http://search.cpan.org/dist/List-AllUtils/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils >= 0.28
BuildRequires:	perl-Scalar-List-Utils >= 1.31
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Warnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Are you sick of trying to remember whether a particular helper is
defined in List::Util or List::MoreUtils? I sure am. Now you
don't have to remember. This module will export all of the functions
that either of those two modules defines.

%description -l pl.UTF-8
Jesteś zmęczony pamiętaniem, czy jakaś funkcja pomocnicza jest
zdefiniowana w List::Util, czy List::MoreUtils? Ja tak. Teraz nie
musisz pamiętać. Ten moduł eksportuje wszystkie funkcje definiowane
przez dowolny z tych dwóch modułów.

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
