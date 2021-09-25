%define debug_package %{nil}

Summary:	The GN build tool
Name:		gn
Version:	20210925
Release:	1
License:	GPLv3+
Group:		Development/Other
Url:		http://chromium.googlesource.com/
# git clone https://gn.googlesource.com/gn
# tar cf gn-%{version}.tar gn
# zstd --ultra -22 --rm *.tar
# gn can't be built from a "git archive"-d tarball, must package .git
# (and even --depth 1 won't work)
Source0:	gn-%{version}.tar.zst
Source100:	%{name}.rpmlintrc
BuildRequires:	python
BuildRequires:	ninja
BuildRequires:	atomic-devel
BuildRequires:	git-core
# FIXME as of clang 10.0.0-20200207 crashes on startup if
# built with clang on armv7hnl. It works perfectly on the
# other arches and on armv7hnl built with gcc...
%ifarch %{arm}
BuildRequires:	gcc gcc-c++
%endif

%description
The gn build tool, needed to build Chromium.

%prep
%autosetup -p1 -n %{name}

%build
%set_build_flags
%ifarch %{arm}
export CC=gcc
export CXX=g++
%endif
python build/gen.py \
	--use-lto \
	--no-static-libstdc++

%ninja_build -C out

%install
install -c -D -m 755 out/gn %{buildroot}%{_bindir}/gn

%check
out/gn_unittests

%files
%{_bindir}/%{name}
