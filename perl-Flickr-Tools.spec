Name:		perl-Flickr-Tools
Summary:	A set of classes that can be used to work with Flickr
Version:	0.02
Release:	%mkrel 1
Group:		Development/Perl
License:	GPL or Artistic
Source:		http://search.cpan.org/CPAN/authors/id/N/NF/NFMNUNES/Flickr-Tools-0.02.tar.gz
BuildArch:	noarch
BuildRequires:	perl-Flickr-API
Requires:	perl
BuildRoot:	%{_tmppath}/%{name}-buildroot/
%description
These modules provide a set of classes that can be used to work with
Flickr, using it's REST API, as provided by the Flickr::API.

The object of this set of classes is to take the "raw" interface that
the Flickr::API provides and turn it into a more usable set of objects
which are easier and faster to use, while providing full access to all
the functionality provided by Flickr.

%prep
%setup -q -n Flickr-Tools-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes TODO
%{perl_vendorlib}/Flickr/API/*.pm
%{perl_vendorlib}/Flickr/*.pm
%{_mandir}/man3/Flickr::*
