%define	LADRver	2009-02A
Summary:	Library for Automated Deduction Research
Name:		LADR
Version:	%(echo %{LADRver} | tr '-' .)
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.cs.unm.edu/~mccune/mace4/download/%{name}-%{LADRver}.tar.gz
# Source0-md5:	f37a5304737ea2b14caf90d0a784964e
Source1:	%{name}-libtoolize
URL:		http://www.cs.unm.edu/~mccune/mace4/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

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
Summary:	-
Summary(pl.UTF-8):	-
Group:		-

%description -n prover9

%description -n prover9 -l pl.UTF-8

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libladr.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libladr.so.4

#%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_includedir}/ladr
%{_libdir}/libladr.la
%attr(755,root,root) %{_libdir}/libladr.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libladr.a

%files -n prover9
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}-ext
