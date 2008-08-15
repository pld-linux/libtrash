Summary:	Libraries to move files to a trash on delete
Summary(pl.UTF-8):	Biblioteka do automatycznego przenoszenia usuwanych plików do kosza
Name:		libtrash
Version:	3.2
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz
# Source0-md5:	56f7b54f50d760e4719f73b98cd8b43a
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-py24.patch
Patch2:		%{name}-noproc.patch
URL:		http://pages.stern.nyu.edu/~marriaga/software/libtrash/
BuildRequires:	/sbin/ldconfig
BuildRequires:	perl-base
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If configured to be preloaded by the dynamic linker, libtrash will
cause applications to transparently move files to a trash directory
instead of actually removing them. After the fake "remove", the files
are available in a directory structure similar as the old one.

%description -l pl.UTF-8
Po skonfigurowaniu tak, by była ładowana przez dynamiczny linker,
biblioteka libtrash powoduje, że aplikacje zamiast kasować przenoszą
pliki do specjalnego katalogu (kosza). Po tym "usunięciu" pliki są
dostępne w strukturze katalogów podobnej do tej sprzed usunięcia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

# no devel package
/sbin/ldconfig -N -n $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libtrash.so

%clean
rm -rf $RPM_BUILD_ROOT

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGE.LOG README config.txt TODO
%attr(755,root,root) %{_libdir}/libtrash.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libtrash.so.3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libtrash.conf
