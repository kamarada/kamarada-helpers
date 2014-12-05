#
# spec file for package Kamarada-helpers
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


Name:           Kamarada-helpers
Version:        13.2
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
%suse_update_desktop_file Kamarada-helpers-chromium
%suse_update_desktop_file Kamarada-helpers-google-chrome
%suse_update_desktop_file Kamarada-helpers-opera
%suse_update_desktop_file Kamarada-helpers-thunderbird


%files
%defattr(-,root,root)
%doc COPYING
%dir /usr/share/Kamarada/
%dir /usr/share/Kamarada/helpers/
/usr/share/icons/hicolor/*/apps/Kamarada_helper.png
/usr/share/Kamarada/helpers/common


%package chromium
Summary:        Kamarada helper for installing the Chromium Web Browser
Group:          Metapackages
Requires:       Kamarada-helpers

Conflicts:      chromium


%description chromium
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Chromium Web Browser.


%files chromium
%defattr(-,root,root)
%doc COPYING
/usr/bin/chromium
/usr/share/applications/Kamarada-helpers-chromium.desktop
/usr/share/Kamarada/helpers/chromium.ymp


%package google-chrome
Summary:        Kamarada helper for installing the Google Chrome Web Browser
Group:          Metapackages
Requires:       Kamarada-helpers

Conflicts:      google-chrome-stable
Conflicts:      google-chrome-beta
Conflicts:      google-chrome-unstable


%description google-chrome
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Google Chrome Web Browser.


%files google-chrome
%defattr(-,root,root)
%doc COPYING
/usr/bin/google-chrome-stable
/usr/share/applications/Kamarada-helpers-google-chrome.desktop
/usr/share/Kamarada/helpers/google-chrome-stable-i386.ymp
/usr/share/Kamarada/helpers/google-chrome-stable-x86_64.ymp


%post google-chrome
update-alternatives --install "/usr/bin/google-chrome" "google-chrome" "/usr/bin/google-chrome-stable" 1
update-alternatives --set "google-chrome" "/usr/bin/google-chrome-stable"


%postun google-chrome
update-alternatives --remove "google-chrome" "/usr/bin/google-chrome-stable"


%package opera
Summary:        Kamarada helper for installing the Opera Web Browser
Group:          Metapackages
Requires:       Kamarada-helpers

Conflicts:      opera


%description opera
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Opera Web Browser.


%files opera
%defattr(-,root,root)
%doc COPYING
/usr/bin/opera
/usr/share/applications/Kamarada-helpers-opera.desktop
/usr/share/Kamarada/helpers/opera.ymp


%package pidgin
Summary:        Kamarada helper for installing the Pidgin Internet Messenger
Group:          Metapackages
Requires:       Kamarada-helpers

Conflicts:      pidgin


%description pidgin
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Pidgin Internet Messenger.


%files pidgin
%defattr(-,root,root)
%doc COPYING
/usr/bin/pidgin
/usr/share/applications/Kamarada-helpers-pidgin.desktop
/usr/share/Kamarada/helpers/pidgin.ymp


%package thunderbird
Summary:        Kamarada helper for installing the Mozilla Thunderbird Mail/News Client
Group:          Metapackages
Requires:       Kamarada-helpers

Conflicts:      MozillaThunderbird


%description thunderbird
Kamarada helpers assist users installing softwares that aren't bundled with Kamarada by default, but probably they will look for.

This helper assists installing the Mozilla Thunderbird Mail/News Client.


%files thunderbird
%defattr(-,root,root)
%doc COPYING
/usr/bin/thunderbird
/usr/share/applications/Kamarada-helpers-thunderbird.desktop
/usr/share/Kamarada/helpers/thunderbird.ymp