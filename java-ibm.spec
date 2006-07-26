%define __spec_install_post exit 0
Summary:	IBM Java virtual machine
Summary(pl):	Implementacja Javy firmy IBM
Name:		ibm-java
Version:	1.4.2
Release:	0.1
License:	IBM Binary Code License
Group:		Development/Languages/Java
%ifarch %{ix86}
Source0:	IBMJava2-JRE-142.tgz
# NoSource0-md5:	b316ee56d95121f47abd20a02c582431
%endif
%ifarch ppc
Source0:	IBMJava2-SDK-142.ppc.tgz
# NoSource0-md5:	4c9390f4488dc9ca84c6dfb2f0aab66e
%endif
NoSource:	0
URL:		http://www.ibm.com/developer/java/
Provides:	jar
Provides:	jdk = %{version}
Provides:	jre = %{version}
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         javadir         %{_libdir}/java
%define         jredir          %{_libdir}/java/jre
%define		sdkdir		%{_libdir}/java

%description
This is IBM's Java implementation.

%description -l pl
Pakiet zawiera implementacjê Javy firmy IBM.

%prep
%setup -q -n IBMJava2-%{_build_arch}-%(echo %{version} | tr -d .)

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{sdkdir},%{jredir},/etc/env.d}

cp -a bin include lib src.jar $RPM_BUILD_ROOT%{sdkdir}
cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{jredir}

ln -s %{jredir}/bin/java $RPM_BUILD_ROOT%{_bindir}
ln -s %{jredir}/bin/keytool $RPM_BUILD_ROOT%{_bindir}
ln -s %{jredir}/bin/policytool $RPM_BUILD_ROOT%{_bindir}
ln -s %{jredir}/bin/rmid $RPM_BUILD_ROOT%{_bindir}
ln -s %{jredir}/bin/rmiregistry $RPM_BUILD_ROOT%{_bindir}
ln -s %{jredir}/bin/tnameserv $RPM_BUILD_ROOT%{_bindir}

ln -s %{sdkdir}/bin/javac $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/appletviewer $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/extcheck $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/idlj $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/jar $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/jarsigner $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/javadoc $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/javah $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/javap $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/jdb $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/native2ascii $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/rmic $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/serialver $RPM_BUILD_ROOT%{_bindir}
ln -s %{sdkdir}/bin/HtmlConverter $RPM_BUILD_ROOT%{_bindir}

sed -i -e 's%#!/bin/sh%#!/bin/bash%g' $RPM_BUILD_ROOT%{jredir}/bin/* || :

%ifarch ppc
echo "JITC_PROCESSOR_TYPE=6" > $RPM_BUILD_ROOT/etc/env.d/JITC_PROCESSOR_TYPE
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%{javadir}
%ifarch ppc
%attr(644,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%endif
