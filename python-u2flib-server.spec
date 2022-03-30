#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 based U2F server library
Summary(pl.UTF-8):	Biblioteka serwera U2F dla Pythona 2
Name:		python-u2flib-server
Version:	5.0.0
Release:	6
License:	BSD
Group:		Libraries/Python
Source0:	https://developers.yubico.com/python-u2flib-server/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	c87bc9984adf96e97aa35323dfc1edd4
URL:		https://developers.yubico.com/python-u2flib-server/
BuildRequires:	asciidoc
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography >= 1.2
BuildRequires:	python-enum34
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 1.2
BuildRequires:	python3-six
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides functionality for working with the server side aspects of the
U2F protocol as defined in FIDO specifications
(<http://fidoalliance.org/specifications/download>).

%description -l pl.UTF-8
Pakiet zawiera funkcje obsługujące serwerowe aspekty protokołu U2F
zdefiniowane w specyfikacji FIDO
(<http://fidoalliance.org/specifications/download>).

%package -n python3-u2flib-server
Summary:	Python 3 based U2F server library
Summary(pl.UTF-8):	Biblioteka serwera U2F dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-u2flib-server
Provides functionality for working with the server side aspects of the
U2F protocol as defined in FIDO specifications
(<http://fidoalliance.org/specifications/download>).

%description -n python3-u2flib-server -l pl.UTF-8
Pakiet zawiera funkcje obsługujące serwerowe aspekty protokołu U2F
zdefiniowane w specyfikacji FIDO
(<http://fidoalliance.org/specifications/download>).

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{py_sitescriptdir}/u2flib_server
%{py_sitescriptdir}/python_u2flib_server-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-u2flib-server
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{py3_sitescriptdir}/u2flib_server
%{py3_sitescriptdir}/python_u2flib_server-%{version}-py*.egg-info
%endif
