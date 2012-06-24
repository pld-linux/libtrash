Summary:        Libraries to move files to a trash on delete
Summary(pl):    Biblioteka do automatycznego przenoszenia  usuwanych  pliki do kosza
Name:		libtrash
Version:        0.9
Release:        1
License:	GPL
Group:		System Environment/Libraries
Provides:	libtrash
Autoreqprov:	on
Source0:	%{name}-%{version}.tgz
Patch0:		%{name}-Makefile.patch
URL:		http://www.m-arriaga.net/software/libtrash/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If configured to be preloaded by the dynamic linker, libtrash will
cause applications to transparently move files to a trash directory
instead of actually removing them. After the fake "remove", the files
are available in a directory structure similar as the old one.

%description -l pl
Jesli konfiguracja byla preladowana przez dynamiczny linker
libtrash spowoduje ze aplikacje  przesuwajac plik 
do katalogu smietnika niezaleznie od aktaulnego usunieci jej
po usunieciu pliki bede dostepne w strukturze katalogow dokladnie jak przed usunieciem.


%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_sysconfdir}}
%{__make} install INSTLIBDIR=$RPM_BUILD_ROOT%{_libdir} SYSCONFFILE=$RPM_BUILD_ROOT%{_sysconfdir}/libtrash.conf

gzip -9nf CHANGE.LOG README config.txt
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_libdir}/libtrash*
%{_sysconfdir}/libtrash.conf

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig
