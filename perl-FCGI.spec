%define	module	FCGI
%define	modver	0.82

%ifarch %{x86_64}
# Workaround for bug in debugsource generator
%global _debugsource_template %{nil}
%endif

Summary:	A Fast CGI module for Perl
Name:		perl-%{module}
Version:	%perl_convert_version %{modver}
Release:	1
License:	Distributable
Group:		Development/Perl
Url:		https://metacpan.org/dist/FCGI
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
This is a Fast CGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

See <http://www.fastcgi.com/> for more information about fastcgi.
Lincoln D. Stein's perl CGI module also contains some information
about fastcgi programming.

%prep
%setup -qn %{module}-%{modver}
chmod 0644 LICENSE META.json META*

%build
# Choose not to build a pure Perl implementation
# (default answer [n] -> return)
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make_build

%install
%make_install

%files
%doc ChangeLog META* README
%{perl_vendorarch}/FCGI*
%{perl_vendorarch}/auto/FCGI
%{_mandir}/man3/*
