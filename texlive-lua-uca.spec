%global tl_name lua-uca
%global tl_revision 74807

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1e
Release:	%{tl_revision}.1
Summary:	Unicode Collation Algorithm library for Lua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/lualibs/lua-uca
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uca.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Lua-UCA library provides basic support for Unicode Collation
Algorithm in Lua. It can be used to sort arrays of strings according to
rules of particular languages. It can be used in other Lua projects that
need to sort text in a language dependent way, like indexing processors,
bibliographic generators, etc.

