Name:           s3fs
Version:        1.73
Release:        1%{?dist}
Summary:        FUSE-based file system backed by Amazon S3
Group:          System Environment/Base

License:        GPLv2
URL:            http://code.google.com/p/s3fs
Source0:        http://s3fs.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        passwd-s3fs


Requires:	fuse >= 2.8.4
Requires:	curl >= 7.0
Requires:	libxml2 >= 2.6
Requires:	openssl >= 0.9

BuildRequires:  fuse-devel, curl-devel, libxml2-devel
BuildRequires:  openssl-devel, mailcap
Conflicts:      fuse-s3fs

%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size=64GB
(limited by s3fs, not Amazon).
.
s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%global debug_package %{nil}

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}
sed -i 's/\r//' README


%install
make install DESTDIR=%{buildroot}
cp -p %{SOURCE1} passwd-s3fs


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc AUTHORS README passwd-s3fs


%changelog
* Tue Oct 29 2013 Norifumi Sunaoka <sunaoka@pocari.org> - 1.73-1
- Initial build of 1.73.

* Thu May 31 2012 Corey Gilmore	<git@cfgci.com> - 1.61-1
- Initial build of 1.61. Disabled generation of useless debug package. Using spec from https://bugzilla.redhat.com/show_bug.cgi?id=725292

* Mon Aug 15 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-5
- Minor mod to get rid of macro in changelog

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-4
- Got rid of unnecessary buildroot cleaning

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-3
- Moved passwd-s3fs to docs folder

* Wed Jul 27 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-2
- Added docs to files section in spec
- Password file passwd-s3fs is installed as 0644 and changed in post

* Sun Jul 24 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-1
- Initial build

