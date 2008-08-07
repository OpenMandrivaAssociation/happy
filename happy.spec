Name:           happy
Version:        1.17
Release:        %mkrel 3
License:        BSD-like
Group:          Development/Other
URL:            http://haskell.org/happy/
Source:         http://www.haskell.org/happy/dist/%{version}/happy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ghc
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt-proc
BuildRequires:  gmp-devel
#libxslt1
Summary:        The LALR(1) Parser Generator for Haskell

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


# the debuginfo subpackage is currently empty anyway, so don't generate it
%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress

%prep
%setup -q

%build

runhaskell Setup.lhs configure --prefix=%{_prefix}  --libdir=%{_libdir}
runhaskell Setup.lhs build
cd doc
test -f configure || autoreconf
./configure
make html

%install
rm -rf ${RPM_BUILD_ROOT}

runhaskell Setup.lhs copy --destdir=${RPM_BUILD_ROOT}

rm -fr %buildroot%_datadir/doc/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%defattr(-,root,root)
%doc ANNOUNCE
%doc CHANGES
%doc LICENSE
%doc README
%doc TODO
%doc doc/happy
%doc examples
%{_bindir}/happy
%{_datadir}/happy-%{version}
