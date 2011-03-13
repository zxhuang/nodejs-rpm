Name:           nodejs
Version:        0.4.2
Release:        1%{?dist}
Summary:        Evented I/O for V8 JavaScript
Group:          Server Development
License:        MIT
URL:            http://nodejs.org/
Source0:        node-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gcc-c++ >= 4.1
BuildRequires:  python
BuildRequires:  libstdc++-devel
BuildRequires:  openssl-devel
 
%description
Node.js is a server-side JavaScript environment that uses an asynchronous 
event-driven model. This allows Node.js to get excellent performance based 
on the architectures of many Internet applications.
 
%package devel
Summary:        Node.js addon development files
Group:          Server Development
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains files for Node.js addons development.
 
%clean
rm -rf %{buildroot}
 
%prep
%setup -q -n node-v%{version}
 
%build
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
./configure --prefix=%{_prefix}
%__make %{?_smp_mflags}
 
%install
%__make DESTDIR=%{buildroot} install
 
%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE
%attr(755,root,root) %{_bindir}/node
%attr(755,root,root) %{_bindir}/node-waf
%attr(755,root,root) /usr/lib/node/wafadmin
%attr(755,root,root) /usr/lib/pkgconfig/nodejs.pc
%{_mandir}/man1/node.1*
 
%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/node
%{_includedir}/node/*.h

%changelog
* Sat Mar 12 2011 Zeke Huang <zxhuang at, gmail.com> 0.4.2-1
- Added Makefile and nodejs.spec for auto creating Node.js rpm.

