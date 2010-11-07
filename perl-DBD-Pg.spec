%define	upstream_name	 DBD-Pg
%define upstream_version 2.17.1

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	PostgreSQL database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:   perl-DBD-Pg-bug-60200.patch
Buildrequires:	chrpath
Buildrequires:	perl(DBI)
Buildrequires:	perl-devel
Buildrequires:	postgresql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PostgreSQL database driver for the DBI module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
export POSTGRES_INCLUDE=/usr/include
export POSTGRES_LIB=%{_libdir}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
chmod 755 %{buildroot}%{perl_vendorarch}/auto/DBD/Pg/Pg.so
chrpath -d %{buildroot}%{perl_vendorarch}/auto/DBD/Pg/Pg.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/auto/DBD
%{perl_vendorarch}/DBD
%{perl_vendorarch}/Bundle
%{_mandir}/*/*
