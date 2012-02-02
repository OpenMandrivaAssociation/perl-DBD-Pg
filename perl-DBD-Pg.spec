%define	module	DBD-Pg
%define	upstream_version 2.18.1

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	PostgreSQL database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/DBD/%{module}-%{upstream_version}.tar.gz
Patch0:		DBD-Pg-2.18.1-string-format-fix.patch
Buildrequires:	perl(DBI)
Buildrequires:	perl-devel
Buildrequires:	postgresql-devel

%description
PostgreSQL database driver for the DBI module

%prep
%setup -q -n %{module}-%{upstream_version}
%patch0 -p1 -b .str_fmt~

%build
export POSTGRES_INCLUDE=/usr/include
export POSTGRES_LIB=%{_libdir}
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/auto/DBD
%{perl_vendorarch}/DBD
%{perl_vendorarch}/Bundle
%{_mandir}/*/*
