#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-stringr
Version  : 1.3.0
Release  : 50
URL      : https://cran.r-project.org/src/contrib/stringr_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stringr_1.3.0.tar.gz
Summary  : Simple, Consistent Wrappers for Common String Operations
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
fantastic 'stringi' package. All function and argument names (and positions)
    are consistent, all functions deal with "NA"'s and zero length vectors
    in the same way, and the output from one function is easy to feed into
    the input of another.

%prep
%setup -q -c -n stringr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522161642

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522161642
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library stringr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stringr/DESCRIPTION
/usr/lib64/R/library/stringr/INDEX
/usr/lib64/R/library/stringr/LICENSE
/usr/lib64/R/library/stringr/Meta/Rd.rds
/usr/lib64/R/library/stringr/Meta/data.rds
/usr/lib64/R/library/stringr/Meta/features.rds
/usr/lib64/R/library/stringr/Meta/hsearch.rds
/usr/lib64/R/library/stringr/Meta/links.rds
/usr/lib64/R/library/stringr/Meta/nsInfo.rds
/usr/lib64/R/library/stringr/Meta/package.rds
/usr/lib64/R/library/stringr/Meta/vignette.rds
/usr/lib64/R/library/stringr/NAMESPACE
/usr/lib64/R/library/stringr/NEWS.md
/usr/lib64/R/library/stringr/R/stringr
/usr/lib64/R/library/stringr/R/stringr.rdb
/usr/lib64/R/library/stringr/R/stringr.rdx
/usr/lib64/R/library/stringr/data/Rdata.rdb
/usr/lib64/R/library/stringr/data/Rdata.rds
/usr/lib64/R/library/stringr/data/Rdata.rdx
/usr/lib64/R/library/stringr/doc/index.html
/usr/lib64/R/library/stringr/doc/regular-expressions.R
/usr/lib64/R/library/stringr/doc/regular-expressions.Rmd
/usr/lib64/R/library/stringr/doc/regular-expressions.html
/usr/lib64/R/library/stringr/doc/stringr.R
/usr/lib64/R/library/stringr/doc/stringr.Rmd
/usr/lib64/R/library/stringr/doc/stringr.html
/usr/lib64/R/library/stringr/help/AnIndex
/usr/lib64/R/library/stringr/help/aliases.rds
/usr/lib64/R/library/stringr/help/figures/logo.png
/usr/lib64/R/library/stringr/help/paths.rds
/usr/lib64/R/library/stringr/help/stringr.rdb
/usr/lib64/R/library/stringr/help/stringr.rdx
/usr/lib64/R/library/stringr/html/00Index.html
/usr/lib64/R/library/stringr/html/R.css
/usr/lib64/R/library/stringr/htmlwidgets/lib/str_view.css
/usr/lib64/R/library/stringr/htmlwidgets/str_view.js
/usr/lib64/R/library/stringr/htmlwidgets/str_view.yaml
