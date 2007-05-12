%define		_name	CrystalDiamond
Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	2.6
Release:	1
License:	GPL
Group:		Themes
Source0:	http://crystaldiamond.aualin.net/downloads/%{_name}%{version}_Class.tar.gz
# Source0-md5:	ae69e7785e0fd8b89d2c4860486f6333
URL:		http://www.paolinoland.it/
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CrystalDiamond is a realistic icon theme based on the best of
Realistik, Vista Inspirate Nuove XT, Crystal Clear, OSX, Debian Icons
and many others.

%description -l pl.UTF-8
CrystalDiamond to motyw ikon składający się z najlepszych ikon
wybranych z motywów Realistik, Vista Inspirate, Nuove XT, Crystal
Clear, OSX, Debian Icons i wielu innych.

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
