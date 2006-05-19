
%define		module	pywm
%define 	ver	0-1-6

Summary:	Module for WindowMaker docklets
Summary(pl):	Modu³ do tworzenia dokletów dla WindowMakera
Name:		python-%{module}
Version:	0.1.6
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pywmdockapps/pywmdockapps.%{ver}.tar.gz
# Source0-md5:	e5f1152984862d1cf9925b169c0e8681
URL:		http://pywmdockapps.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	sed >= 4.0
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

%description -l pl
Pywmgeneral to modu³ Pythona pomocny przy tworzeniu dokletów dla
WindowMakera w Pythonie. Jest to w wiêkszo¶ci wrapper dla funkcji z
popularnego wmgeneral.c, ale dodano te¿ trochê nowych funkcji.

Pakiet zawiera tak¿e napisany w Pythonie modu³ pywmhelpers.py
zawieraj±ce funkcje pomocne przy tworzeniu dokletów WM. Ten modu³
zawiera funkcje Pythona obudowuj±ce funkcje dostarczane przez modu³
rozszerzenia. U³atwiaj± przekazywanie argumentów i zwracaj±
przyjemniejsze warto¶ci. Dostêpne jest te¿ trochê dodatkowych funkcji,
takich jak pomoc przy obs³udze prostego pliku konfiguracyjnego. Ten
modu³ jest lepiej udokumentowany ni¿ pywmgeneral. Zalecane jest
u¿ywanie wy³±cznie pywmhelpers i nie ruszanie w ogóle modu³u
pywmgeneral bezpo¶rednio. Informacje o sposobie korzystania z modu³u
znajduj± siê w dokumentacji w pywmhelpers.py. Mo¿liwe jest tak¿e
zaimportowanie go z poziomu interaktywnego interpretera i wywo³anie
"help(pywmhelpers)".

%prep
%setup -q -n pywmgeneral

sed -i -e 's,/usr/X11R6/lib,/usr/X11R6/%{_lib},' setup.py

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
