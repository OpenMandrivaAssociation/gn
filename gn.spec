Summary:	The GN build tool
Name:		gn
Version:	20200209
Release:	1
License:	GPLv3+
Group:		Development/Other
Url:		http://chromium.googlesource.com/
# git clone https://gn.googlesource.com/gn
# tar cf gn-%{version}.tar gn
# zstd -19 --rm *.tar
# gn can't be built from a "git archive"-d tarball, must package .git
# (and even --depth 1 won't work)
Source0:	gn-%{version}.tar.zst
Source100:	%{name}.rpmlintrc
BuildRequires:	python
BuildRequires:	ninja
BuildRequires:	atomic-devel
BuildRequires:	git-core

%description
The gn build tool, needed to build Chromium

%prep
%autosetup -p1 -n %{name}
python build/gen.py --no-static-libstdc++

%build
%ninja_build -C out

%install
install -c -D -m 755 out/gn %{buildroot}%{_bindir}/gn

%check
out/gn_unittests

%files
%{_bindir}/%{name}
