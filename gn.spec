%define date 20170114

Summary:	The GN build tool
Name:		gn
Version:	20190403
Release:	1
License:	GPLv3+
Group:		Development/Other
Url:		http://chromium.googlesource.com/
# git clone https://chromium.googlesource.com/chromium/src/tools/gn 
Source0:	gn-%{date}.tar.xz
# 
# git clone https://chromium.googlesource.com/chromium/src/base
Source1:	base-%{date}.tar.xz
# https://chromium.googlesource.com/chromium/src/build
Source2:	build-%{date}.tar.xz
# https://chromium.googlesource.com/chromium/src/build/config
Source3:	config-%{date}.tar.xz
# https://chromium.googlesource.com/chromium/testing/gtest
Source4:	gtest-%{date}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	python
BuildRequires:	ninja
BuildRequires:	atomic-devel

%description
The gn build tool, needed to build Chromium

%prep
%setup -qc

mkdir tools
mv gn tools
tar x -f %{SOURCE1}
tar x -f %{SOURCE2}
tar x -C build -f %{SOURCE3}
mkdir testing
tar x -C testing -f %{SOURCE4}

%apply_patches

%build
cd tools/gn
2to3 -w bootstrap/bootstrap.py
python ./bootstrap/bootstrap.py -s

%install
install -c -D -m 755 out/Release/gn %{buildroot}%{_bindir}/gn

%files
%{_bindir}/%{name}
