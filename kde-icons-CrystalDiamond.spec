%define         _name CrystalDiamond
Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	2.5
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.hasnoname.de/Iconpacks/%{_name}%{version}Classical.tar.gz
# Source0-md5:	d2d94e146c3f32339c4cb60a71261273
URL:		http://www.paolinoland.it/
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a realistic icon theme based on the best of Realistik, Vista Inspirate
Nuove XT, Crystal Clear, OSX, Debian Icons and many others.

%description -l pl
%{_name} to motyw ikon sk�adaj�cy si� z najlepszych ikon wybranych z motyw�w Realistik,
Vista Inspirate, Nuove XT, Crystal Clear, OSX, Debian Icons i wielu innych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
