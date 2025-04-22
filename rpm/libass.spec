%define keepstatic 1
Name:           libass
Version:        0.17.1
Release:        1%{?dist}
Summary:        Portable library for SSA/ASS subtitles rendering
License:        ISC
URL:            https://github.com/libass
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  nasm
BuildRequires:  pkgconfig(fontconfig) >= 2.10.92
BuildRequires:  pkgconfig(freetype2) >= 9.10.3
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.5
BuildRequires:  pkgconfig(libpng) >= 1.2.0
BuildRequires:  make

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-static
Summary:        Development files for %{name}

%description    devel-static
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
./autogen.sh
%configure --enable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license COPYING
%doc Changelog
%{_libdir}/*.so.9*

%files devel
%{_includedir}/ass
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%files devel-static
%{_libdir}/libass.*a
