%global commit 6f6bb1353fc84f4cc37138baa99f586750028a01
%global date 20240301
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} >= 42
%global _sbindir %{_bindir}
%endif

Name:           rtmpdump
Version:        2.6^%{date}git%{shortcommit}
Release:        2%{?dist}
Epoch:          1
Summary:        Toolkit for RTMP streams
# The tools are GPLv2+. The library is LGPLv2+, see below.
License:        GPLv2+
URL:            https://%{name}.mplayerhq.hu/

Source0:        %{name}-%{shortcommit}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  nettle-devel
BuildRequires:  zlib-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp
Summary:        Support library for RTMP streams
License:        LGPLv2+

%description -n librtmp
librtmp is a support library for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp-devel
Summary:        Files for librtmp development
License:        LGPLv2+
Requires:       librtmp%{?_isa} = %{?epoch}:%{version}-%{release}

%description -n librtmp-devel
librtmp is a support library for RTMP streams. The librtmp-devel package
contains include files needed to develop applications using librtmp.

%prep
%autosetup -n %{name}

%build
make SYS=posix CRYPTO=GNUTLS SHARED=yes OPT="%{optflags}"

%install
make \
    CRYPTO=GNUTLS \
    SHARED=yes \
    DESTDIR=%{buildroot} \
    prefix=%{_prefix} \
    mandir=%{_mandir} \
    libdir=%{_libdir} \
%if 0%{?fedora} >= 42
    sbindir=%{_bindir} \
%endif
    install
find %{buildroot} -name "*.a" -delete

%files
%license COPYING
%doc README
%{_bindir}/rtmpdump
%if 0%{?fedora} >= 42
%{_bindir}/rtmpsrv
%{_bindir}/rtmpgw
%{_bindir}/rtmpsuck
%else
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsuck
%endif
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files -n librtmp
%license librtmp/COPYING
%doc ChangeLog
%{_libdir}/librtmp.so.1

%files -n librtmp-devel
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%{_mandir}/man3/librtmp.3*

%changelog
* Fri Mar 14 2025 Simone Caronni <negativo17@gmail.com> - 1:2.6^20240301git6f6bb13-2
- Update package to new versioning guidelines.
- Update URL.
- Adjust for Fedora 42's unified bin directory.

* Wed Apr 03 2024 Simone Caronni <negativo17@gmail.com> - 1:2.6-1.20240301git6f6bb13
- Update to latest 2.6 release.
- Clean up SPEC file.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1:2.4-9.20151223gitfa8646d
- Add GCC build requirement.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:2.4-8.20151223gitfa8646d
- Update release version according to packaging guidelines.
- Update source location.

* Fri Aug 05 2016 Simone Caronni <negativo17@gmail.com> - 1:2.4-7.fa8646d
- Update to latest sources.

* Tue Apr 19 2016 Simone Caronni <negativo17@gmail.com> - 2.4-6.gita107cef
- Remove group.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 2.4-5.git.a107cef
- Update to latest sources.
- Add license macro.
- Update URLs as per packaging guidelines.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 2.4-3.20131205.gitdc76f0a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
