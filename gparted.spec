Summary:	GNOME Partition Editor
Summary(pl.UTF-8):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.18.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
# Source0-md5:	c4c928de08519c923abaa5a099881241
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	glibmm-devel >= 2.14
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel >= 2.16.0
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-progs
BuildRequires:	parted-devel >= 1.7.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	gksu
Requires:	hicolor-icon-theme
Requires:	parted >= 1.7.1
Suggests:	btrfs-progs
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	hfsutils
Suggests:	jfsutils
Suggests:	lvm2
Suggests:	mdadm
Suggests:	mtools
Suggests:	nilfs-utils
Suggests:	ntfsprogs
Suggests:	reiser4progs
Suggests:	reiserfsprogs
Suggests:	xfsprogs
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GKSUPROG=/usr/bin/gksu \
	--enable-libparted-dmraid \
	--enable-online-resize

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/gparted
%attr(755,root,root) %{_sbindir}/gpartedbin
%{_desktopdir}/gparted.desktop
%{_mandir}/man8/gparted.8*
%{_iconsdir}/*/*/*/gparted.*
%{_datadir}/appdata/gparted.appdata.xml
