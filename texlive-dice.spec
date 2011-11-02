Name:		texlive-dice
Version:	20080607
Release:	1
Summary:	A font for die faces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A MetaFont font that can produce die faces in 2D or with
various 3D effects.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/dice/dice3d.mf
%{_texmfdistdir}/fonts/tfm/public/dice/dice3d.tfm
%doc %{_texmfdistdir}/doc/fonts/dice/dice3d.dvi
%doc %{_texmfdistdir}/doc/fonts/dice/dice3d.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
