Name:           opencl-icd-loader
Version:        2.2.9
Release:        1%{?dist}
Summary:        OpenCL ICD loader

License:        BSD
URL:            https://forge.imag.fr/projects/ocl-icd/
Source0:        https://forge.imag.fr/frs/download.php/716/ocl-icd-%{version}.tar.gz

BuildRequires:  opencl-headers
BuildRequires:  ruby


%description
OpenCL implementations are provided as ICD (Installable Client Driver). An
OpenCL program can use several ICD thanks to the use of an ICD Loader as
provided by this project. This free ICD Loader can load any (free or non free)
ICD.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n ocl-icd-%{version}


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

rm -rf %{buildroot}%{_datadir}/doc/
mkdir -p %{buildroot}%{_sysconfdir}/OpenCL/vendors/


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING NEWS README
%{_sysconfdir}/OpenCL/
%{_libdir}/*.so.*

%files devel
%doc ocl_icd_bindings.c
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man7/*.7*


%changelog
* Fri Oct 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.2.9-1
- Public release
