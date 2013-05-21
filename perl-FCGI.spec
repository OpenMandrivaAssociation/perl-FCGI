%define	module	FCGI
%define	modver	0.74

Summary:	A Fast CGI module for Perl
Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	Distributable
Group:		Development/Perl
URL:		http://search.cpan.org/~flora/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/%{module}-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
This is a Fast CGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

See <http://www.fastcgi.com/> for more information about fastcgi.
Lincoln D. Stein's perl CGI module also contains some information
about fastcgi programming.

%prep
%setup -q -n %{module}-%{modver}
chmod 0644 LICENSE.TERMS

%build
# Choose not to build a pure Perl implementation
# (default answer [n] -> return)
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
%makeinstall_std

%files
%doc README LICENSE.TERMS ChangeLog
%{_mandir}/*/*
%{perl_vendorarch}/FCGI*
%{perl_vendorarch}/auto/FCGI

%changelog
* Thu Dec 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.740.0-4
- rebuild for new perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.740.0-3
+ Revision: 765235
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.740.0-2
+ Revision: 763745
- rebuilt for perl-5.14.x

* Thu Jan 12 2012 Oden Eriksson <oeriksson@mandriva.com> 0.740.0-1
+ Revision: 760486
- 0.74 (fixes CVE-2011-2766)

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.730.0-1
+ Revision: 682117
- update to new version 0.73

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.720.0-1
+ Revision: 677328
- update to new version 0.72

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.710.0-4
+ Revision: 667135
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.710.0-3mdv2011.0
+ Revision: 564433
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 555250
- rebuild

* Thu Apr 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.1
+ Revision: 530663
- update to 0.71

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.1
+ Revision: 526439
- update to 0.70

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.1
+ Revision: 506746
- update to 0.69

* Wed Jan 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.680.0-1mdv2010.1
+ Revision: 486779
- update to 0.68

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.670.0-1mdv2010.0
+ Revision: 407070
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.67-8mdv2009.0
+ Revision: 223717
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.67-7mdv2008.1
+ Revision: 151425
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - simplify buildrequires


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.67-6mdv2007.0
+ Revision: 108537
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-FCGI

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.67-5mdk
- Rebuild

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.67-4mdk 
- rebuild for new perl

