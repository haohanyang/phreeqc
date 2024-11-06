#include <pybind11/pybind11.h>
#include "IPhreeqc.h"

namespace py = pybind11;

PYBIND11_MODULE(phreeqc, m)
{
    m.doc() = "Python bindings for PHREEQC Version 3";
    m.def("create_phreeqc", &CreateIPhreeqc, "Create a new IPhreeqc instance.");
}