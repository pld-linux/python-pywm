
%define		module	pywm

Summary:	Module for WindowMaker docklets
Summary(pl):	Modu³ do tworzenia dokletów dla WindowMakera
Name:		python-%{module}
Version:	0.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://errl.info/pywmdockapps/downloads/current/pywmgeneral-%{version}.tar.gz
# Source0-md5:	a393198a17f0c3f14920525cffc82669
URL:		http://errl.info/pywmdockapps/
BuildRequires:	XFree86-devel
BuildRequires:	python-devel >= 1:2.4
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
%setup -q -n pywmgeneral-%{version}

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
