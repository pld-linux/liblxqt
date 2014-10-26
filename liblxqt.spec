#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt - libraries
Summary(pl.UTF-8):	lxqt - biblioteki
Name:		liblxqt
Version:	0.8.0
Release:	0.2
License:	LGPL
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lxqt/0.8.0/%{name}-%{version}.tar.xz
# Source0-md5:	67512eae6af364e8b53777dc14e800fd
URL:		http://www.lxqt.org/
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Gui-platform-directfb >= %{qtver}
BuildRequires:	Qt5Gui-platform-egl >= %{qtver}
BuildRequires:	Qt5Gui-platform-kms >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
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

%build
install -d build
cd build
%cmake \
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblxqt-qt5.so.*.*.*
%ghost %{_libdir}/liblxqt-qt5.so.0
%dir %{_datadir}/lxqt-qt5
%dir %{_datadir}/lxqt-qt5/translations
%dir %{_datadir}/lxqt-qt5/translations/liblxqt
%lang(ar) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_hu.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_sl.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_sr@latin.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/liblxqt/liblxqt_zh_TW.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt-qt5
%{_libdir}/liblxqt-qt5.so
%{_pkgconfigdir}/lxqt-qt5.pc
%{_datadir}/cmake/lxqt-qt5


