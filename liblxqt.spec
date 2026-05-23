#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Core shared library for LXQt desktop suite
Summary(pl.UTF-8):	Podstawowa biblioteka współdzielona dla LXQt Desktop Suite
Name:		liblxqt
Version:	2.4.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	https://github.com/lxqt/liblxqt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	daa81b9deda0ac4c37ab3ec914bae82b
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	libqtxdg-devel >= 4.4.0
BuildRequires:	lxqt-build-tools >= 2.4.0
BuildRequires:	polkit-qt6-1-devel
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core utility library for all LXQT components

%description -l pl.UTF-8
Podstawowa biblioteka narzędzi dla wszystkich komponentów LXQT

%package devel
Summary:	liblxqt - header files and development documentation
Summary(pl.UTF-8):	liblxqt - pliki nagłówkowe i dokumentacja do lxqt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qtver}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Widgets-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

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
%attr(755,root,root) %{_bindir}/lxqt-backlight_backend
%dir %{_datadir}/lxqt
%{_datadir}/lxqt/power.conf
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%{_libdir}/liblxqt.so.*.*.*
%ghost %{_libdir}/liblxqt.so.2
%{_datadir}/polkit-1/actions/org.lxqt.backlight.pkexec.policy

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt
%{_libdir}/liblxqt.so
%{_pkgconfigdir}/lxqt.pc
%{_datadir}/cmake/lxqt
