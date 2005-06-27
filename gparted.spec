%define		_pre	pre2
Summary:	GNOME Partition Editor
Summary(pl):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.0.9
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications/System
#Source0:	http://dl.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
Source0:	http://gparted.sourceforge.net/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	dd6e336e4eeee8265594aef4f73d1b0c
Patch0:		%{name}-desktop.patch
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	parted-devel >= 1.6.13
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GParted stands for GNOME Partition Editor and is a graphical frontend
to parted. Among other features it supports creating, resizing, moving
and copying of partitions.

%description -l pl
GParted jest graficzn± nak³adk± na parted. Program umo¿liwia miêdzy
innymi tworzenie, zmianê rozmiaru, przenoszenie i kopiowanie partycji.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Are these includes required?
rm -rf $RPM_BUILD_ROOT%{_includedir}/GParted

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
