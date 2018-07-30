#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-bash
Version  : 0.3.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/08/48/48bf12b657b68bc8eeee64245a15d331cb6d204c9855f9bdb21c48517df3/colcon-bash-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/08/48/48bf12b657b68bc8eeee64245a15d331cb6d204c9855f9bdb21c48517df3/colcon-bash-0.3.1.tar.gz
Summary  : Extension for colcon to provide Bash scripts.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-bash-python3
Requires: colcon-bash-python
BuildRequires : buildreq-distutils3

%description
===========

%package python
Summary: python components for the colcon-bash package.
Group: Default
Requires: colcon-bash-python3

%description python
python components for the colcon-bash package.


%package python3
Summary: python3 components for the colcon-bash package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-bash package.


%prep
%setup -q -n colcon-bash-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532981314
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
