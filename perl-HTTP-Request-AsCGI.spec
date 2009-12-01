%define	upstream_name	 HTTP-Request-AsCGI
%define upstream_version 1.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Setup a CGI enviroment from a HTTP::Request
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

# http://search.cpan.org/src/CHANSEN/HTTP-Request-AsCGI-0.5/META.yml:
#     HTTP::Response:                1.53
# http://search.cpan.org/src/GAAS/libwww-perl-5.804/lib/HTTP/Response.pm = 1.52
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response) >= 1.530.0
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-libwww-perl >= 5.805.0

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(Class::Accessor)

%description
This module provides a convenient way of setting up an CGI enviroment
from an HTTP::Request object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes examples
%{perl_vendorlib}/HTTP
%{_mandir}/*/*
