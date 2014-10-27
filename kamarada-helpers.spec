#
# spec file for package kamarada-helpers
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


Name:           kamarada-helpers
Version:        13.1
Release:        1
Summary:        Kamarada helpers for installing new software
License:        GPL-2.0+
Group:          Metapackages
Url:            https://github.com/kamarada/kamarada-helpers
Source0:        LICENSE
Source1:        rootcopy.tar.gz
BuildArch:      noarch
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       hicolor-icon-theme
Requires:       sudo
Requires:       yast2-metapackage-handler


%description
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.


%prep
cp -a %{SOURCE0} COPYING
mkdir rootcopy
tar -zxvf %{SOURCE1} -C rootcopy


%build


%install
cp -R $RPM_BUILD_DIR/rootcopy/* $RPM_BUILD_ROOT
%suse_update_desktop_file opera


%files
%defattr(-,root,root)
%doc COPYING
%dir /usr/share/Kamarada/
%dir /usr/share/Kamarada/helpers/
/usr/share/icons/hicolor/*/apps/kamarada_helper.png
/usr/share/Kamarada/helpers/common


%package opera
Summary:        Kamarada helper for installing the Opera Browser
Group:          Metapackages
Requires:       kamarada-helpers

Conflicts:      opera


%description opera
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Opera Browser.


%files opera
%defattr(-,root,root)
%doc COPYING
/usr/bin/opera
/usr/share/applications/opera.desktop
/usr/share/Kamarada/helpers/opera.ymp