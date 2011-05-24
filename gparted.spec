Summary:	GNOME Partition Editor
Summary(pl.UTF-8):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
# Source0-md5:	ba3a434a259ae2ddcfc7f7488ee648ef
URL:		http://gparted.sourceforge.net/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel >= 2.10.0
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-progs
BuildRequires:	parted-devel >= 1.7.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
Requires:	parted >= 1.7.1
Suggests:	dosfstools
Suggests:	e2fsprogs
Suggests:	hfsutils
Suggests:	jfsutils
Suggests:	mtools
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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/gparted
%attr(755,root,root) %{_sbindir}/gpartedbin
%{_desktopdir}/gparted.desktop
%{_mandir}/man8/gparted.8*
%{_iconsdir}/*/*/*/gparted.*
