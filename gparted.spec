Summary:	GNOME Partition Editor
Summary(pl):	Edytor partycji dla GNOME
Name:		gparted
Version:	0.0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/gparted/%{name}-%{version}.tar.bz2
# Source0-md5:	dd2942221ae3e835bdc52fd594e9b51a
Patch0:		%{name}-am.patch
URL:		http://gparted.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	parted-devel >= 1.6.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GParted stands for GNOME Partition Editor and is a graphical frontend
to parted. Among other features it supports creating, resizing, moving
and copying of partitions.

%description -l pl
GParted jest graficzn± nak³adk± na parted. Program umo¿liwia miêdzy
innymi tworzenie, zmianê rozmiaru, przenoszenie i kopiowanie partycji.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
