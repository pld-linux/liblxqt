#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt - libraries
Summary(pl.UTF-8):	lxqt - biblioteki
Name:		liblxqt
Version:	0.7.0
Release:	0.1
License:	LGPL
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	cb026bd0cece2004b545fbe47fc7fe9c
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt - libraries.

%package devel
Summary:	liblxqt - header files and development documentation
Summary(pl.UTF-8):	liblxqt - pliki nagłówkowe i dokumentacja do lxqt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
%attr(755,root,root) %{_libdir}/liblxqt.so.*.*.*
%ghost %{_libdir}/liblxqt.so.0
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%lang(ar) %{_datadir}/lxqt/translations/liblxqt_ar.qm
%lang(cs) %{_datadir}/lxqt/translations/liblxqt_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt/translations/liblxqt_cs_CZ.qm
%lang(da) %{_datadir}/lxqt/translations/liblxqt_da.qm
%lang(da_DK) %{_datadir}/lxqt/translations/liblxqt_da_DK.qm
%lang(de) %{_datadir}/lxqt/translations/liblxqt_de.qm
%lang(de_DE) %{_datadir}/lxqt/translations/liblxqt_de_DE.qm
%lang(el) %{_datadir}/lxqt/translations/liblxqt_el_GR.qm
%lang(eo) %{_datadir}/lxqt/translations/liblxqt_eo.qm
%lang(es) %{_datadir}/lxqt/translations/liblxqt_es.qm
%lang(es_VE) %{_datadir}/lxqt/translations/liblxqt_es_VE.qm
%lang(eu) %{_datadir}/lxqt/translations/liblxqt_eu.qm
%lang(fi) %{_datadir}/lxqt/translations/liblxqt_fi.qm
%lang(fr) %{_datadir}/lxqt/translations/liblxqt_fr_FR.qm
%lang(hu) %{_datadir}/lxqt/translations/liblxqt_hu.qm
%lang(ia) %{_datadir}/lxqt/translations/liblxqt_ia.qm
%lang(id) %{_datadir}/lxqt/translations/liblxqt_id_ID.qm
%lang(it) %{_datadir}/lxqt/translations/liblxqt_it_IT.qm
%lang(ja) %{_datadir}/lxqt/translations/liblxqt_ja.qm
%lang(ko) %{_datadir}/lxqt/translations/liblxqt_ko.qm
%lang(lt) %{_datadir}/lxqt/translations/liblxqt_lt.qm
%lang(nl) %{_datadir}/lxqt/translations/liblxqt_nl.qm
%lang(pl) %{_datadir}/lxqt/translations/liblxqt_pl_PL.qm
%lang(pt) %{_datadir}/lxqt/translations/liblxqt_pt.qm
%lang(pt_BR) %{_datadir}/lxqt/translations/liblxqt_pt_BR.qm
%lang(ro) %{_datadir}/lxqt/translations/liblxqt_ro_RO.qm
%lang(ru) %{_datadir}/lxqt/translations/liblxqt_ru.qm
%lang(ru_RU) %{_datadir}/lxqt/translations/liblxqt_ru_RU.qm
%lang(sk) %{_datadir}/lxqt/translations/liblxqt_sk_SK.qm
%lang(sl) %{_datadir}/lxqt/translations/liblxqt_sl.qm
%lang(sl) %{_datadir}/lxqt/translations/liblxqt_sr@latin.qm
%lang(sr) %{_datadir}/lxqt/translations/liblxqt_sr_RS.qm
%lang(th) %{_datadir}/lxqt/translations/liblxqt_th_TH.qm
%lang(tr) %{_datadir}/lxqt/translations/liblxqt_tr.qm
%lang(uk) %{_datadir}/lxqt/translations/liblxqt_uk.qm
%lang(zh_CN) %{_datadir}/lxqt/translations/liblxqt_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt/translations/liblxqt_zh_TW.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt
%{_libdir}/liblxqt.so
%{_pkgconfigdir}/lxqt.pc
%{_datadir}/cmake/lxqt
