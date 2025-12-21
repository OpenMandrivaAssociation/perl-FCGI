%undefine _debugsource_packages

%define	module	FCGI
%define	version	0.82

Summary:	A Fast CGI module for Perl
Name:		perl-%{module}
Version:	0.82
Release:	3
License:	Distributable
Group:		Development/Perl
Url:		https://metacpan.org/dist/FCGI
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel

# **** perl_convert_version
Obsoletes:	%{name} = 0.820.0-1

%description
This is a Fast CGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

See <http://www.fastcgi.com/> for more information about fastcgi.
Lincoln D. Stein's perl CGI module also contains some information
about fastcgi programming.

%prep
%autosetup -p1 -n %{module}-%{version}
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
