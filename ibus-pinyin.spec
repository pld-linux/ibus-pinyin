# TODO: opencc
Summary:	The Chinese Pinyin and Bopomofo engines for IBus input platform
Summary(pl.UTF-8):	Silniki chińskie Pinyin i Bopomofo dla platformy wprowadzania znaków IBus
Name:		ibus-pinyin
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	2cef66bef079969689a7e0fdb7b7f767
Source1:	http://ibus.googlecode.com/files/pinyin-database-1.2.99.tar.bz2
# Source1-md5:	d0951b8daa7f56a2cbd3b6b4e42532e0
Patch0:		%{name}-boost.patch
Patch1:		%{name}-lua51.patch
URL:		http://code.google.com/p/ibus
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	boost-devel >= 1.39
BuildRequires:	ibus-devel >= 1.3.99
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	sqlite3-devel >= 3
Requires:	ibus >= 1.2.0
Requires:	ibus-pinyin-db = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%description -l pl.UTF-8
Silniki chińskie Pinyin i Bopomofo dla platformy wprowadzania znaków
IBus.

%package db-open-phrase
Summary:	The open-phrase database for IBus Pinyin
Summary(pl.UTF-8):	Baza danych open-phraze dla modułu IBus Pinyin
Group:		Libraries
Provides:	ibus-pinyin-db = %{version}-%{release}

%description db-open-phrase
The phrase database for IBus Pinyin and Bopomofo from open-phrase
project.

%description db-open-phrase -l pl.UTF-8
Baza danych fraz dla silników IBus Pinyin i Bopomofo z projektu
open-phrase.

%package db-android
Summary:	The Android phrase database for IBus Pinyin and Bopomofo
Summary(pl.UTF-8):	Baza danych Androida dla modułu IBus Pinyin
Group:		Libraries
Provides:	ibus-pinyin-db = %{version}-%{release}

%description db-android
The phrase database for IBus Pinyin and Bopomofo from android project.

%description db-android
Baza danych fraz dla silników IBus Pinyin i Bopomofo z projektu
Android.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} data/db/open-phrase

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-boost \
	--enable-db-open-phrase \
	--disable-opencc \
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
%{_datadir}/ibus-pinyin/db/create_index.sql
%dir %{_datadir}/ibus-pinyin
%dir %{_datadir}/ibus-pinyin/db
%{_datadir}/ibus/component/pinyin.xml
%{_datadir}/ibus-pinyin/base.lua
%{_datadir}/ibus-pinyin/db/english.db

%files db-open-phrase
%defattr(644,root,root,755)
%{_datadir}/ibus-pinyin/db/open-phrase.db

%files db-android
%defattr(644,root,root,755)
%{_datadir}/ibus-pinyin/db/android.db
