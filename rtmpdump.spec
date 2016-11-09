%global commit0 fa8646daeb19dfd12c181f7d19de708d623704c0
%global date 20151223
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           rtmpdump
Version:        2.4
Release:        8%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Epoch:          1
Summary:        Toolkit for RTMP streams

# The tools are GPLv2+. The library is LGPLv2+, see below.
License:        GPLv2+
URL:            http://%{name}.mplayerhq.hu/
Source0:        http://git.ffmpeg.org/gitweb/%{name}.git/snapshot/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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
%setup -qn %{name}-%{shortcommit0}

%build
make SYS=posix CRYPTO=GNUTLS SHARED=yes OPT="%{optflags}"

%install
make CRYPTO=GNUTLS SHARED=yes DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} libdir=%{_libdir} install
find %{buildroot} -name "*.a" -delete

%post -n librtmp -p /sbin/ldconfig

%postun -n librtmp -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_bindir}/rtmpdump
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files -n librtmp
%{!?_licensedir:%global license %%doc}
%license librtmp/COPYING
%doc ChangeLog
%{_libdir}/librtmp.so.1

%files -n librtmp-devel
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%{_mandir}/man3/librtmp.3*

%changelog
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
