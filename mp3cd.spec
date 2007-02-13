#
# Conditional build:
%bcond_with	test	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	MP3, Ogg, and WAV files to audio CDs converter
Summary(pl.UTF-8):	Konwerter plików MP3, Ogg i WAV do formatu audio CD
Name:		mp3cd
Version:	1.22.0
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://outflux.net/software/pkgs/mp3cd/download/%{name}-1.022.tar.gz
# Source0-md5:	c4381cbc00455b1da30e0a2d77f44dba
URL:		http://outflux.net/software/pkgs/mp3cd/
BuildRequires:	rpm-perlprov
Requires:	cdrdao
Requires:	cdrtools
Requires:	mpg123
Requires:	normalize
Requires:	sox
Requires:	vorbis-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3cd is a Perl script that normalizes and burns MP3, Ogg, and WAV
files to audio CDs.

%description -l pl.UTF-8
mp3cd jest skryptem Perla, który normalizuje i nagrywa pliki MP3, Ogg
i WAV w formacie audio CD.

%prep
%setup -q -n %{name}-1.022

%build
%{__perl} Makefile.PL
%{__make}

%{?with_test:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install scripts/mp3cd $RPM_BUILD_ROOT%{_bindir}
install blib/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
