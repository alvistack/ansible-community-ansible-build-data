# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ansible
Epoch: 100
Version: 9.11.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Official assortment of Ansible collections
License: GPL-3.0-only
URL: https://github.com/ansible-community/ansible-build-data/tags
Source0: %{name}_%{version}.orig.tar.gz
Source99: %{name}.rpmlintrc
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
find %{buildroot}%{python3_sitelib} -type d -name 'docs' -prune -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type d -name 'tests' -prune -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '.*' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.orig' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.pem' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.rej' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.swp' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.ps1' -exec rm -rf {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.rst' -exec chmod a-x {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' -exec sed -i -e 's|^#!/usr/bin/env python|#!/usr/bin/python3|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' -exec sed -i -e 's|^#!/usr/bin/python.*|#!/usr/bin/python3|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.py' | xargs grep -E -l -e '^#!/usr/bin/python3' | xargs chmod a+x
find %{buildroot}%{python3_sitelib} -type f -name '*.sh' -exec sed -i -e 's|^#!/usr/bin/env bash|#!/bin/bash|' {} \;
find %{buildroot}%{python3_sitelib} -type f -name '*.sh' | xargs grep -E -l -e '^#!/bin/bash' | xargs chmod a+x
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/ansible/windows/tests/integration/targets/win_command/files/crt_setmode.c
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/community/vmware/check-ignores-order
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/kubernetes/core/molecule/default/roles/k8scopy/files/hello
rm -rf %{buildroot}%{python3_sitelib}/ansible_collections/cisco/meraki/scripts
fdupes -qnrps %{buildroot}%{python3_sitelib}
install -Dpm755 -d %{buildroot}%{_datadir}/ansible/collctions
pushd %{buildroot}%{_datadir}/ansible/collctions && \
    ln -fs ../../../../%{python3_sitelib}/ansible_collections . && \
    popd

%check

%package -n ansible
Summary: Official assortment of Ansible collections
Requires: ansible-core >= 100:2.16.12
Requires: ansible-core < 100:2.17
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
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/collctions
%{_bindir}/*
%{_datadir}/ansible/collctions/*
%{python3_sitelib}/*

%changelog
