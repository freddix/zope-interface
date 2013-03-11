Summary:	Python 'interface' concept implementation
Name:		zope-interface
Version:	4.0.3
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
# Source0-md5:	1ddd308f2c83703accd1696158c300eb
URL:		http://www.zope.org/Products/ZopeInterface/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	zope-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 'interface' concept implementation.

%prep
%setup -qn zope.interface-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/*.c
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/common/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/zope/interface/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py_sitedir}/zope/interface
%attr(755,root,root) %{py_sitedir}/zope/interface/_zope_interface_coptimizations.so
%{py_sitedir}/zope.interface-*-nspkg.pth
%{py_sitedir}/zope/interface/*.py[co]
%{py_sitedir}/zope/interface/common

