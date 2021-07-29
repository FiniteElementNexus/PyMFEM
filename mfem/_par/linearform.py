# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _linearform
else:
    import _linearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _linearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _linearform.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.coefficient
import mfem._par.globals
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.matrix
import mfem._par.vector
import mfem._par.operators
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.nonlininteg
class LinearForm(mfem._par.vector.Vector):
    r"""Proxy of C++ mfem::LinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(LinearForm self, FiniteElementSpace f) -> LinearForm
        __init__(LinearForm self, FiniteElementSpace f, LinearForm lf) -> LinearForm
        __init__(LinearForm self) -> LinearForm
        __init__(LinearForm self, FiniteElementSpace f, double * data) -> LinearForm
        """
        _linearform.LinearForm_swiginit(self, _linearform.new_LinearForm(*args))

    def GetFES(self):
        r"""GetFES(LinearForm self) -> FiniteElementSpace"""
        return _linearform.LinearForm_GetFES(self)
    GetFES = _swig_new_instance_method(_linearform.LinearForm_GetFES)

    def FESpace(self, *args):
        r"""
        FESpace(LinearForm self) -> FiniteElementSpace
        FESpace(LinearForm self) -> FiniteElementSpace
        """
        return _linearform.LinearForm_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_linearform.LinearForm_FESpace)

    def AddDomainIntegrator(self, *args):
        r"""
        AddDomainIntegrator(LinearForm self, LinearFormIntegrator lfi)
        AddDomainIntegrator(LinearForm self, LinearFormIntegrator lfi, intArray elem_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        lfi = args[0]	     
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddDomainIntegrator(self, *args)


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(LinearForm self, LinearFormIntegrator lfi)
        AddBoundaryIntegrator(LinearForm self, LinearFormIntegrator lfi, intArray bdr_attr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        lfi = args[0]	     	     
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddBoundaryIntegrator(self, *args)


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(LinearForm self, LinearFormIntegrator lfi)
        AddBdrFaceIntegrator(LinearForm self, LinearFormIntegrator lfi, intArray bdr_attr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        lfi = args[0]	     
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddBdrFaceIntegrator(self, *args)


    def AddInteriorFaceIntegrator(self, lfi):
        r"""AddInteriorFaceIntegrator(LinearForm self, LinearFormIntegrator lfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(lfi)
        lfi.thisown=0 


        return _linearform.LinearForm_AddInteriorFaceIntegrator(self, lfi)


    def GetDLFI(self):
        r"""GetDLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetDLFI(self)
    GetDLFI = _swig_new_instance_method(_linearform.LinearForm_GetDLFI)

    def GetDLFI_Delta(self):
        r"""GetDLFI_Delta(LinearForm self) -> mfem::Array< mfem::DeltaLFIntegrator * > *"""
        return _linearform.LinearForm_GetDLFI_Delta(self)
    GetDLFI_Delta = _swig_new_instance_method(_linearform.LinearForm_GetDLFI_Delta)

    def GetBLFI(self):
        r"""GetBLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetBLFI(self)
    GetBLFI = _swig_new_instance_method(_linearform.LinearForm_GetBLFI)

    def GetFLFI(self):
        r"""GetFLFI(LinearForm self) -> mfem::Array< mfem::LinearFormIntegrator * > *"""
        return _linearform.LinearForm_GetFLFI(self)
    GetFLFI = _swig_new_instance_method(_linearform.LinearForm_GetFLFI)

    def GetFLFI_Marker(self):
        r"""GetFLFI_Marker(LinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _linearform.LinearForm_GetFLFI_Marker(self)
    GetFLFI_Marker = _swig_new_instance_method(_linearform.LinearForm_GetFLFI_Marker)

    def Assemble(self):
        r"""Assemble(LinearForm self)"""
        return _linearform.LinearForm_Assemble(self)
    Assemble = _swig_new_instance_method(_linearform.LinearForm_Assemble)

    def AssembleDelta(self):
        r"""AssembleDelta(LinearForm self)"""
        return _linearform.LinearForm_AssembleDelta(self)
    AssembleDelta = _swig_new_instance_method(_linearform.LinearForm_AssembleDelta)

    def Update(self, *args):
        r"""
        Update(LinearForm self)
        Update(LinearForm self, FiniteElementSpace f)
        Update(LinearForm self, FiniteElementSpace f, Vector v, int v_offset)
        """
        return _linearform.LinearForm_Update(self, *args)
    Update = _swig_new_instance_method(_linearform.LinearForm_Update)

    def MakeRef(self, f, v, v_offset):
        r"""MakeRef(LinearForm self, FiniteElementSpace f, Vector v, int v_offset)"""
        return _linearform.LinearForm_MakeRef(self, f, v, v_offset)
    MakeRef = _swig_new_instance_method(_linearform.LinearForm_MakeRef)

    def __call__(self, gf):
        r"""__call__(LinearForm self, GridFunction gf) -> double"""
        return _linearform.LinearForm___call__(self, gf)
    __call__ = _swig_new_instance_method(_linearform.LinearForm___call__)
    __swig_destroy__ = _linearform.delete_LinearForm

# Register LinearForm in _linearform:
_linearform.LinearForm_swigregister(LinearForm)



