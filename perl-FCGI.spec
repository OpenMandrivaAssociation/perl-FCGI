%define upstream_name	 FCGI
%define upstream_version 0.74

Summary:	A Fast CGI module for Perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	Distributable
Group:		Development/Perl
URL:		http://search.cpan.org/~flora/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

%description
This is a Fast CGI module for perl. It's based on the FCGI module that
comes with Open Market's FastCGI Developer's Kit, but does not require
you to recompile perl.

See <http://www.fastcgi.com/> for more information about fastcgi.
Lincoln D. Stein's perl CGI module also contains some information
about fastcgi programming.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 0644 LICENSE.TERMS

%build
# Choose not to build a pure Perl implementation
# (default answer [n] -> return)
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%files
%doc README LICENSE.TERMS ChangeLog
%{_mandir}/*/*
%{perl_vendorarch}/FCGI*
%{perl_vendorarch}/auto/FCGI
