Summary:	GNOME Partition Editor
Summary(pl.UTF-8):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.32.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/gparted/%{name}-%{version}.tar.gz
# Source0-md5:	df4fe0350ba55cee6fddae289bd9d3f1
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	glibmm-devel >= 2.45.40
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel >= 2.22.0
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libsigc++-devel >= 1:2.5.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-progs
BuildRequires:	parted-devel >= 3.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	gksu
Requires:	glibmm >= 2.45.40
Requires:	gtkmm >= 2.22.0
Requires:	hicolor-icon-theme
Requires:	libsigc++ >= 1:2.5.1
Requires:	parted >= 3.2
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
%attr(755,root,root) %{_bindir}/gparted
%attr(755,root,root) %{_sbindir}/gpartedbin
%{_desktopdir}/gparted.desktop
%{_iconsdir}/hicolor/*/apps/gparted.*
%{_datadir}/appdata/gparted.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.gparted.policy
%{_mandir}/man8/gparted.8*
