#include <exception>
#include <pybind11/pybind11.h>
#include "IPhreeqc.h"

namespace py = pybind11;

struct Phreeqc
{
    Phreeqc()
    {
        int res = CreateIPhreeqc();
        if (res < 0)
        {
            throw std::runtime_error("Failed to create an IPhreeqc instance");
        }

        id = res;
    }

    void loadDatabase(const char *path)
    {
        int errors = LoadDatabase(id, path);
        if (errors > 0)
        {
            throw std::runtime_error("Failed to load database");
        }
    }

    void runString(const char *input)
    {
        int errors = RunString(id, input);
        if (errors > 0)
        {
            throw std::runtime_error("Failed to run string");
        }
    }

    void runFile(const char *path)
    {
        int errors = RunFile(id, path);
        if (errors > 0)
        {
            throw std::runtime_error("Failed to run path");
        }
    }

    const char *getSelectedOutputString()
    {
        return GetSelectedOutputString(id);
    }

    int id;
};

PYBIND11_MODULE(phreeqc, m)
{
    m.doc() = "Python bindings for PHREEQC Version 3";
    py::class_<Phreeqc>(m, "Phreeqc")
        .def(py::init<>())
        .def("load_database", &Phreeqc::loadDatabase)
        .def("run_string", &Phreeqc::runString)
        .def("run_file", &Phreeqc::runFile)
        .def("get_selected_output_string", &Phreeqc::getSelectedOutputString);
}