Summary:	Telegram is a new era of messaging
Name:		telegram-desktop
Version:	0.9.15
Release:	1%{?dist}

Group:		Applications/Internet
License:	GPLv3
URL:		https://telegram.org/
Source0:	https://updates.tdesktop.com/tlinux32/tsetup32.%{version}.tar.xz
Source1:	https://updates.tdesktop.com/tlinux/tsetup.%{version}.tar.xz
Source2:	telegram.png
Source3:	telegram.desktop

BuildRequires:	desktop-file-utils


%description
Telegram is a messaging app with a focus on speed and security, it’s super
fast, simple and free. You can use Telegram on all your devices at the same
time — your messages sync seamlessly across any of your phones, tablets or
computers.

With Telegram, you can send messages, photos, videos and files of any type
(doc, zip, mp3, etc), as well as create groups for up to 200 people. You can
write to your phone contacts and find people by their usernames. As a result,
Telegram is like SMS and email combined — and can take care of all your
personal or business messaging needs.


%prep
%ifarch %ix86
%setup -b0 -q -n Telegram
%endif

%ifarch x86_64 amd64
%setup -b1 -q -n Telegram
%endif

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -arf ./Telegram %{buildroot}%{_datadir}/%{name}/telegram
cp -arf ./Updater %{buildroot}%{_datadir}/%{name}/updater
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

ln -s %{_datadir}/%{name}/telegram %{buildroot}%{_bindir}/telegram

cp %{SOURCE3} %{buildroot}%{_datadir}/%{name}.desktop

desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/%{name}.desktop


%files
%{_bindir}/telegram
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/telegram
%{_datadir}/%{name}/updater
%{_datadir}/applications/telegram-desktop.desktop
%{_datadir}/pixmaps/telegram.png

%changelog
* Thu Dec 10 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.15-1.R
- update to 0.9.15

* Thu Nov 26 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.13-1.R
- update to 0.9.13

* Fri Nov 13 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.10-1.R
- update to 0.9.10

* Tue Oct 27 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 0.9.6-1.R
- clean up spec
- update to 0.9.6

* Mon Aug 03 2015 rommon <rommon@t-online.de> - 0.8.45-1
- update to new version

* Sat Jul 18 2015 rommon <rommon@t-online.de> - 0.8.38-1
- update to new version

* Fri Jun 26 2015 rommon <rommon@t-online.de> - 0.8.32-1
- update to new version
- rename from telegram to telegram-desktop

* Tue Jun 9 2015 rommon <rommon@t-online.de> - 0.8.24-1
- update to new version

* Fri May 1 2015 rommon <rommon@t-online.de> - 0.8.11-1
- update to new version

* Mon Apr 27 2015 rommon <rommon@t-online.de> - 0.8.7-1
- update to new version

* Mon Apr 27 2015 rommon <rommon@t-online.de> - 0.8.4-5
- fix icon permissions

* Fri Apr 24 2015 rommon <rommon@t-online.de> - 0.8.4-4
- fix desktop file

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-3
- changed desktop file

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-2
- adaption for 32/64 bit builds

* Tue Apr 21 2015 rommon <rommon@t-online.de> - 0.8.4-1
- initial package
