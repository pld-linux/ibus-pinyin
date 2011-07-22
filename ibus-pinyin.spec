Summary:	The Chinese Pinyin and Bopomofo engines for IBus input platform
Name:		ibus-pinyin
Version:	1.3.99.20110706
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0d9d5d78106c2d36c28a00b74aa9a6c3
Source1:	http://ibus.googlecode.com/files/pinyin-database-1.2.99.tar.bz2
# Source1-md5:	d0951b8daa7f56a2cbd3b6b4e42532e0
Patch0:		%{name}-boost.patch
Patch1:		%{name}-lua51.patch
URL:		http://code.google.com/p/ibus
BuildRequires:	boost-devel
BuildRequires:	ibus-devel >= 1.3.99
BuildRequires:	libuuid-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
Requires:	ibus >= 1.2.0
Requires:	ibus-pinyin-db = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Chinese Pinyin and Bopomof input methods for IBus platform.

%package db-open-phrase
Summary:	The open phrase database for ibus Pinyin
Group:		Libraries
Provides:	ibus-pinyin-db = %{version}-%{release}

%description db-open-phrase
The phrase database for ibus Pinyin and Bopomofo from open-phrase
project.

%package db-android
Summary:	The android phrase database for ibus Pinyin and Bopomofo
Group:		Libraries
Provides:	ibus-pinyin-db = %{version}-%{release}

%description db-android
The phrase database for ibus Pinyin and Bopomofo from android project.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} data/db/open-phrase

%build
%{__autoconf}
%configure \
	--enable-db-open-phrase \
	--disable-opencc \
	--enable-boost

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=${RPM_BUILD_ROOT}

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
%{_datadir}/ibus/component/*
%{_datadir}/ibus-pinyin/base.lua
%{_datadir}/ibus-pinyin/db/english.db

%files db-open-phrase
%defattr(644,root,root,755)
%{_datadir}/ibus-pinyin/db/open-phrase.db

%files db-android
%defattr(644,root,root,755)
%{_datadir}/ibus-pinyin/db/android.db
