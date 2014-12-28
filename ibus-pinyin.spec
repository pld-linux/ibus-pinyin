#
# Conditional build:
%bcond_without	opencc	# OpenCC Chinese conversion
#
Summary:	The Chinese Pinyin and Bopomofo engines for IBus input platform
Summary(pl.UTF-8):	Silniki chińskie Pinyin i Bopomofo dla platformy wprowadzania znaków IBus
Name:		ibus-pinyin
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		Libraries
# note: currently developed in https://github.com/ibus/ibus-pinyin
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f7728b5b785fae58e2b4de8dfda45612
Patch0:		%{name}-xx-icon-symbol.patch
Patch1:		%{name}-lua51.patch
URL:		https://github.com/ibus/ibus-pinyin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	boost-devel >= 1.39
BuildRequires:	gettext-tools
BuildRequires:	ibus-devel >= 1.4.99
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	lua51-devel >= 5.1
%{?with_opencc:BuildRequires:	opencc-devel}
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	pyzy-devel >= 0.0.8
BuildRequires:	sqlite3-devel >= 3
Requires:	ibus >= 1.4.99
%requires_eq_to pyzy-db pyzy-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%description -l pl.UTF-8
Silniki chińskie Pinyin i Bopomofo dla platformy wprowadzania znaków
IBus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-boost \
	%{?with_opencc:--enable-opencc} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/ibus-engine-pinyin
%attr(755,root,root) %{_libexecdir}/ibus-setup-pinyin
%{_datadir}/ibus-pinyin/phrases.txt
%{_datadir}/ibus-pinyin/icons
%{_datadir}/ibus-pinyin/setup
%dir %{_datadir}/ibus-pinyin
%dir %{_datadir}/ibus-pinyin/db
%{_datadir}/ibus/component/pinyin.xml
%{_datadir}/ibus-pinyin/base.lua
%{_datadir}/ibus-pinyin/db/english.db
%{_desktopdir}/ibus-setup-bopomofo.desktop
%{_desktopdir}/ibus-setup-pinyin.desktop
