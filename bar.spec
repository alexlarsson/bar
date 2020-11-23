%define _source_payload w9.gzdio
%define _binary_payload w9.gzdio

Name:           bar
Version:        1.0.0
Release:        1%{?dist}
Summary:        User of foo
License:        MIT

Source: https://github.com/alexlarsson/bar/releases/download/1.0.0/bar-1.0.0.tar.gz

BuildRequires: foo-devel

%description
User of foo

%prep
%setup -q -n %{name}-%{version}

%build
make CFLAGS=-g

%install
make install DESTDIR=%{buildroot} BINDIR=%{_bindir}

%files
%{_bindir}/bar

%changelog
* Wed Nov 18 2020 Alexander Larsson <alexl@redhat.com> - 1.0.0.-1
- FOO THE BARS!
