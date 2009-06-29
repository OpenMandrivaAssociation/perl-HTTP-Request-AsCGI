%define	module	HTTP-Request-AsCGI
%define	name	perl-%{module}
%define	modprefix HTTP
%define	version	0.9
%define	release	%mkrel 2

Summary:	Setup a CGI enviroment from a HTTP::Request
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
# http://search.cpan.org/src/CHANSEN/HTTP-Request-AsCGI-0.5/META.yml:
#     HTTP::Response:                1.53
# http://search.cpan.org/src/GAAS/libwww-perl-5.804/lib/HTTP/Response.pm = 1.52
Requires:	perl(Class::Accessor)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response) >= 1.53
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-libwww-perl >= 5.805
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a convenient way of setting up an CGI enviroment
from an HTTP::Request object.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes examples
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

