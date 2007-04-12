%define ver 0.14.1
%define rel 1

Name:		cutecom
Version:	%ver
Release:	%mkrel %rel
URL:		http://cutecom.sourceforge.net/
Summary:	Graphical serial terminal program
License:	GPL
Group:		Communications
Source:		http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	qt3-devel mandriva-create-kde-mdk-menu kdelibs-common

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
install -d %{buildroot}/%{_menudir}
kdedesktop2mdkmenu.pl %{name} "More Applications/Communications" %{buildroot}/%{_datadir}/applnk/Utilities/cutecom.desktop %{buildroot}/%{_menudir}/%{name}

%clean
rm -Rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%{_bindir}/cutecom
%{_datadir}/applnk/Utilities/cutecom.desktop
%{_menudir}/%{name}
%doc README Changelog


