%define		_pre	rc1
Summary:	Python language binding for Smart Common Input Method platform
Name:		scim-python
Version:	0.1.13
Release:	0.%{_pre}.0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://scim-python.googlecode.com/files/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	d3b21df185b88a2100c2eee0007bc2cd
Source1:	http://scim-python.googlecode.com/files/pinyin-database-0.1.10.5.tar.bz2
# Source1-md5:	140a7dd821e8e74299bfb2089993838b
Source2:	http://scim-python.googlecode.com/files/xingma-zhengma-0.1.10.1.tar.bz2
# Source2-md5:	8adb3e43fe3c898caeaaf5146eaa3e94
Source3:	http://scim-python.googlecode.com/files/xingma-wubi86-0.1.10.1.tar.bz2
# Source3-md5:	016146c4683e7b250a9738c08a9a7f1f
Source4:	http://scim-python.googlecode.com/files/xingma-erbi-qingsong-0.1.10.1.tar.bz2
# Source4-md5:	9fee870c92f174d0d3fce31513e20b96
Source5:	http://scim-python.googlecode.com/files/xingma-cangjie5-0.1.10.1.tar.bz2
# Source5-md5:	873a0bbbbf24b584ec5015e7775549c1
Patch0:		%{name}-bashizm.patch
URL:		http://code.google.com/p/scim-python/
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	perl(XML::Parser)
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	scim-devel
Requires:	python-modules
Requires:	python-pygtk-gtk
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python wrapper for Smart Common Input Method platform.

%package english
Summary:	Python english IM engine
Group:		Libraries
BuildRequires:	python-pyenchant
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyenchant

%description english
This package contains a python english IM engine.

%package pinyin
Summary:	Two python chinese pinyin IM engines
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pinyin
This package contains two python chinese pinyin IM engines.

%package chinese
Summary:	Python chinese IM engines
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pinyin = %{version}-%{release}
Requires:	%{name}-xingma-cangjie = %{version}-%{release}
Requires:	%{name}-xingma-erbi = %{version}-%{release}
Requires:	%{name}-xingma-wubi = %{version}-%{release}
Requires:	%{name}-xingma-zhengma = %{version}-%{release}

%description chinese
This package contains some python chinese IM engines.

%package xingma
Summary:	Python XingMa IM engine
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description xingma
This package contains a python XingMa IM engine.

%package xingma-cangjie
Summary:	CangJie table for Python XingMa IM engine
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-cangjie
This package contains a CangJie table for python XingMa IM engine.

%package xingma-erbi
Summary:	ErBi table for Python XingMa IM engine
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-erbi
This package contains an ErBi table for python XingMa IM engine.

%package xingma-wubi
Summary:	WuBi table for Python XingMa IM engine
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-wubi
This package contains an ZhengMa table for python XingMa IM engine.

%package xingma-zhengma
Summary:	ZhengMa table for Python XingMa IM engine
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-zhengma
This package contains an ZhengMa table for python XingMa IM engine.

%prep
%setup -q -n %{name}-%{version}%{_pre} -a2 -a3 -a4 -a5
%patch0 -p1

cp %{SOURCE1} python/engine/PinYin/

%build
%{__autoconf}
%configure \
	--enable-english-writer \
	--enable-pinyin

%{__make}

%{__python} python/engine/XingMa/XMCreateDB.py -s cangjie5.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s erbi-qs.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s wubi.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s zhengma.txt.bz2 -p data/pinyin_table.txt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/scim-0.1/scim/_scim.la

install cangjie5.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables/
install cangjie.png $RPM_BUILD_ROOT%{_datadir}/scim/icons/

install erbi-qs.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables/
install erbi-qs.png $RPM_BUILD_ROOT%{_datadir}/scim/icons/

install wubi.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables/
install wubi.png $RPM_BUILD_ROOT%{_datadir}/scim/icons/

install zhengma.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables/
install zhengma.png $RPM_BUILD_ROOT%{_datadir}/scim/icons/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{py_sitedir}/scim-0.1
%dir %{py_sitedir}/scim-0.1/scim
%attr(755,root,root) %{py_sitedir}/scim-0.1/scim/_scim.so
%{py_sitedir}/scim-0.1/scim/*.py*
%{py_sitedir}/scim.pth
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/python.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/Helper/python.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/python.so
%dir %{_datadir}/scim-python
%dir %{_datadir}/scim-python/engine
%dir %{_datadir}/scim-python/setupui
%dir %{_datadir}/scim-python/helper
%{_datadir}/scim-python/engine/__init__.py*
%{_datadir}/scim-python/setupui/__init__.py*
%{_datadir}/scim-python/helper/__init__.py*
%{_datadir}/scim/icons/scim-python.png

%files english
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/EnglishWriter
%{_datadir}/scim-python/setupui/EnglishWriter

%files chinese
%defattr(644,root,root,755)

%files pinyin
%defattr(644,root,root,755)
%dir %{_datadir}/scim-python/data
%{_datadir}/scim-python/data/pinyin_table.txt
%{_datadir}/scim-python/engine/PinYin
%{_datadir}/scim-python/helper/PinYinSetup
%{_datadir}/scim-python/helper/ZhengJuSetup

%files xingma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XMCreateDB
%dir %{_datadir}/scim-python/engine/XingMa
%attr(755,root,root) %{_datadir}/scim-python/engine/XingMa/XMCreateDB.py
%{_datadir}/scim-python/engine/XingMa/XMDict.py*
%{_datadir}/scim-python/engine/XingMa/XMSQLiteDB.py*
%{_datadir}/scim-python/engine/XingMa/XingMa.py*
%{_datadir}/scim-python/engine/XingMa/__init__.py*
%dir %{_datadir}/scim-python/engine/XingMa/tables
%{_datadir}/scim-python/engine/XingMa/tables/.keep
%{_datadir}/scim/icons/py-mode.png
%{_datadir}/scim/icons/xm-mode.png

%files xingma-cangjie
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/XingMa/tables/cangjie5.db
%{_datadir}/scim/icons/cangjie.png

%files xingma-erbi
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/XingMa/tables/erbi-qs.db
%{_datadir}/scim/icons/erbi-qs.png

%files xingma-wubi
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/XingMa/tables/wubi.db
%{_datadir}/scim/icons/wubi.png

%files xingma-zhengma
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/XingMa/tables/zhengma.db
%{_datadir}/scim/icons/zhengma.png
