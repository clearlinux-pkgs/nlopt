#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nlopt
Version  : 2.7.1
Release  : 36
URL      : https://github.com/stevengj/nlopt/archive/v2.7.1/nlopt-2.7.1.tar.gz
Source0  : https://github.com/stevengj/nlopt/archive/v2.7.1/nlopt-2.7.1.tar.gz
Summary  : nonlinear optimization libary
Group    : Development/Tools
License  : LGPL-2.1 MIT zlib-acknowledgement
Requires: nlopt-data = %{version}-%{release}
Requires: nlopt-filemap = %{version}-%{release}
Requires: nlopt-lib = %{version}-%{release}
Requires: nlopt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : guile-dev
BuildRequires : octave-dev
BuildRequires : pypi(numpy)
BuildRequires : python3
BuildRequires : python3-dev

%description
"Subplex" gradient-free minimization code, based on a variant of
Nelder-Mead simplex by Tom Rowan.

%package data
Summary: data components for the nlopt package.
Group: Data

%description data
data components for the nlopt package.


%package dev
Summary: dev components for the nlopt package.
Group: Development
Requires: nlopt-lib = %{version}-%{release}
Requires: nlopt-data = %{version}-%{release}
Provides: nlopt-devel = %{version}-%{release}
Requires: nlopt = %{version}-%{release}

%description dev
dev components for the nlopt package.


%package filemap
Summary: filemap components for the nlopt package.
Group: Default

%description filemap
filemap components for the nlopt package.


%package lib
Summary: lib components for the nlopt package.
Group: Libraries
Requires: nlopt-data = %{version}-%{release}
Requires: nlopt-license = %{version}-%{release}
Requires: nlopt-filemap = %{version}-%{release}

%description lib
lib components for the nlopt package.


%package license
Summary: license components for the nlopt package.
Group: Default

%description license
license components for the nlopt package.


%prep
%setup -q -n nlopt-2.7.1
cd %{_builddir}/nlopt-2.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647639416
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :

%install
export SOURCE_DATE_EPOCH=1647639416
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nlopt
cp %{_builddir}/nlopt-2.7.1/COPYING %{buildroot}/usr/share/package-licenses/nlopt/6bde78f7f5f4dc57b34bdcfab2484a5aff2da46e
cp %{_builddir}/nlopt-2.7.1/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/cd23454a0abd93b92c357ee22524f583364fbc78
cp %{_builddir}/nlopt-2.7.1/src/algs/ags/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/4d078684fdcb8fdac6f1b1aef151e542e4a483d1
cp %{_builddir}/nlopt-2.7.1/src/algs/bobyqa/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/d0a422e23498cf10eba733d4b7882a3484ee510a
cp %{_builddir}/nlopt-2.7.1/src/algs/cobyla/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/9990b0b02ee9570457a9d860b6e37ae06a1f9dc7
cp %{_builddir}/nlopt-2.7.1/src/algs/direct/COPYING %{buildroot}/usr/share/package-licenses/nlopt/0c65a98a772b9aa5d3b6bf331102ab6ad8d0f698
cp %{_builddir}/nlopt-2.7.1/src/algs/esch/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/1be95ecfc4cd8e5f28390a8566884eb61b22001a
cp %{_builddir}/nlopt-2.7.1/src/algs/luksan/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/6907a52aa4c1680fd7bd7a3cf1da49002abc9c74
cp %{_builddir}/nlopt-2.7.1/src/algs/newuoa/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/8e9752a28519de55490b55e7fd282c5ee91be74f
cp %{_builddir}/nlopt-2.7.1/src/algs/slsqp/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/2dacd8b2f1e11bcd431639c4b40256c9e18d2c82
cp %{_builddir}/nlopt-2.7.1/src/algs/stogo/COPYRIGHT %{buildroot}/usr/share/package-licenses/nlopt/077253c67533010dac1211c9a46589df20d874cb
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/octave/6.4.0/site/oct/x86_64-generic-linux-gnu/nlopt_optimize.oct

%files data
%defattr(-,root,root,-)
/usr/share/octave/6.4.0/site/m/NLOPT_AUGLAG.m
/usr/share/octave/6.4.0/site/m/NLOPT_AUGLAG_EQ.m
/usr/share/octave/6.4.0/site/m/NLOPT_GD_MLSL.m
/usr/share/octave/6.4.0/site/m/NLOPT_GD_MLSL_LDS.m
/usr/share/octave/6.4.0/site/m/NLOPT_GD_STOGO.m
/usr/share/octave/6.4.0/site/m/NLOPT_GD_STOGO_RAND.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_CRS2_LM.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT_L.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT_L_NOSCAL.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT_L_RAND.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT_L_RAND_NOSCAL.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_DIRECT_NOSCAL.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_ESCH.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_ISRES.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_MLSL.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_MLSL_LDS.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_ORIG_DIRECT.m
/usr/share/octave/6.4.0/site/m/NLOPT_GN_ORIG_DIRECT_L.m
/usr/share/octave/6.4.0/site/m/NLOPT_G_MLSL.m
/usr/share/octave/6.4.0/site/m/NLOPT_G_MLSL_LDS.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_AUGLAG.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_AUGLAG_EQ.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_CCSAQ.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_LBFGS.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_LBFGS_NOCEDAL.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_MMA.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_SLSQP.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_TNEWTON.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_TNEWTON_PRECOND.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_TNEWTON_PRECOND_RESTART.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_TNEWTON_RESTART.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_VAR1.m
/usr/share/octave/6.4.0/site/m/NLOPT_LD_VAR2.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_AUGLAG.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_AUGLAG_EQ.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_BOBYQA.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_COBYLA.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_NELDERMEAD.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_NEWUOA.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_NEWUOA_BOUND.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_PRAXIS.m
/usr/share/octave/6.4.0/site/m/NLOPT_LN_SBPLX.m
/usr/share/octave/6.4.0/site/m/nlopt_minimize.m
/usr/share/octave/6.4.0/site/m/nlopt_minimize_constrained.m

%files dev
%defattr(-,root,root,-)
/usr/include/nlopt.f
/usr/include/nlopt.h
/usr/include/nlopt.hpp
/usr/lib64/cmake/nlopt/NLoptConfig.cmake
/usr/lib64/cmake/nlopt/NLoptConfigVersion.cmake
/usr/lib64/cmake/nlopt/NLoptLibraryDepends-relwithdebinfo.cmake
/usr/lib64/cmake/nlopt/NLoptLibraryDepends.cmake
/usr/lib64/libnlopt.so
/usr/lib64/pkgconfig/nlopt.pc
/usr/share/man/man3/nlopt.3
/usr/share/man/man3/nlopt_minimize.3
/usr/share/man/man3/nlopt_minimize_constrained.3

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-nlopt

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnlopt.so.0
/usr/lib64/libnlopt.so.0.11.1
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nlopt/077253c67533010dac1211c9a46589df20d874cb
/usr/share/package-licenses/nlopt/0c65a98a772b9aa5d3b6bf331102ab6ad8d0f698
/usr/share/package-licenses/nlopt/1be95ecfc4cd8e5f28390a8566884eb61b22001a
/usr/share/package-licenses/nlopt/2dacd8b2f1e11bcd431639c4b40256c9e18d2c82
/usr/share/package-licenses/nlopt/4d078684fdcb8fdac6f1b1aef151e542e4a483d1
/usr/share/package-licenses/nlopt/6907a52aa4c1680fd7bd7a3cf1da49002abc9c74
/usr/share/package-licenses/nlopt/6bde78f7f5f4dc57b34bdcfab2484a5aff2da46e
/usr/share/package-licenses/nlopt/8e9752a28519de55490b55e7fd282c5ee91be74f
/usr/share/package-licenses/nlopt/9990b0b02ee9570457a9d860b6e37ae06a1f9dc7
/usr/share/package-licenses/nlopt/cd23454a0abd93b92c357ee22524f583364fbc78
/usr/share/package-licenses/nlopt/d0a422e23498cf10eba733d4b7882a3484ee510a
