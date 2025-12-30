Name:		python-pymacaroons
Version:	0.13.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pymacaroons/pymacaroons-%{version}.tar.gz
Summary:	Macaroon library for Python
URL:		https://pypi.org/project/pymacaroons/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Macaroon library for Python

%prep
%autosetup -p1 -n pymacaroons-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/pymacaroons
%{py_sitedir}/pymacaroons-*.*-info
