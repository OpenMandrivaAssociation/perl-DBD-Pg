%define	module	DBD-Pg
%define	name	perl-%{module}
%define	version	2.0.0
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PostgreSQL database driver for the DBI module
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
Buildrequires:	perl(DBI)
Buildrequires:	perl-devel
Buildrequires:	postgresql-devel
Buildrequires:	rpath
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PostgreSQL database driver for the DBI module

%prep
%setup -q -n %{module}-%{version}
rm -f t/00-signature.t

%build
export POSTGRES_INCLUDE=/usr/include/pgsql
export POSTGRES_LIB=%{_libdir}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
chrpath -d %{buildroot}%{perl_vendorarch}/auto/DBD/Pg/Pg.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/auto/DBD
%{perl_vendorarch}/DBD
%{_mandir}/*/*


