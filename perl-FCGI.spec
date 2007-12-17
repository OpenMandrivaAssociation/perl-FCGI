%define modname	FCGI
%define name	perl-%{modname}
%define version	0.67
%define release %mkrel 6

Summary:	A Fast CGI module for Perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		Development/Perl
Source0:	%{modname}-%{version}.tar.bz2
URL:		http://cpan.valueclick.com/authors/id/SKIMO/
Requires:	perl
BuildRequires:	perl-devel

%description
This is a Fast CGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

See <http://www.fastcgi.com/> for more information about fastcgi.
Lincoln D. Stein's perl CGI module also contains some information
about fastcgi programming.

%prep
%setup -q -n %{modname}-%{version}
chmod 0644 LICENSE.TERMS

%build
# Choose not to build a pure Perl implementation
# (default answer [n] -> return)
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE.TERMS ChangeLog
%{_mandir}/*/*
%{perl_vendorarch}/FCGI*
%{perl_vendorarch}/auto/FCGI


