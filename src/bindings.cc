#include <variant>
#include <exception>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "IPhreeqc.hpp"

namespace py = pybind11;

class _Phreeqc : public IPhreeqc
{
public:
    bool _AccumulateLine(const char *line)
    {
        auto result = AccumulateLine(line);
        if (result == VR_OUTOFMEMORY)
        {
            return false;
        }
        return true;
    }

    bool _SetCurrentSelectedOutputUserNumber(int n)
    {
        auto result = SetCurrentSelectedOutputUserNumber(n);
        if (result == VR_INVALIDARG)
        {
            return false;
        }
        return true;
    }

    const std::tuple<int, long, double, std::string> _GetSelectedOutputValue(int row, int col)
    {

        VAR var;
        VarInit(&var);
        auto result = GetSelectedOutputValue(row, col, &var);

        if (result == VR_OK)
        {
            if (var.type == TT_LONG)
            {
                return std::make_tuple(0, var.lVal, 0.0, "");
            }
            else if (var.type == TT_DOUBLE)
            {
                return std::make_tuple(1, 0, var.dVal, "");
            }
            else if (var.type == TT_STRING)
            {
                return std::make_tuple(2, 0, 0.0, var.sVal);
            }
            else if (var.type == TT_EMPTY)
            {
                throw std::runtime_error("EMPTY value");
            }
            else
            {
                throw std::runtime_error("ERROR value");
            }
        }
        else if (result == VR_OUTOFMEMORY)
        {
            throw std::bad_alloc();
        }
        else if (result == VR_BADVARTYPE)
        {
            throw std::invalid_argument("Failure, Invalid VAR type");
        }
        else if (result == VR_INVALIDARG)
        {
            throw std::invalid_argument("Failure, Invalid argument");
        }
        else if (result == VR_INVALIDROW)
        {
            throw std::invalid_argument("Invalid row");
        }
        else
        {
            throw std::invalid_argument("Invalid column");
        }
    }
};

PYBIND11_MODULE(_iphreeqc, m)
{

    m.doc() = "Python bindings for PHREEQC Version 3";
    py::class_<_Phreeqc>(m, "_Phreeqc")
        .def(py::init<>())
        .def("accumulate_line", &_Phreeqc::_AccumulateLine)
        .def("add_error", &_Phreeqc::AddError)
        .def("add_warning", &_Phreeqc::AddWarning)
        .def("clear_accumulated_lines", &_Phreeqc::ClearAccumulatedLines)
        .def("get_accumulated_lines", &_Phreeqc::GetAccumulatedLines)
        .def("get_component", &_Phreeqc::GetComponent)
        .def("get_component_count", &_Phreeqc::GetComponentCount)
        .def("get_current_selected_output_user_number", &_Phreeqc::GetCurrentSelectedOutputUserNumber)
        .def("get_dump_file_name", &_Phreeqc::GetDumpFileName)
        .def("get_dump_file_on", &_Phreeqc::GetDumpFileOn)
        .def("get_dump_string", &_Phreeqc::GetDumpString)
        .def("get_dump_string_line", &_Phreeqc::GetDumpStringLine)
        .def("get_dump_string_line_count", &_Phreeqc::GetDumpStringLineCount)
        .def("get_dump_string_on", &_Phreeqc::GetDumpStringOn)
        .def("get_error_file_name", &_Phreeqc::GetErrorFileName)
        .def("get_error_file_on", &_Phreeqc::GetErrorFileOn)
        .def("get_error_on", &_Phreeqc::GetErrorOn)
        .def("get_error_string", &_Phreeqc::GetErrorString)
        .def("get_error_string_line", &_Phreeqc::GetErrorStringLine)
        .def("get_error_string_line_count", &_Phreeqc::GetErrorStringLineCount)
        .def("get_error_string_on", &_Phreeqc::GetErrorStringOn)
        .def("get_id", &_Phreeqc::GetId)
        .def("get_log_file_name", &_Phreeqc::GetLogFileName)
        .def("get_log_file_on", &_Phreeqc::GetLogFileOn)
        .def("get_log_string", &_Phreeqc::GetLogString)
        .def("get_log_string_line", &_Phreeqc::GetLogStringLine)
        .def("get_log_string_line_count", &_Phreeqc::GetLogStringLineCount)
        .def("get_log_string_on", &_Phreeqc::GetLogStringOn)
        .def("get_nth_selected_output_user_number", &_Phreeqc::GetNthSelectedOutputUserNumber)
        .def("get_output_file_name", &_Phreeqc::GetOutputFileName)
        .def("get_output_file_on", &_Phreeqc::GetOutputFileOn)
        .def("get_output_string", &_Phreeqc::GetOutputString)
        .def("get_output_string_line", &_Phreeqc::GetOutputStringLine)
        .def("get_output_string_line_count", &_Phreeqc::GetOutputStringLineCount)
        .def("get_output_string_on", &_Phreeqc::GetOutputStringOn)
        .def("get_selected_output_column_count", &_Phreeqc::GetSelectedOutputColumnCount)
        .def("get_selected_output_count", &_Phreeqc::GetSelectedOutputCount)
        .def("get_selected_output_file_name", &_Phreeqc::GetSelectedOutputFileName)
        .def("get_selected_output_file_on", &_Phreeqc::GetSelectedOutputFileOn)
        .def("get_selected_output_row_count", &_Phreeqc::GetSelectedOutputRowCount)
        .def("get_selected_output_string", &_Phreeqc::GetSelectedOutputString)
        .def("get_selected_output_string_line", &_Phreeqc::GetSelectedOutputStringLine)
        .def("get_selected_output_string_line_count", &_Phreeqc::GetSelectedOutputStringLineCount)
        .def("get_selected_output_string_on", &_Phreeqc::GetSelectedOutputStringOn)
        .def("_get_selected_output_value", &_Phreeqc::_GetSelectedOutputValue)
        .def_static("get_version_string", &_Phreeqc::GetVersionString)
        .def("get_warning_string", &_Phreeqc::GetWarningString)
        .def("get_warning_string_line", &_Phreeqc::GetWarningStringLine)
        .def("get_warning_string_line_count", &_Phreeqc::GetWarningStringLineCount)
        .def("list_components", &_Phreeqc::ListComponents)
        .def("load_database", &_Phreeqc::LoadDatabase)
        .def("load_database_string", &_Phreeqc::LoadDatabaseString)
        .def("output_accumulated_lines", &_Phreeqc::OutputAccumulatedLines)
        .def("output_error_string", &_Phreeqc::OutputErrorString)
        .def("output_warning_string", &_Phreeqc::OutputWarningString)
        .def("run_accumulated", &_Phreeqc::RunAccumulated)
        .def("run_file", &_Phreeqc::RunFile)
        .def("run_string", &_Phreeqc::RunString)
        .def("set_current_selected_output_user_number", &_Phreeqc::_SetCurrentSelectedOutputUserNumber)
        .def("set_dump_file_name", &_Phreeqc::SetDumpFileName)
        .def("set_dump_file_on", &_Phreeqc::SetDumpFileOn)
        .def("set_dump_string_on", &_Phreeqc::SetDumpStringOn)
        .def("set_error_file_name", &_Phreeqc::SetErrorFileName)
        .def("set_error_file_on", &_Phreeqc::SetErrorFileOn)
        .def("set_error_on", &_Phreeqc::SetErrorOn)
        .def("set_error_string_on", &_Phreeqc::SetErrorStringOn)
        .def("set_log_file_name", &_Phreeqc::SetLogFileName)
        .def("set_log_file_on", &_Phreeqc::SetLogFileOn)
        .def("set_log_string_on", &_Phreeqc::SetLogStringOn)
        .def("set_output_file_name", &_Phreeqc::SetOutputFileName)
        .def("set_output_file_on", &_Phreeqc::SetOutputFileOn)
        .def("set_output_string_on", &_Phreeqc::SetOutputStringOn)
        .def("set_selected_output_file_name", &_Phreeqc::SetSelectedOutputFileName)
        .def("set_selected_output_file_on", &_Phreeqc::SetSelectedOutputFileOn)
        .def("set_selected_output_string_on", &_Phreeqc::SetSelectedOutputStringOn);

    m.attr("__version__") = "0.2.1";
}