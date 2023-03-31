Name:		texlive-coursepaper
Version:	15878
Release:	2
Summary:	Prepare university course papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coursepaper
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coursepaper.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
