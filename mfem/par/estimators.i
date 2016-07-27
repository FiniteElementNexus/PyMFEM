%module estimators
%{
#include "numpy/arrayobject.h"
#include "fem/estimators.hpp"
#define MFEM_USE_MPI  
%}
%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);

// initialization required to return numpy array from SWIG
%init %{
import_array();
%}

%import "array.i"
%import "vector.i"
%import "fespace.i"
%import "bilinearform.i"
%import "gridfunc.i"

%ignore mfem::ZienkiewiczZhuEstimator::ZienkiewiczZhuEstimator(
				       BilinearFormIntegrator &integ,
				       GridFunction &sol,
				       FiniteElementSpace *flux_fes);
%ignore mfem::ZienkiewiczZhuEstimator::ZienkiewiczZhuEstimator(
				       BilinearFormIntegrator &integ,
				       GridFunction &sol,
				       FiniteElementSpace &flux_fes);
%ignore mfem::L2ZienkiewiczZhuEstimator::L2ZienkiewiczZhuEstimator(
					BilinearFormIntegrator &integ,
					ParGridFunction &sol,
					ParFiniteElementSpace *flux_fes,
					ParFiniteElementSpace *smooth_flux_fes);
%ignore mfem::L2ZienkiewiczZhuEstimator::L2ZienkiewiczZhuEstimator(
					BilinearFormIntegrator &integ,
					ParGridFunction &sol,
					ParFiniteElementSpace &flux_fes,
					ParFiniteElementSpace &smooth_flux_fes);


namespace mfem{
  %pythonprepend ZienkiewiczZhuEstimator::ZienkiewiczZhuEstimator %{
     if own_flux_fes: flux_fes.thisown=0
  %}
  %pythonprepend L2ZienkiewiczZhuEstimator::L2ZienkiewiczZhuEstimator %{
     if own_flux_fes: flux_fes.thisown=0
  %}
}

%include "fem/estimators.hpp"


namespace mfem{
  %extend ZienkiewiczZhuEstimator{
     ZienkiewiczZhuEstimator(mfem::BilinearFormIntegrator &integ,
  			     mfem::GridFunction &sol,
  			     mfem::FiniteElementSpace *flux_fes,
			     bool own_flux_fes = false){
       if (own_flux_fes){
           return new mfem::ZienkiewiczZhuEstimator(integ, sol, flux_fes);
       } else {
           return new mfem::ZienkiewiczZhuEstimator(integ, sol, *flux_fes);
       }
     }
  };
  %extend L2ZienkiewiczZhuEstimator{
     L2ZienkiewiczZhuEstimator(mfem::BilinearFormIntegrator &integ,
     			       mfem::ParGridFunction &sol,
  			       mfem::ParFiniteElementSpace *flux_fes,
                               mfem::ParFiniteElementSpace *smooth_flux_fes,     
			       bool own_flux_fes = false){
       if (own_flux_fes){
	 return new mfem::L2ZienkiewiczZhuEstimator(integ, sol,
						    flux_fes, smooth_flux_fes);
       } else {
	 return new mfem::L2ZienkiewiczZhuEstimator(integ, sol, *flux_fes,
						      *smooth_flux_fes);
       }
     }
  };
}

