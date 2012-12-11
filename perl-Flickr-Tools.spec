%define upstream_name    Flickr-Tools
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A set of classes that can be used to work with Flickr
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/N/NF/NFMNUNES/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Flickr::API)
BuildRequires:	perl(Test::MockObject)
BuildArch:	noarch

%description
These modules provide a set of classes that can be used to work with
Flickr, using it's REST API, as provided by the Flickr::API.

The object of this set of classes is to take the "raw" interface that
the Flickr::API provides and turn it into a more usable set of objects
which are easier and faster to use, while providing full access to all
the functionality provided by Flickr.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes TODO
%{perl_vendorlib}/Flickr/API/*.pm
%{perl_vendorlib}/Flickr/*.pm
%{_mandir}/man3/Flickr::*

%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 409308
- rebuild using %%perl_convert_version

* Mon Oct 13 2008 Nicolas Vigier <nvigier@mandriva.com> 0.02-1mdv2009.1
+ Revision: 293346
- import perl-Flickr-Tools


