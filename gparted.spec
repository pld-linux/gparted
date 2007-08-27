Summary:	GNOME Partition Editor
Summary(pl.UTF-8):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.3.3
Release:	5
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
# Source0-md5:	f3d16ccfda72fa1dac9fa1ff9ded2c42
Patch0:		%{name}-desktop.patch
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	parted-devel >= 1.7.1
BuildRequires:	pkgconfig
Requires:	parted >= 1.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GParted stands for GNOME Partition Editor and is a graphical frontend
to parted. Among other features it supports creating, resizing, moving
and copying of partitions.

%description -l pl.UTF-8
GParted jest graficzną nakładką na parted. Program umożliwia między
innymi tworzenie, zmianę rozmiaru, przenoszenie i kopiowanie partycji.

%prep
%setup -q
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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
