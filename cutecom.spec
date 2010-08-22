%define ver 0.20.0
%define rel 1

Name:		cutecom
Version:	0.22.0
Release:	%mkrel %rel
URL:		http://cutecom.sourceforge.net/
Summary:	Graphical serial terminal program
License:	GPL
Group:		Communications
Source:		http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	qt4-devel desktop-file-utils cmake

%description
CuteCom is a graphical serial terminal, like minicom. It is aimed mainly at
hardware developers or other people who need a terminal to talk to their
devices. 

%prep
%setup -q

%build
%cmake
%make

%install
rm -Rf %{buildroot}
%makeinstall_std -C build

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="System;Settings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications cutecom.desktop

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
%{_mandir}/man1/cutecom.1*
%doc README Changelog
