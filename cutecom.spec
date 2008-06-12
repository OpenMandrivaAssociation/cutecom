%define ver 0.14.1
%define rel 2

Name:		cutecom
Version:	%ver
Release:	%mkrel %rel
URL:		http://cutecom.sourceforge.net/
Summary:	Graphical serial terminal program
License:	GPL
Group:		Communications
Source:		http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	qt3-devel kdelibs-common desktop-file-utils

%description
CuteCom is a graphical serial terminal, like minicom. It is aimed mainly at
hardware developers or other people who need a terminal to talk to their
devices. 

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}
mv %{buildroot}/usr/local/bin %{buildroot}/%{_prefix}
mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}/usr/share/applnk/Utilities/cutecom.desktop %{buildroot}/usr/share/applications/cutecom.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="System;Settings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -Rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{_bindir}/cutecom
%{_datadir}/applications/cutecom.desktop
%doc README Changelog


