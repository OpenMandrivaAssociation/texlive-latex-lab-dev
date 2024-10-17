Name:		texlive-latex-lab-dev
Version:	64899
Release:	2
Summary:	LaTeX laboratory: Development pre-release
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-lab-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a testing release for upcoming changes to
the latex-lab bundle, which provides a route for additions to
the LaTeX kernel to be stablised. It accompanies the
pre-testing kernel code (latex-base-dev), and is intended for
testing by knowledgeable users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/latex-lab
%doc %{_texmfdistdir}/source/latex-dev/latex-lab/latex-lab.ins
%doc %{_texmfdistdir}/source/latex-dev/latex-lab/latex-lab-testphase.dtx
%doc %{_texmfdistdir}/source/latex-dev/latex-lab/latex-lab-new-or.dtx
%doc %{_texmfdistdir}/source/latex-dev/latex-lab/latex-lab-footnotes.dtx
%doc %{_texmfdistdir}/source/latex-dev/latex-lab/documentmetadata-support.dtx
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/latex-lab
%{_texmfdistdir}/tex/latex-dev/latex-lab/tagpdf-latex-lab-testphase.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/phase-II-latex-lab-testphase.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/phase-I-latex-lab-testphase.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/new-or-latex-lab-testphase.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/latex-lab-testphase-new-or.sty
%{_texmfdistdir}/tex/latex-dev/latex-lab/latex-lab-footnotes.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/latex-lab-footmisc.ltx
%{_texmfdistdir}/tex/latex-dev/latex-lab/documentmetadata-support.ltx
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/usage-of-kern-kern.txt
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/usage-of-footnotetext.txt
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/usage-of-footnotemark.txt
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/latex-lab-testphase.pdf
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/latex-lab-new-or.pdf
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/latex-lab-footnotes.pdf
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/documentmetadata-support-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/documentmetadata-support-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/documentmetadata-support-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/documentmetadata-support-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/latex-lab/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
