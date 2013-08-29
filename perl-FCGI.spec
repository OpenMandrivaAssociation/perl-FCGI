%define	module	FCGI
%define	modver	0.74

Summary:	A Fast CGI module for Perl
Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	Distributable
Group:		Development/Perl
Url:		http://search.cpan.org/~flora/
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
%setup -qn %{module}-%{modver}
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
%{perl_vendorarch}/FCGI*
%{perl_vendorarch}/auto/FCGI
%{_mandir}/man3/*

