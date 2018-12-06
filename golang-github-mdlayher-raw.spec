%global goipath         github.com/mdlayher/raw
%global commit          fa5ef3332ca961deab5782da07b1616fea8a9dd8

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Enables reading and writing data at the network driver level
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(golang.org/x/net/bpf)
BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{summary}

%package devel
Summary:        %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup


%install
%goinstall


%check
%gochecks

%files devel -f devel.file-list
%license LICENSE.md
%doc README.md

%changelog
* Fri Nov 30 2018 mskalick@redhat.com - 0-0.2.20181126gitfa5ef33
- Fix issues reported during review

* Mon Nov 26 2018 mskalick@redhat.com - 0-0.1.20181126gitfa5ef33
- First package for Fedora

