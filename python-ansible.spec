%global debug_package %{nil}

Name: python-ansible
Epoch: 100
Version: 5.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Official assortment of Ansible collections
License: GPL-3.0-only
URL: https://github.com/ansible-community/ansible-build-data/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Ansible collections for ansible-core.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type d -name '.*' -prune -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '.*' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.orig' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.pem' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.rej' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.swp' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.rst' -exec chmod a-x {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' -exec sed -i -e 's|^#!/usr/bin/env python|#!/usr/bin/python3|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' -exec sed -i -e 's|^#!/usr/bin/python.*|#!/usr/bin/python3|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' | xargs grep -E -l -e '^#!/usr/bin/python3' | xargs chmod a+x
find %{buildroot}%{python3_sitelib} -type f -name '*.sh' -exec sed -i -e 's|^#!/usr/bin/env bash|#!/bin/bash|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.sh' | xargs grep -E -l -e '^#!/bin/bash' | xargs chmod a+x
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/ansible/windows/tests/integration/targets/win_command/files/crt_setmode.c
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/community/vmware/check-ignores-order
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/kubernetes/core/molecule/default/roles/k8scopy/files/hello
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%package -n ansible
Summary: Official assortment of Ansible collections
Requires: ansible-core >= 100:2.12.0
Requires: ansible-core < 100:2.13
Requires: python3
Provides: python3-ansible = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible) = %{epoch}:%{version}-%{release}

%description -n ansible
Ansible collections for ansible-core.

%files -n ansible
%license COPYING
%{python3_sitelib}/*

%changelog
