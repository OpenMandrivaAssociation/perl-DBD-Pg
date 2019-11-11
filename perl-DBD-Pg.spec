%define	module	DBD-Pg
%define upstream_version 3.9.1

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	PostgreSQL database driver for the DBI module





License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
Buildrequires:	perl(DBI)
Buildrequires:	perl-devel
Buildrequires:	postgresql-devel

%description
PostgreSQL database driver for the DBI module

%prep
%setup -q -n %{module}-%{upstream_version}

%build
export POSTGRES_INCLUDE=/usr/include
export POSTGRES_LIB=%{_libdir}
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%{perl_vendorarch}/auto/DBD
%{perl_vendorarch}/DBD
%{perl_vendorarch}/Bundle
%{_mandir}/*/*







