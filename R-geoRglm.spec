%global packname  geoRglm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.2
Release:          1
Summary:          geoRglm - a package for generalised linear spatial models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/geoRglm_0.9-2.tar.gz
Requires:         R-geoR R-stats 
Requires:         R-coda 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-geoR R-stats
BuildRequires:    R-coda 

%description
Functions for inference in generalised linear spatial models. The
posterior and predictive inference is based on Markov chain Monte Carlo
methods. Package geoRglm is an extension to the package geoR, which must
be installed first.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

