Summary:	CELT low-latency audio codec v0.5.1
Summary(pl.UTF-8):	CELT - kodek dźwiękowy o małym opóźnieniu - wersja 0.5.1
Name:		celt051
Version:	0.5.1.3
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/celt/celt-%{version}.tar.gz
# Source0-md5:	67e7b5e45db57a6f1f0a6962f5ecb190
URL:		http://celt-codec.org/
# for tools
BuildRequires:	libogg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CELT is an attempt to write a low-latency audio codec.

This package contains 0.5.1 version of CELT codec, as used by SPICE
virtualization system.

%description -l pl.UTF-8
CELT to próba napisania kodeka dźwiękowego o małym opóźnieniu.

Ten pakiet zawiera wersję 0.5.1 kodeka CELT, używana przez system
wirtualizacji SPICE.

%package devel
Summary:	Header files for CELT 0.5.1 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CELT 0.5.1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CELT 0.5.1 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CELT 0.5.1.

%package static
Summary:	Static CELT 0.5.1 library
Summary(pl.UTF-8):	Statyczna biblioteka CELT 0.5.1
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CELT 0.5.1 library.

%description static -l pl.UTF-8
Statyczna biblioteka CELT 0.5.1.

%prep
%setup -q -n celt-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/celtdec051
%attr(755,root,root) %{_bindir}/celtenc051
%attr(755,root,root) %{_libdir}/libcelt051.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcelt051.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcelt051.so
%{_libdir}/libcelt051.la
%{_includedir}/celt051
%{_pkgconfigdir}/celt051.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcelt051.a
