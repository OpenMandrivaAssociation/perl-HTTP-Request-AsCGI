%define	upstream_name	 HTTP-Request-AsCGI
%define upstream_version 1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:	Setup a CGI enviroment from a HTTP::Request
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
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
BuildRequires:	perl-devel

BuildArch:	noarch

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
%makeinstall_std

%files 
%doc README Changes examples
%{perl_vendorlib}/HTTP
%{_mandir}/*/*


%changelog
* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 490487
- update to 1.2

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 472241
- update to 1.0

* Mon Nov 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.1
+ Revision: 469245
- rebuild using %%perl_convert_version

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-2mdv2010.0
+ Revision: 390766
- fix dependencies

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdv2010.0
+ Revision: 370131
- update to new version 0.9

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.5-7mdv2009.0
+ Revision: 257251
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-5mdv2008.1
+ Revision: 136998
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:20:57 (60027)
- whitespace changed to fix mixed-use-of-spaces-and-tabs

* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:17:13 (60025)
- spec file cleanup
- bump release for rebuild

* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:10:48 (60024)
Import perl-HTTP-Request-AsCGI

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.5-3mdk
- Updated BuildRequires
- Updated to comply with Mandriva perl packaging policies

* Mon Mar 06 2006 Buchan Milne <bgmilne@mandriva.org> 0.5-2mdk
- buildrequire newer perl-libwww-perl (aid backport)

* Wed Jan 25 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.5-1mdk
- 0.5

* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.3-1mdk
- 0.3

* Tue Dec 20 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.2-4mdk
- Fix BuildRequires

* Tue Dec 20 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.2-3mdk
- Fix BuildRequires

* Mon Dec 19 2005 Buchan Milne <bgmilne@mandriva.org> 0.2-2mdk
- Rebuild
- use mkrel

* Sat Dec 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.2-1mdk
- Initial MDV package

