%global tl_name dice
%global tl_revision 28501

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A font for die faces
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dice
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Metafont font that can produce die faces in 2D or with various 3D
effects.

