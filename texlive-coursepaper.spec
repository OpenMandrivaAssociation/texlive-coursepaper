%global tl_name coursepaper
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Prepare university course papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coursepaper
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Coursepaper is a class with which students can provide simple course
papers, in a uniform design to ease the task of marking.

