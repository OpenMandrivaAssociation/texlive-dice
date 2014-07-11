# revision 28501
# category Package
# catalog-ctan /fonts/dice
# catalog-date 2012-12-11 20:24:18 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-dice
Version:	20121211
Release:	7
Summary:	A font for die faces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A Metafont font that can produce die faces in 2D or with
various 3D effects.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/dice/dice3d.mf
%{_texmfdistdir}/fonts/tfm/public/dice/dice3d.tfm
%doc %{_texmfdistdir}/doc/fonts/dice/dice3d.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
