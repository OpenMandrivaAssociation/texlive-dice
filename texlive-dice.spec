Name:		texlive-dice
Version:	28501
Release:	2
Summary:	A font for die faces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dice
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
