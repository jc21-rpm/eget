%define debug_package %{nil}

%global gh_user zyedidia

Name:           eget
Version:        1.3.4
Release:        1%{?dist}
Summary:        Easily install prebuilt binaries from GitHub.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
Eget is the best way to easily get pre-built binaries for your favorite tools.
It downloads and extracts pre-built binaries from releases on GitHub.

%prep
%setup -q -n %{name}-%{version}

%build
make build

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc man/eget.md LICENSE

%changelog
* Tue Sep 10 2024 Jamie Curnow <jc@jc21.com> 1.3.4-1
- v1.3.4
