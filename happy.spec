#% global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module happy
Name:           %{module}
Version:        1.18.10
Release:        5
Summary:        Parser generator for Haskell
Group:          Development/Other
License:        BSD
URL:            https://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
patch0:         happy-1.18.10.userhooks.patch

BuildRequires:  ghc, ghc-devel, haskell-macros
buildrequires:  haskell(mtl)

%description
Happy is a parser generator system for Haskell, similar to the tool
`yacc' for C. Like `yacc', it takes a file containing an annotated BNF
specification of a grammar and produces a Haskell module containing a
parser for the grammar.

Happy is flexible: you can have several Happy parsers in the same
program, and several entry points to a single grammar. Happy can work
in conjunction with a lexical analyser supplied by the user (either
hand-written or generated by another program), or it can parse a
stream of characters directly (but this isn't practical in most
cases).

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .userhooks

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_bindir}/%{module}
%{_datadir}/%{module}-%{version}
%{_docdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files


%changelog
* Mon Aug 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.18.5-1mdv2011.0
+ Revision: 572239
- Update to 1.18.5

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1.18.4-1mdv2010.1
+ Revision: 503519
- New version 1.18.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.17-3mdv2009.0
+ Revision: 267072
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Thierry Vignaud <tv@mandriva.org> 1.17-2mdv2009.0
+ Revision: 217022
- remove authors from description

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 1.17-1mdv2009.0
+ Revision: 213909
- New version 1.17

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 26 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.16-1mdv2008.0
+ Revision: 71545
- 1.16

  + Pixel <pixel@mandriva.com>
    - Import happy



* Mon Oct 03 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.15-3mdk
- Fix BuildRequires

* Mon Oct 03 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.15-2mdk
- BuildRequires fix
- Remove redundant buildrequires :
	- libxml2 is required by libxslt-proc

* Wed Jun 15 2005 Gaetan Lehmann <glehmann@deborah.mandrakesoft.com> 1.15-1mdk
- initial contrib

* Fri Jan 21 2005 Jens Petersen <petersen@haskell.org> - 1.15-2
- initial packaging based on spec file from tarball
- setup libdir for x86_64
