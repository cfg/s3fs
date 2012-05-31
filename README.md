s3fs
====

CentOS/RH RPMs for s3fs/FuseOverAmazon from <http://code.google.com/p/s3fs/>

Based off the [spec file](http://kad.fedorapeople.org/packages/s3fs/s3fs.spec) created by [Jorge A Gallegos](http://kad.fedorapeople.org/), referenced at <https://bugzilla.redhat.com/show_bug.cgi?id=725292>

Includes RPMs for fuse-2.8.5.

Tested on x64 CentOS 5.7 and 5.8

Building fresh RPMs
-------------------
My notes, not step-by-step instructions.

Set up your build environment

    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

If you don't have a .rpmmacros file, create one

    cp ~/.rpmmacros ~/.rpmmacros.bak ; echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros


Build fuse-2.8.5 RPMs
---------------------
Uses [fuse-2.8.5-99.vitki.01.el5.src.rpm](https://rpm.vitki.net/pub/SRPMS/fuse-2.8.5-99.vitki.01.el5.src.rpm) from [rpm.vitki.net](https://rpm.vitki.net/pub/SRPMS/)
Rebuild:

    cd ~/rpmbuild/SRPMS
    rpmbuild --rebuild fuse-2.8.5-99.vitki.01.el5.src.rpm

And install

    cd ~/rpmbuild/RPMS/$HOSTTYPE/
    rpm -Uvh fuse-2.8.5-99.vitki.01.el5.$HOSTTYPE.rpm fuse-devel-2.8.5-99.vitki.01.el5.$HOSTTYPE.rpm fuse-libs-2.8.5-99.vitki.01.el5.$HOSTTYPE.rpm


Build the s3fs RPMs
-------------------

Build the RPMs

    rpmbuild -ba --buildroot ~/rpmbuild/BUILDROOT/ ~/rpmbuild/SPECS/s3fs.spec

And install

    rpm -Uvh ~/rpmbuild/RPMS/$HOSTTYPE/s3fs-1.61-5.$HOSTTYPE.rpm