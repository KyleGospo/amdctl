Name:           amdctl
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Set P-State voltages and clock speeds on recent AMD CPUs on Linux

License:        GPLv3
URL:            https://github.com/KyleGospo/amdctl

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  make
BuildRequires:  gcc

%description
Set P-State voltages and clock speeds on recent AMD CPUs on Linux.
Disclaimer: This software can damage your hardware, use at your own risk.

%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 ./%{name} %{buildroot}%{_sbindir}/

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}

%changelog
{{{ git_dir_changelog }}}
