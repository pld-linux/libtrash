Summary:        Libraries to move files to a trash on delete
Summary(pl):    Biblioteka do automatycznego przenoszenia usuwanych plików do kosza
Name:		libtrash
Version:        1.1
Release:        1
License:	GPL
Group:		Libraries
Source0:	http://www.m-arriaga.net/software/libtrash/%{name}-%{version}.tgz
Patch0:		%{name}-Makefile.patch
URL:		http://www.m-arriaga.net/software/libtrash/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If configured to be preloaded by the dynamic linker, libtrash will
cause applications to transparently move files to a trash directory
instead of actually removing them. After the fake "remove", the files
are available in a directory structure similar as the old one.

%description -l pl
Po skonfigurowaniu tak, by by³a ³adowana przez dynamiczny linker,
biblioteka libtrash powoduje, ¿e aplikacje zamiast kasowaæ przenosz±
pliki do specjalnego katalogu (kosza). Po tym "usuniêciu" pliki s±
dostêpne w strukturze katalogów podobnej do tej sprzed usuniêcia.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}

%{__make} install \
	INSTLIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	SYSCONFFILE=$RPM_BUILD_ROOT%{_sysconfdir}/libtrash.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE.LOG README config.txt
%attr(755,root,root) %{_libdir}/libtrash.so.*.*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/libtrash.conf

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig
