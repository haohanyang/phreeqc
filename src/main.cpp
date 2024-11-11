#include <exception>
#include <pybind11/pybind11.h>
#include "IPhreeqc.hpp"

namespace py = pybind11;

namespace Bindings
{
    struct Phreeqc
    {
        Phreeqc()
        {
            instance = new IPhreeqc();
        }

        ~Phreeqc()
        {
            if (instance != nullptr)
            {
                delete instance;
            }
        }

        void loadDatabase(const char *path)
        {
            int errors = instance->LoadDatabase(path);
            if (errors > 0)
            {
                throw std::runtime_error("Failed to load database");
            }
        }

        void runString(const char *input)
        {
            int errors = instance->RunString(input);
            if (errors > 0)
            {
                throw std::runtime_error("Failed to run string");
            }
        }

        void runFile(const char *path)
        {
            int errors = instance->RunFile(path);
            if (errors > 0)
            {
                throw std::runtime_error("Failed to run path");
            }
        }

        const py::list getSelectedOutput()
        {
            py::list output;

            VAR var;
            VarInit(&var);

            const int colCount = instance->GetSelectedOutputColumnCount();
            const int rowCount = instance->GetSelectedOutputRowCount();

            for (int row = 0; row < rowCount; row++)
            {
                py::list rowData;
                for (int col = 0; col < colCount; col++)
                {
                    if (instance->GetSelectedOutputValue(row, col, &var) != VR_OK)
                    {
                        rowData.append(py::str("error"));
                    }
                    else
                    {
                        if (var.type == TT_LONG)
                        {
                            rowData.append(py::int_(var.lVal));
                        }
                        else if (var.type == TT_DOUBLE)
                        {
                            rowData.append(py::float_(var.dVal));
                        }
                        else if (var.type == TT_STRING)
                        {
                            rowData.append(py::str(var.sVal));
                        }
                        else
                        {
                            rowData.append(py::none());
                        }
                    }
                }

                output.append(rowData);
            }

            return output;
        }

        IPhreeqc *instance;
    };
}

PYBIND11_MODULE(IPhreeqc, m)
{
    m.doc() = "Python bindings for PHREEQC Version 3";
    py::class_<Bindings::Phreeqc>(m, "Phreeqc")
        .def(py::init<>())
        .def("load_database", &Bindings::Phreeqc::loadDatabase)
        .def("run_string", &Bindings::Phreeqc::runString)
        .def("run_file", &Bindings::Phreeqc::runFile)
        .def("get_selected_output", &Bindings::Phreeqc::getSelectedOutput);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}