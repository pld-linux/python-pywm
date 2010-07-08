%define		module	pywm
%define 	ver		0-1-6
Summary:	Module for WindowMaker docklets
Summary(pl.UTF-8):	Moduł do tworzenia dokletów dla WindowMakera
Name:		python-%{module}
Version:	0.1.6
Release:	5
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pywmdockapps/pywmdockapps.%{ver}.tar.gz
# Source0-md5:	e5f1152984862d1cf9925b169c0e8681
URL:		http://pywmdockapps.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pywmgeneral is a Python module that will help you develope WindowMaker
dockapps in Python. It is mostly a wrapper around the functions from
the popular wmgeneral.c, but some new functions are added too.

It also contains the Python written module pywmhelpers.py which
contains functions to aid the development of WM dockapps. This module
contains Python functions that wrap up the functions which the
extension module provides. They ease up argument passing and give
nicer return values. Some additional functions, like help for handling
a simple configuration file is also available. This module is better
documented than the pywmgeneral. It is adviced to only use pywmhelpers
and not touch the pywmgeneral module directly at all. For information
about how to use the module, see the documentation in pywmhelpers.py.
It is also possible to import it in the interactive interpreter and
issue 'help(pywmhelpers)'.

%description -l pl.UTF-8
Pywmgeneral to moduł Pythona pomocny przy tworzeniu dokletów dla
WindowMakera w Pythonie. Jest to w większości wrapper dla funkcji z
popularnego wmgeneral.c, ale dodano też trochę nowych funkcji.

Pakiet zawiera także napisany w Pythonie moduł pywmhelpers.py
zawierające funkcje pomocne przy tworzeniu dokletów WM. Ten moduł
zawiera funkcje Pythona obudowujące funkcje dostarczane przez moduł
rozszerzenia. Ułatwiają przekazywanie argumentów i zwracają
przyjemniejsze wartości. Dostępne jest też trochę dodatkowych funkcji,
takich jak pomoc przy obsłudze prostego pliku konfiguracyjnego. Ten
moduł jest lepiej udokumentowany niż pywmgeneral. Zalecane jest
używanie wyłącznie pywmhelpers i nie ruszanie w ogóle modułu
pywmgeneral bezpośrednio. Informacje o sposobie korzystania z modułu
znajdują się w dokumentacji w pywmhelpers.py. Możliwe jest także
zaimportowanie go z poziomu interaktywnego interpretera i wywołanie
"help(pywmhelpers)".

%prep
%setup -q -n pywmgeneral
%{__sed} -i -e 's,/usr/X11R6/lib,%{?_x_libraries}%{!?_x_libraries:%{_libdir}},' setup.py

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pywmgeneral-*.egg-info
%endif
