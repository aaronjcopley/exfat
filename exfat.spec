Name: exfat
Summary: Free exFAT file system implementation
Version: 1.4.0
Release: 1%{?dist}
License: GPLv2+
Source: https://github.com/relan/exfat/archive/refs/tags/v%{version}.tar.gz
URL: https://github.com/relan/exfat
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fuse-devel
BuildRequires: gcc

%description
This project aims to provide a full-featured exFAT file system implementation
for Unix-like systems. It consists of a FUSE module (fuse-exfat) and a set of
utilities (exfat-utils).

%package -n %{name}-utils
Summary: Utilities for managing the exFAT file system
Conflicts: exfatprogs

%description -n %{name}-utils
The exfat-utils package contains a number of utilities for creating, checking,
modifying, and correcting inconsistencies in exFAT file systems.

%prep
%autosetup

%build
autoreconf --install
%configure
%make_build

%install
%make_install
ln -s %{_mandir}/man8/exfatfsck.8.gz %{buildroot}/%{_mandir}/man8/fsck.exfat.8.gz
ln -s %{_mandir}/man8/mkexfatfs.8.gz %{buildroot}/usr/share/man/man8/mkfs.exfat.8.gz
ln -s %{_mandir}/man8/mount.exfat-fuse.8.gz %{buildroot}/usr/share/man/man8/mount.exfat.8.gz

%files -n %{name}-utils
%license COPYING
%{_sbindir}/dumpexfat
%{_sbindir}/exfatattrib
%{_sbindir}/exfatfsck
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%{_sbindir}/mkfs.exfat
%{_mandir}/man8/dumpexfat.8.gz
%{_mandir}/man8/exfatattrib.8.gz
%{_mandir}/man8/exfatfsck.8.gz
%{_mandir}/man8/exfatlabel.8.gz
%{_mandir}/man8/fsck.exfat.8.gz
%{_mandir}/man8/mkexfatfs.8.gz
%{_mandir}/man8/mkfs.exfat.8.gz

%package -n fuse-%{name}
Summary: FUSE driver for exFAT filesystem
Requires: fuse

%description -n fuse-%{name}
A FUSE file system driver to access files on exFAT file systems

%files -n fuse-%{name}
%{_sbindir}/mount.exfat
%{_sbindir}/mount.exfat-fuse
%{_mandir}/man8/mount.exfat-fuse.8.gz
%{_mandir}/man8/mount.exfat.8.gz

%changelog
* Sun Feb 02 2025 Aaron Copley <3943415+aaronjcopley@users.noreply.github.com> - 1.4.0-1
- Initial package
