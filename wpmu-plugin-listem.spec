%define		plugin	listem
Summary:	WordPressMU plugin to list alphabetically all public blogs in one page
Name:		wpmu-plugin-%{plugin}
Version:	0.1
Release:	0.3
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://wpmudev.org/download/738066546_Listem-%{version}.zip
# Source0-md5:	2cd9d80d118c60111a8359aa37e1cfc4
URL:		http://wpmudev.org/project/Listem
Patch0:		avatar-hook.patch
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	wpmu >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins
%define		_sysconfdir	/etc/webapps/wpmu

%description
Listem is a WordPress MU plugin developed off of List-All plug-in for
WordPress MU created by Andrew Billits

This is an updated version that allows ordering alphabetically as
well.

%prep
%setup -qc
install -d wpmudev
mv *.txt *.php wpmudev
%{__unzip} -qq Listem-NA.zip
# GPL v2
rm -f license.txt
mv {read-me,readme}.txt
%undos readme.txt
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{pluginsdir},%{_sysconfdir}}
cp -a listem.php $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{pluginsdir}/*.php
