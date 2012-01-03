# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/coursepaper
# catalog-date 2008-09-18 22:52:44 +0200
# catalog-license other-free
# catalog-version 2.0
Name:		texlive-coursepaper
Version:	2.0
Release:	2
Summary:	Prepare university course papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coursepaper
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Coursepaper is a class with which students can provide simple
course papers, in a uniform design to ease the task of marking.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coursepaper/coursepaper.cls
%doc %{_texmfdistdir}/doc/latex/coursepaper/coursepaper.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
