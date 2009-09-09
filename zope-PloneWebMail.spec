%define Product PloneWebMail
%define product plonewebmail
%define name    zope-%{Product}
%define version 1.0
%define release %mkrel 9

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	IMAP email client for Plone
License:	GPL
Group:		System/Servers
URL:		http://plonewebmail.openprojects.it
Source:		http://plonewebmail.openprojects.it/Members/admin/PloneWebMail-%{version}final.tar.bz2
Requires:	zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
PloneWebMail is an IMAP (POP3 support coming soon) email client for Plone.
It's very simple and the features are basic :

- Read IMAP messages with attachments
- Send & forward messages with attachments (plain text & HTML)
- IMAP folders management
- copy/move IMAP messages
- Basic addressbook
- i18n implementation


%prep
%setup -c -q
find -type f -name '.*' | xargs rm -f
find -type d -name '.xvpics' | xargs rm -rf

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
