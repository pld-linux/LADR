#
# TODO:
#	- pl descriptions
#
%define	LADRver	2009-02A
Summary:	Library for Automated Deduction Research
Name:		LADR
Version:	%(echo %{LADRver} | tr '-' .)
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://www.cs.unm.edu/~mccune/mace4/download/%{name}-%{LADRver}.tar.gz
# Source0-md5:	f37a5304737ea2b14caf90d0a784964e
Source1:	%{name}-libtoolize
URL:		http://www.cs.unm.edu/~mccune/mace4/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LADR (Library for Automated Deduction Research) is a library for
use in constructing theorem provers.  Among other useful routines it
provides facilities for applying inference rules such as resolution
and paramodulation to clauses.  LADR is used by the prover9 theorem
prover, and by the mace4 countermodel generator.

%package devel
Summary:	Header files for LADR library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LADR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LADR library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LADR.

%package static
Summary:	Static LADR library
Summary(pl.UTF-8):	Statyczna biblioteka LADR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LADR library.

%description static -l pl.UTF-8
Statyczna biblioteka LADR.

%package -n prover9
Summary:	Theorem prover and countermodel generator
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description -n prover9
This package provides the Prover9 resolution/paramodulation theorem
prover and the Mace4 countermodel generator.

Prover9 is an automated theorem prover for first-order and equational
logic. It is a successor of the Otter prover.  Prover9 uses the
inference techniques of ordered resolution and paramodulation with
literal selection.

The program Mace4 searches for finite structures satisfying first-order
and equational statements, the same kind of statement that Prover9
accepts. If the statement is the denial of some conjecture, any
structures found by Mace4 are counterexamples to the conjecture.

Mace4 can be a valuable complement to Prover9, looking for
counterexamples before (or at the same time as) using Prover9 to search
for a proof. It can also be used to help debug input clauses and formulas
for Prover9.

%package apps
Summary:	The LADR deduction library, miscellaneous applications
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description apps
This package provides miscellaneous LADR applications.

%prep
%setup -q -n %{name}-%{LADRver}
install %{SOURCE1} Llibtoolize
./Llibtoolize --patch .

%build
%{__make} all \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/ladr} \
	$RPM_BUILD_ROOT%{_examplesdir}/prover9-%{version}

cp -a prover9.examples $RPM_BUILD_ROOT%{_examplesdir}/prover9-%{version}
cp -a mace4.examples $RPM_BUILD_ROOT%{_examplesdir}/prover9-%{version}

install ladr/*.h $RPM_BUILD_ROOT%{_includedir}/ladr

install bin/* $RPM_BUILD_ROOT%{_bindir}

libtool --mode=install --tag=CC cp -a ladr/libladr.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libladr.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libladr.so.4


%files devel
%defattr(644,root,root,755)
%doc ladr/html
%{_includedir}/ladr
%{_libdir}/libladr.la
%attr(755,root,root) %{_libdir}/libladr.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libladr.a

%files -n prover9
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/prover9
%attr(755,root,root) %{_bindir}/prooftrans
%attr(755,root,root) %{_bindir}/mace4
%attr(755,root,root) %{_bindir}/isofilter
%attr(755,root,root) %{_bindir}/isofilter0
%attr(755,root,root) %{_bindir}/isofilter2
%attr(755,root,root) %{_bindir}/interpformat
%{_examplesdir}/prover9-%{version}

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/attack
%attr(755,root,root) %{_bindir}/autosketches4
%attr(755,root,root) %{_bindir}/clausefilter
%attr(755,root,root) %{_bindir}/clausetester
%attr(755,root,root) %{_bindir}/complex
%attr(755,root,root) %{_bindir}/directproof
%attr(755,root,root) %{_bindir}/dprofiles
%attr(755,root,root) %{_bindir}/fof-prover9
%attr(755,root,root) %{_bindir}/get_givens
%attr(755,root,root) %{_bindir}/get_interps
%attr(755,root,root) %{_bindir}/get_kept
%attr(755,root,root) %{_bindir}/gvizify
%attr(755,root,root) %{_bindir}/idfilter
%attr(755,root,root) %{_bindir}/interpfilter
%attr(755,root,root) %{_bindir}/ladr_to_tptp
%attr(755,root,root) %{_bindir}/latfilter
%attr(755,root,root) %{_bindir}/looper
%attr(755,root,root) %{_bindir}/miniscope
%attr(755,root,root) %{_bindir}/mirror-flip
%attr(755,root,root) %{_bindir}/newauto
%attr(755,root,root) %{_bindir}/newsax
%attr(755,root,root) %{_bindir}/olfilter
%attr(755,root,root) %{_bindir}/perm3
%attr(755,root,root) %{_bindir}/renamer
%attr(755,root,root) %{_bindir}/rewriter
%attr(755,root,root) %{_bindir}/sigtest
%attr(755,root,root) %{_bindir}/tptp_to_ladr
%attr(755,root,root) %{_bindir}/unfast
%attr(755,root,root) %{_bindir}/upper-covers
