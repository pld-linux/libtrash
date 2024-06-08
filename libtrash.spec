Summary:	Libraries to move files to a trash on delete
Summary(pl.UTF-8):	Biblioteka do automatycznego przenoszenia usuwanych plików do kosza
Name:		libtrash
Version:	3.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz
# Source0-md5:	7eeda8187327588ad32bbcb80f33e796
URL:		https://pages.stern.nyu.edu/~marriaga/software/libtrash/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no devel package
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtrash.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md TODO config.txt
%attr(755,root,root) %{_libdir}/libtrash.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libtrash.so.3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libtrash.conf
