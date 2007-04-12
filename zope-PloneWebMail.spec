%define product		PloneWebMail
%define version		1.0
%define release		4

%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	PloneWebMail is an IMAP email client for Plone
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plonewebmail.openprojects.it/Members/admin/PloneWebMail-%{version}final.tar.bz2
URL:		http://plonewebmail.openprojects.it
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}

Provides:	plone-PloneWebMail == %{version}
Obsoletes:	plone-PloneWebMail

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*



