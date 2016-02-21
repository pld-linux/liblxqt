#
# Conditional build:
#
%define		qtver		5.5.1

Summary:	lxqt - libraries
Summary(pl.UTF-8):	lxqt - biblioteki
Name:		liblxqt
Version:	0.10.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3856e2e690612c5564dc52f5b570a438
Patch0:		lxqt_share_dir.patch
URL:		http://www.lxqt.org/
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Gui-platform-directfb >= %{qtver}
BuildRequires:	Qt5Gui-platform-egl >= %{qtver}
BuildRequires:	Qt5Gui-platform-eglfs-kms >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt - libraries.

%package devel
Summary:	liblxqt - header files and development documentation
Summary(pl.UTF-8):	liblxqt - pliki nagłówkowe i dokumentacja do lxqt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5DBus-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DLXQT_ETC_XDG_DIR=/etc/xdg \
    ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%attr(755,root,root) %{_libdir}/liblxqt.so.*.*.*
%ghost %{_libdir}/liblxqt.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt
%{_libdir}/liblxqt.so
%{_pkgconfigdir}/lxqt.pc
%{_datadir}/cmake/lxqt
