#
# TODO:
#	/usr/lib64/scim-1.0/scim-helper-launcher setup 8034d025-bdfc-4a10-86a4-82b9461b32b0
#	Reading pinyin phrase lib failed
#	Traceback (most recent call last):
#	  File "/usr/share/scim-python/setupui/__init__.py", line 27, in <module>
#	    import gtk 
#	  File "/usr/lib64/python2.7/site-packages/gtk-2.0/gtk/__init__.py", line 30, in <module>
#	  File "/usr/lib64/python2.7/site-packages/gobject/__init__.py", line 26, in <module>
#	  File "/usr/lib64/python2.7/site-packages/glib/__init__.py", line 22, in <module>
#	ImportError: /usr/lib64/libpyglib-2.0-python.so.0: undefined symbol: PyCObject_Type
#	Segmentation fault
#
Summary:	Python language binding for Smart Common Input Method platform
Summary(pl.UTF-8):	Wiązania Pythona dla platformy wprowadzania znaków SCIM
Name:		scim-python
Version:	0.1.13
%define	subver	rc1
Release:	0.%{subver}.0.1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/scim-python/downloads/list
Source0:	http://scim-python.googlecode.com/files/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	d3b21df185b88a2100c2eee0007bc2cd
Source1:	http://scim-python.googlecode.com/files/pinyin-database-0.1.10.5.tar.bz2
# Source1-md5:	140a7dd821e8e74299bfb2089993838b
Source2:	http://scim-python.googlecode.com/files/xingma-zhengma-0.1.10.1.tar.bz2
# Source2-md5:	8adb3e43fe3c898caeaaf5146eaa3e94
Source3:	http://scim-python.googlecode.com/files/xingma-wubi86-0.1.10.1.tar.bz2
# Source3-md5:	016146c4683e7b250a9738c08a9a7f1f
Source4:	http://scim-python.googlecode.com/files/xingma-erbi-qingsong-0.1.10.1.tar.bz2
# Source4-md5:	9fee870c92f174d0d3fce31513e20b96
Source5:	http://scim-python.googlecode.com/files/xingma-cangjie5-0.1.10.2.tar.bz2
# Source5-md5:	90c758ec2299e3dca30b58f42dd0c5dd
Source6:	http://scim-python.googlecode.com/files/xingma-compose-0.1.10.1.tar.bz2
# Source6-md5:	2173d9fe28316652ea628c4cdb755785
Patch0:		%{name}-bashizm.patch
URL:		http://code.google.com/p/scim-python/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pyenchant
BuildRequires:	python-pygtk-devel >= 2:2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	scim-devel >= 1.4
Requires:	python-modules >= 1:2.5
Requires:	python-pygtk-gtk >= 2:2
Requires:	scim >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		scim_dir_ver	%(pkg-config --variable=scim_binary_version scim)

%description
Python wrapper for Smart Common Input Method platform.

%description -l pl.UTF-8
Pythonowe obudowanie dla platformy wprowadzania znaków SCIM (Smart
Common Input Method).

%package english
Summary:	Python English IM engine
Summary(pl.UTF-8):	Silnik IM w Pythonie dla języka angielskiego
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyenchant

%description english
This package contains a Python English IM engine.

%description english -l pl.UTF-8
Ten pakiet zawiera silnik IM w Pythonie dla języka angielskiego.

%package pinyin
Summary:	Two Python Chinese pinyin IM engines
Summary(pl.UTF-8):	Dwa silniki IM pinyin w Pythonie dla języka chińskiego
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pinyin
This package contains two python chinese pinyin IM engines.

%description pinyin -l pl.UTF-8
Dwa silniki IM pinyin w Pythonie dla języka chińskiego.

%package chinese
Summary:	Python Chinese IM engines (metapackage)
Summary(pl.UTF-8):	Silniki IM w Pythonie dla języka chińskiego (metapakiet)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pinyin = %{version}-%{release}
Requires:	%{name}-xingma-cangjie = %{version}-%{release}
Requires:	%{name}-xingma-compose = %{version}-%{release}
Requires:	%{name}-xingma-erbi = %{version}-%{release}
Requires:	%{name}-xingma-wubi = %{version}-%{release}
Requires:	%{name}-xingma-zhengma = %{version}-%{release}

%description chinese
This metapackage gathers some Python Chinese IM engines.

%description chinese
Ten metapakiet gromadzi kilka silników IM w Pythonie dla języka
chińskiego.

%package xingma
Summary:	Python XingMa IM engine
Summary(pl.UTF-8):	Silnik IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description xingma
This package contains a Python XingMa IM engine.

%description xingma -l pl.UTF-8
Ten pakiet zawiera silnik IM XingMa w Pythonie.

%package xingma-cangjie
Summary:	CangJie table for Python XingMa IM engine
Summary(pl.UTF-8):	Tablica CangJie dla silnika IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-cangjie
This package contains a CangJie table for Python XingMa IM engine.

%description xingma-cangjie -l pl.UTF-8
Ten pakiet zawiera tablicę CangJie dla silnika IM XingMa w Pythonie.

%package xingma-compose
Summary:	Compose table for Python XingMa IM engine
Summary(pl.UTF-8):	Tablica Compose dla silnika IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-compose
This package contains a Compose table for Python XingMa IM engine.

%description xingma-compose -l pl.UTF-8
Ten pakiet zawiera tablicę Compose dla silnika IM XingMa w Pythonie.

%package xingma-erbi
Summary:	ErBi table for Python XingMa IM engine
Summary(pl.UTF-8):	Tablica ErBi dla silnika IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-erbi
This package contains an ErBi table for Python XingMa IM engine.

%description xingma-erbi -l pl.UTF-8
Ten pakiet zawiera tablicę ErBi dla silnika IM XingMa w Pythonie.

%package xingma-wubi
Summary:	WuBi table for Python XingMa IM engine
Summary(pl.UTF-8):	Tablica WuBi dla silnika IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-wubi
This package contains an ZhengMa table for Python XingMa IM engine.

%description xingma-wubi -l pl.UTF-8
Ten pakiet zawiera tablicę WuBi dla silnika IM XingMa w Pythonie.

%package xingma-zhengma
Summary:	ZhengMa table for Python XingMa IM engine
Summary(pl.UTF-8):	Tablica ZhengMa dla silnika IM XingMa w Pythonie
Group:		Libraries
Requires:	%{name}-xingma = %{version}-%{release}

%description xingma-zhengma
This package contains an ZhengMa table for Python XingMa IM engine.

%description xingma-zhengma -l pl.UTF-8
Ten pakiet zawiera tablicę ZhengMa dla silnika IM XingMa w Pythonie.

%prep
%setup -q -n %{name}-%{version}%{subver} -a2 -a3 -a4 -a5 -a6
%patch0 -p1

cp %{SOURCE1} python/engine/PinYin/

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-english-writer \
	--enable-pinyin

%{__make}

%{__python} python/engine/XingMa/XMCreateDB.py -s cangjie5.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s compose.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s erbi-qs.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s wubi.txt.bz2 -p data/pinyin_table.txt
%{__python} python/engine/XingMa/XMCreateDB.py -s zhengma.txt.bz2 -p data/pinyin_table.txt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/scim-0.1/scim/_scim.la

install cangjie5.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables
install cangjie5.png $RPM_BUILD_ROOT%{_datadir}/scim/icons

install compose.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables
install compose.png $RPM_BUILD_ROOT%{_datadir}/scim/icons

install erbi-qs.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables
install erbi-qs.png $RPM_BUILD_ROOT%{_datadir}/scim/icons

install wubi.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables
install wubi.png $RPM_BUILD_ROOT%{_datadir}/scim/icons

install zhengma.db $RPM_BUILD_ROOT%{_datadir}/scim-python/engine/XingMa/tables
install zhengma.png $RPM_BUILD_ROOT%{_datadir}/scim/icons

%py_postclean
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{py_sitedir}/scim-0.1
%dir %{py_sitedir}/scim-0.1/scim
%attr(755,root,root) %{py_sitedir}/scim-0.1/scim/_scim.so
%{py_sitedir}/scim-0.1/scim/*.py[co]
%{py_sitedir}/scim.pth
%attr(755,root,root) %{_libdir}/scim-1.0/%{scim_dir_ver}/Helper/python.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{scim_dir_ver}/IMEngine/python.so
%attr(755,root,root) %{_libdir}/scim-1.0/%{scim_dir_ver}/SetupUI/python.so
%dir %{_datadir}/scim-python
%dir %{_datadir}/scim-python/engine
%{_datadir}/scim-python/engine/__init__.py*
%dir %{_datadir}/scim-python/helper
%{_datadir}/scim-python/helper/__init__.py*
%dir %{_datadir}/scim-python/setupui
%{_datadir}/scim-python/setupui/__init__.py*
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
%{_datadir}/scim/icons/cangjie5.png

%files xingma-compose
%defattr(644,root,root,755)
%{_datadir}/scim-python/engine/XingMa/tables/compose.db
%{_datadir}/scim/icons/compose.png

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
