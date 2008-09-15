%define up_name	ioxml
%define name	ocaml-%{up_name}
%define version	0.8
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    XML parsers generator
Group:      Development/Other
License:    MIT
URL:        http://cristal.inria.fr/~ddr/IoXML/
Source0:    http://cristal.inria.fr/~ddr/IoXML/distrib/src/%{up_name}-%{version}.tgz
BuildRequires:  ocaml
BuildRequires:  camlp5
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
IoXML is a Camlp5 syntax extension for OCaml mli and ml files which generates
XML parsers and printers for all types you define. 

%prep
%setup -q -n %{up_name}-%{version}

%build
make all

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}/ocaml/camlp5
make install LIBDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE CHANGES
%{_libdir}/ocaml/camlp5/*

