%define	module	DBD-Pg
%define	upstream_version 2.19.2

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	PostgreSQL database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/DBD/%{module}-%{upstream_version}.tar.gz
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


%changelog
* Thu Jul 26 2012 Oden Eriksson <oeriksson@mandriva.com> 2.19.2-2
+ Revision: 811051
- 2.19.2

* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.18.1-2
+ Revision: 770615
- apply string format fix
- remove no longer needed chrpath
- clean spec
- mass rebuild of perl extensions against perl 5.14.2

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.1-1
+ Revision: 673790
- update to new version 2.18.1

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.0-1
+ Revision: 649137
- update to new version 2.18.0

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.17.2-1mdv2011.0
+ Revision: 602040
- new version

* Sun Nov 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.17.1-2mdv2011.0
+ Revision: 594874
- Add patch to works with newer pgsql

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.17.1-1mdv2010.1
+ Revision: 536959
- update to 2.17.1

* Thu Jan 21 2010 Jérôme Quelin <jquelin@mandriva.org> 2.16.1-1mdv2010.1
+ Revision: 494440
- update to 2.16.1

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 2.16.0-1mdv2010.1
+ Revision: 480713
- update to 2.16.0

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 2.15.1-2mdv2010.0
+ Revision: 420360
- force rebuild
- update to 2.15.1

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 2.15.0-1mdv2010.0
+ Revision: 410152
- update to 2.15.0

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.13.1-1mdv2010.0
+ Revision: 371422
- new version

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.8-1mdv2009.1
+ Revision: 320931
- update to new version 2.11.8

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.7-1mdv2009.1
+ Revision: 314749
- update to new version 2.11.7

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.6-1mdv2009.1
+ Revision: 309301
- update to new version 2.11.6

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.5-1mdv2009.1
+ Revision: 307064
- update to new version 2.11.5

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.4-1mdv2009.1
+ Revision: 302819
- update to new version 2.11.4

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.3-1mdv2009.1
+ Revision: 299750
- update to new version 2.11.3

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.2-1mdv2009.1
+ Revision: 294627
- update to new version 2.11.2

* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.0-1mdv2009.1
+ Revision: 293567
- update to new version 2.11.0

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.10.7-1mdv2009.1
+ Revision: 292136
- update to new version 2.10.7

* Wed Sep 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.10.3-1mdv2009.0
+ Revision: 279699
- update to new version 2.10.3

* Fri Aug 29 2008 Olivier Thauvin <nanardon@mandriva.org> 2.10.0-1mdv2009.0
+ Revision: 277147
- 2.10

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.9.0-1mdv2009.0
+ Revision: 270350
- update to new version 2.9.0

* Fri Jul 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.7-1mdv2009.0
+ Revision: 248710
- update to new version 2.8.7

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.6-1mdv2009.0
+ Revision: 242060
- update to new version 2.8.6

* Tue Jul 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.5-1mdv2009.0
+ Revision: 235778
- update to new version 2.8.5

* Fri Jul 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.4-1mdv2009.0
+ Revision: 233649
- update to new version 2.8.4

* Tue Jul 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.3-1mdv2009.0
+ Revision: 232736
- update to new version 2.8.3

* Fri Jul 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.2-1mdv2009.0
+ Revision: 231883
- new version

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.1-1mdv2009.0
+ Revision: 218701
- update to new version 2.8.1

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.0-1mdv2009.0
+ Revision: 214605
- new version

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.2-1mdv2009.0
+ Revision: 208352
- update to new version 2.7.2

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.1-1mdv2009.0
+ Revision: 206817
- update to new version 2.7.1

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.6-1mdv2009.0
+ Revision: 205394
- update to new version 2.6.6

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.4-1mdv2009.0
+ Revision: 202318
- update to new version 2.6.4

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.1-1mdv2009.0
+ Revision: 196823
- update to new version 2.6.1

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-1mdv2009.0
+ Revision: 195436
- new version

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.1-1mdv2009.0
+ Revision: 193792
- update to new version 2.5.1

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-1mdv2008.1
+ Revision: 178291
- update to new version 2.2.2

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-1mdv2008.1
+ Revision: 177901
- update to new version 2.2.1

* Fri Feb 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 176706
- update to new version 2.2.0

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.3-1mdv2008.1
+ Revision: 173874
- update to new version 2.1.3

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.2-1mdv2008.1
+ Revision: 173533
- update to new version 2.1.2

* Wed Feb 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.1-1mdv2008.1
+ Revision: 173292
- update to new version 2.1.1

* Tue Feb 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2008.1
+ Revision: 166709
- nuke rpath
- update to new version 2.0.0

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.49-3mdv2008.1
+ Revision: 151344
- rebuild for perl-5.10.0

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.49-2mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

