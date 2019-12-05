#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-bash
Version  : 0.4.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/de/0b/f8eacb552c30aaf87c91db496b0216a3f7c89ed57959f9a48c7fbbf142c4/colcon-bash-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/0b/f8eacb552c30aaf87c91db496b0216a3f7c89ed57959f9a48c7fbbf142c4/colcon-bash-0.4.1.tar.gz
Summary  : Extension for colcon to provide Bash scripts.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-bash-python = %{version}-%{release}
Requires: colcon-bash-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
colcon-bash
===========
An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to provide `Bash <https://www.gnu.org/software/bash/>`_ scripts.

%package python
Summary: python components for the colcon-bash package.
Group: Default
Requires: colcon-bash-python3 = %{version}-%{release}

%description python
python components for the colcon-bash package.


%package python3
Summary: python3 components for the colcon-bash package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-bash package.


%prep
%setup -q -n colcon-bash-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569982935
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
