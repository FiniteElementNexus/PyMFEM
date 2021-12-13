%module(package="mfem._par") fe_coll
%{
#include "fem/fem.hpp"
#include "fem/fe_coll.hpp"
#include "fem/fespace.hpp"
#include "fem/eltrans.hpp"
#include "fem/coefficient.hpp"
#include "fem/intrules.hpp"  
#include <iostream>
#include <sstream>
#include <fstream>
#include <limits>
#include <cmath>
#include <cstring>
#include <ctime>
#include "numpy/arrayobject.h"
#include "pycoefficient.hpp"  
%}

%init %{
import_array();
%}

%import "mesh.i"
%import "array.i"
%import "matrix.i"
%import "intrules.i"
%import "coefficient.i"
%import "fe.i"
%import "densemat.i"
%import "sparsemat.i"
%import "vector.i"
%import "eltrans.i"
%import "lininteg.i"

%pointer_class(int, intp);

%include "fem/fe_coll.hpp"
%pythoncode %{
  DG_FECollection = L2_FECollection
%}   
