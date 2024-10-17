Name:		texlive-lua-uca
Version:	71218
Release:	1
Summary:	Unicode Collation Algorithm library for Lua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lua-uca
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Lua-UCA library provides basic support for Unicode
Collation Algorithm in Lua. It can be used to sort arrays of
strings according to rules of particular languages. It can be
used in other Lua projects that need to sort text in a language
dependent way, like indexing processors, bibliographic
generators, etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/support/lua-uca
%{_texmfdistdir}/scripts/lua-uca
%doc %{_texmfdistdir}/doc/support/lua-uca

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
