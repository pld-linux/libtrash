Summary:	Libraries to move files to a trash on delete
Summary(pl):	Biblioteka do automatycznego przenoszenia usuwanych plik�w do kosza
Name:		libtrash
Version:	2.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz
# Source0-md5:	c335bf506cfe2433d16df71dc29acfc3
Patch0:		%{name}-Makefile.patch
URL:		http://pages.stern.nyu.edu/~marriaga/software/libtrash/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If configured to be preloaded by the dynamic linker, libtrash will
cause applications to transparently move files to a trash directory
instead of actually removing them. After the fake "remove", the files
are available in a directory structure similar as the old one.

%description -l pl
Po skonfigurowaniu tak, by by�a �adowana przez dynamiczny linker,
biblioteka libtrash powoduje, �e aplikacje zamiast kasowa� przenosz�
pliki do specjalnego katalogu (kosza). Po tym "usuni�ciu" pliki s�
dost�pne w strukturze katalog�w podobnej do tej sprzed usuni�cia.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}

%{__make} install \
	INSTLIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	SYSCONFFILE=$RPM_BUILD_ROOT%{_sysconfdir}/libtrash.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGE.LOG README config.txt TODO
%attr(755,root,root) %{_libdir}/libtrash.so.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libtrash.conf
