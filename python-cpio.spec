%if !(0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

Name:           python-cpio
Version:        0.1
Release:        16%{?dist}
Summary:        A Python module for accessing cpio archives

Group:          Development/Languages
License:        LGPLv2+
URL:            http://developer.berlios.de/projects/python-cpio/
Source0:        http://download.berlios.de/python-cpio/python-cpio-0.1.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel

%description
This is a Python module for accessing cpio archives.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING.lib README TODO
%{python_sitelib}/cpioarchive.py*
%if 0%{?fedora} >= 9 || 0%{?rhel} >= 6
%{python_sitelib}/*.egg-info
%endif


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 8 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-10
- Update for new python guidelines
- Fix spec so that EPEL-6 will build

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-7
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1-6
- fix license tag

* Tue Apr  1 2008 José Matos <jamatos[AT]fc.up.pt> - 0.1-5
- Add egg-info for F9+.

* Tue Aug 28 2007 José Matos <jamatos[AT]fc.up.pt> - 0.1-4
- License fix, rebuild for devel (F8).

* Tue Dec 12 2006 José Matos <jamatos[AT]fc.up.pt> - 0.1-3
- Rebuild for python 2.5.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.1-2
- Rebuild for FC6.

* Tue Jan  3 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1-1
- Initial RPM release
