#include <stdexcept>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "IPhreeqc.hpp"

namespace py = pybind11;

// RAII wrapper that calls VarClear on destruction to free any allocated string memory.
struct ScopedVAR
{
    VAR var;
    ScopedVAR() { VarInit(&var); }
    ~ScopedVAR() { VarClear(&var); }
    ScopedVAR(const ScopedVAR &) = delete;
    ScopedVAR &operator=(const ScopedVAR &) = delete;
};

static py::object var_to_py(const VAR &var)
{
    switch (var.type)
    {
    case TT_LONG:
        return py::cast(var.lVal);
    case TT_DOUBLE:
        return py::cast(var.dVal);
    case TT_STRING:
        return py::cast(std::string(var.sVal));
    case TT_EMPTY:
        throw std::runtime_error("Cell contains no data (TT_EMPTY)");
    default:
        throw std::runtime_error("Cell contains an error value (TT_ERROR)");
    }
}

PYBIND11_MODULE(_phreeqc, m)
{
    m.doc() =
        "Python bindings for IPhreeqc -- PHREEQC Version 3.\n\n"
        "Provides an interface to PHREEQC: A Computer Program for Speciation, "
        "Batch-Reaction, One-Dimensional Transport, and Inverse Geochemical Calculations.";

    py::class_<IPhreeqc>(m, "_Phreeqc")
        .def(py::init<>())

        // ── Accumulate ────────────────────────────────────────────────────────
        .def("AccumulateLine", [](IPhreeqc &self, const char *line)
             {
                 if (self.AccumulateLine(line) == VR_OUTOFMEMORY)
                     throw std::bad_alloc(); }, py::arg("line"), "Accumulate line(s) for input to phreeqc.\n\n"
                                   ":param line: The line(s) to add for input to phreeqc.\n"
                                   ":raises MemoryError: If out of memory.\n"
                                   ":see: ClearAccumulatedLines, OutputAccumulatedLines, RunAccumulated")

        .def("ClearAccumulatedLines", &IPhreeqc::ClearAccumulatedLines, "Clear the accumulated input buffer.\n\n"
                                                                        "Input buffer is accumulated from calls to AccumulateLine.\n"
                                                                        ":see: AccumulateLine, GetAccumulatedLines, OutputAccumulatedLines, RunAccumulated")

        .def("GetAccumulatedLines", &IPhreeqc::GetAccumulatedLines, "Retrieve the accumulated input string.\n\n"
                                                                    "The accumulated input string can be run with RunAccumulated.\n"
                                                                    ":returns: The accumulated input string.\n"
                                                                    ":see: AccumulateLine, ClearAccumulatedLines, OutputAccumulatedLines, RunAccumulated")

        .def("OutputAccumulatedLines", &IPhreeqc::OutputAccumulatedLines, "Output the accumulated input buffer to stdout.\n\n"
                                                                          ":see: AccumulateLine, ClearAccumulatedLines, RunAccumulated")

        .def("RunAccumulated", &IPhreeqc::RunAccumulated, "Run the input buffer as defined by calls to AccumulateLine.\n\n"
                                                          "The accumulated input is cleared at the next call to AccumulateLine.\n"
                                                          "LoadDatabase or LoadDatabaseString must have been called first with 0 errors.\n"
                                                          ":returns: The number of errors encountered.\n"
                                                          ":see: AccumulateLine, ClearAccumulatedLines, RunFile, RunString")

        // ── Errors ────────────────────────────────────────────────────────────
        .def("AddError", &IPhreeqc::AddError, py::arg("error_msg"), "Append an error message and increment the error count.\n\n"
                                                                    "Internally used to create an error condition.\n"
                                                                    ":param error_msg: The error message to display.\n"
                                                                    ":returns: The current error count.\n"
                                                                    ":see: GetErrorString, GetErrorStringLine, GetErrorStringLineCount, OutputErrorString")

        .def("GetErrorFileName", &IPhreeqc::GetErrorFileName, "Retrieve the name of the error file.\n\n"
                                                              "Default is 'phreeqc.id.err' where id is obtained from GetId.\n"
                                                              ":returns: The name of the error file.\n"
                                                              ":see: SetErrorFileName, SetErrorFileOn, SetErrorStringOn")

        .def("GetErrorFileOn", &IPhreeqc::GetErrorFileOn, "Retrieve the current value of the error file switch.\n\n"
                                                          ":returns: True if errors are written to file; False otherwise.\n"
                                                          ":see: SetErrorFileOn")

        .def("GetErrorOn", &IPhreeqc::GetErrorOn, "Retrieve the current value of the error switch.\n\n"
                                                  ":returns: True if error messages are sent to the error file and string buffer.\n"
                                                  ":see: SetErrorOn")

        .def("GetErrorString", &IPhreeqc::GetErrorString, "Retrieve error messages from the last call to a run or load method.\n\n"
                                                          ":returns: A string containing error messages.\n"
                                                          ":see: GetErrorStringLine, GetErrorStringLineCount, OutputErrorString")

        .def("GetErrorStringLine", &IPhreeqc::GetErrorStringLine, py::arg("n"), "Retrieve the given error line.\n\n"
                                                                                ":param n: The zero-based index of the line to retrieve.\n"
                                                                                ":returns: The given line of the error string buffer.\n"
                                                                                ":see: GetErrorStringLineCount, OutputErrorString")

        .def("GetErrorStringLineCount", &IPhreeqc::GetErrorStringLineCount, "Retrieve the number of lines in the current error string buffer.\n\n"
                                                                            ":returns: The number of lines.\n"
                                                                            ":see: GetErrorStringLine, OutputErrorString")

        .def("GetErrorStringOn", &IPhreeqc::GetErrorStringOn, "Retrieve the current value of the error string switch.\n\n"
                                                              ":returns: True if error output is stored; False otherwise.\n"
                                                              ":see: SetErrorStringOn")

        .def("OutputErrorString", &IPhreeqc::OutputErrorString, "Output the error messages normally stored in the error file to stdout.\n\n"
                                                                ":see: GetErrorStringLine, GetErrorStringLineCount")

        .def("SetErrorFileName", &IPhreeqc::SetErrorFileName, py::arg("filename"), "Set the name of the error file.\n\n"
                                                                                   "Default is 'phreeqc.id.err' where id is obtained from GetId.\n"
                                                                                   ":param filename: The name of the file to write error output to.\n"
                                                                                   ":see: GetErrorFileName, SetErrorFileOn, SetErrorStringOn")

        .def("SetErrorFileOn", &IPhreeqc::SetErrorFileOn, py::arg("value"), "Set the error file switch on or off. Initial setting is True.\n\n"
                                                                            ":param value: True to write errors to file; False to suppress.\n"
                                                                            ":see: GetErrorFileOn")

        .def("SetErrorOn", &IPhreeqc::SetErrorOn, py::arg("value"), "Set the error switch on or off. Initial setting is True.\n\n"
                                                                    ":param value: True to generate and display error messages; False to suppress.\n"
                                                                    ":see: GetErrorOn")

        .def("SetErrorStringOn", &IPhreeqc::SetErrorStringOn, py::arg("value"), "Set the error string switch on or off. Initial setting is True.\n\n"
                                                                                ":param value: True to capture error output to a string buffer; False otherwise.\n"
                                                                                ":see: GetErrorString, SetErrorFileOn")

        // ── Warnings ──────────────────────────────────────────────────────────
        .def("AddWarning", &IPhreeqc::AddWarning, py::arg("warning_msg"), "Append a warning message and increment the warning count.\n\n"
                                                                          ":param warning_msg: The warning message to display.\n"
                                                                          ":returns: The current warning count.\n"
                                                                          ":see: GetWarningString, GetWarningStringLine, GetWarningStringLineCount, OutputWarningString")

        .def("GetWarningString", &IPhreeqc::GetWarningString, "Retrieve warning messages from the last call to a run or load method.\n\n"
                                                              ":returns: A string containing warning messages.\n"
                                                              ":see: GetWarningStringLine, GetWarningStringLineCount, OutputWarningString")

        .def("GetWarningStringLine", &IPhreeqc::GetWarningStringLine, py::arg("n"), "Retrieve the given warning line.\n\n"
                                                                                    ":param n: The zero-based index of the line to retrieve.\n"
                                                                                    ":returns: The given warning line message.\n"
                                                                                    ":see: GetWarningStringLineCount, OutputWarningString")

        .def("GetWarningStringLineCount", &IPhreeqc::GetWarningStringLineCount, "Retrieve the number of lines in the current warning string buffer.\n\n"
                                                                                ":returns: The number of lines.\n"
                                                                                ":see: GetWarningStringLine, OutputWarningString")

        .def("OutputWarningString", &IPhreeqc::OutputWarningString, "Output the warning messages to stdout.\n\n"
                                                                    ":see: GetWarningStringLine, GetWarningStringLineCount")

        // ── Components ────────────────────────────────────────────────────────
        .def("GetComponent", &IPhreeqc::GetComponent, py::arg("n"), "Retrieve the given component by zero-based index.\n\n"
                                                                    ":param n: The zero-based index of the component to retrieve.\n"
                                                                    ":returns: The component name, or an empty string if n is out of range.\n"
                                                                    ":see: GetComponentCount, ListComponents")

        .def("GetComponentCount", &IPhreeqc::GetComponentCount, "Retrieve the number of components in the current list.\n\n"
                                                                ":returns: The current count of components.\n"
                                                                ":see: GetComponent, ListComponents")

        .def("ListComponents", &IPhreeqc::ListComponents, "Retrieve the current list of components.\n\n"
                                                          ":returns: A list of component name strings.\n"
                                                          ":see: GetComponent, GetComponentCount")

        // ── Database ──────────────────────────────────────────────────────────
        .def("LoadDatabase", &IPhreeqc::LoadDatabase, py::arg("filename"), "Load the specified database file into phreeqc.\n\n"
                                                                           "All previous definitions are cleared.\n"
                                                                           ":param filename: The name (or path) of the phreeqc database file.\n"
                                                                           ":returns: The number of errors encountered.\n"
                                                                           ":see: LoadDatabaseString")

        .def("LoadDatabaseString", &IPhreeqc::LoadDatabaseString, py::arg("input"), "Load the specified string as a database into phreeqc.\n\n"
                                                                                    "All previous definitions are cleared.\n"
                                                                                    ":param input: String containing data to use as the phreeqc database.\n"
                                                                                    ":returns: The number of errors encountered.\n"
                                                                                    ":see: LoadDatabase")

        // ── Run ───────────────────────────────────────────────────────────────
        .def("RunFile", &IPhreeqc::RunFile, py::arg("filename"), "Run the specified phreeqc input file.\n\n"
                                                                 "LoadDatabase or LoadDatabaseString must have been called first with 0 errors.\n"
                                                                 ":param filename: The name of the phreeqc input file to run.\n"
                                                                 ":returns: The number of errors encountered.\n"
                                                                 ":see: RunAccumulated, RunString")

        .def("RunString", &IPhreeqc::RunString, py::arg("input"), "Run the specified string as input to phreeqc.\n\n"
                                                                  "LoadDatabase or LoadDatabaseString must have been called first with 0 errors.\n"
                                                                  ":param input: String containing phreeqc input.\n"
                                                                  ":returns: The number of errors encountered.\n"
                                                                  ":see: RunAccumulated, RunFile")

        // ── Selected Output ───────────────────────────────────────────────────
        .def("GetCurrentSelectedOutputUserNumber", &IPhreeqc::GetCurrentSelectedOutputUserNumber, "Retrieve the current SELECTED_OUTPUT user number. Initial setting is 1.\n\n"
                                                                                                  ":returns: The current SELECTED_OUTPUT user number.\n"
                                                                                                  ":see: SetCurrentSelectedOutputUserNumber")

        .def("GetNthSelectedOutputUserNumber", &IPhreeqc::GetNthSelectedOutputUserNumber, py::arg("n"), "Retrieve the nth user number of the currently defined SELECTED_OUTPUT blocks.\n\n"
                                                                                                        ":param n: The zero-based index of the SELECTED_OUTPUT user number to retrieve.\n"
                                                                                                        ":returns: The nth defined user number; a negative value indicates an error.\n"
                                                                                                        ":see: GetCurrentSelectedOutputUserNumber, GetSelectedOutputCount")

        .def("GetSelectedOutputColumnCount", &IPhreeqc::GetSelectedOutputColumnCount, "Retrieve the number of columns in the current selected-output buffer.\n\n"
                                                                                      ":returns: The number of columns.\n"
                                                                                      ":see: GetSelectedOutputRowCount, GetSelectedOutputValue")

        .def("GetSelectedOutputCount", &IPhreeqc::GetSelectedOutputCount, "Retrieve the count of SELECTED_OUTPUT blocks currently defined.\n\n"
                                                                          ":returns: The number of SELECTED_OUTPUT blocks.\n"
                                                                          ":see: GetNthSelectedOutputUserNumber, SetCurrentSelectedOutputUserNumber")

        .def("GetSelectedOutputFileName", &IPhreeqc::GetSelectedOutputFileName, "Retrieve the name of the current selected output file.\n\n"
                                                                                "Default is 'selected_n.id.out' where id is obtained from GetId.\n"
                                                                                ":returns: The name of the file to write SELECTED_OUTPUT to.\n"
                                                                                ":see: SetSelectedOutputFileName, SetSelectedOutputFileOn, SetSelectedOutputStringOn")

        .def("GetSelectedOutputFileOn", &IPhreeqc::GetSelectedOutputFileOn, "Retrieve the current selected-output file switch.\n\n"
                                                                            ":returns: True if output is written to the selected-output file; False otherwise.\n"
                                                                            ":see: SetSelectedOutputFileOn")

        .def("GetSelectedOutputRowCount", &IPhreeqc::GetSelectedOutputRowCount, "Retrieve the number of rows in the current selected-output buffer.\n\n"
                                                                                "Row 0 contains column headings; data rows start at index 1.\n"
                                                                                ":returns: The number of rows (including the header row).\n"
                                                                                ":see: GetSelectedOutputColumnCount, GetSelectedOutputValue")

        .def("GetSelectedOutputString", &IPhreeqc::GetSelectedOutputString, "Retrieve the string buffer containing SELECTED_OUTPUT.\n\n"
                                                                            "SetSelectedOutputStringOn must have been set to True.\n"
                                                                            ":returns: A string containing SELECTED_OUTPUT.\n"
                                                                            ":see: GetSelectedOutputStringLine, GetSelectedOutputStringLineCount")

        .def("GetSelectedOutputStringLine", &IPhreeqc::GetSelectedOutputStringLine, py::arg("n"), "Retrieve the given selected output line.\n\n"
                                                                                                  "SetSelectedOutputStringOn must have been set to True.\n"
                                                                                                  ":param n: The zero-based index of the line to retrieve.\n"
                                                                                                  ":returns: The given line, or an empty string if n is out of range.\n"
                                                                                                  ":see: GetSelectedOutputStringLineCount, SetSelectedOutputStringOn")

        .def("GetSelectedOutputStringLineCount", &IPhreeqc::GetSelectedOutputStringLineCount, "Retrieve the number of lines in the current selected output string buffer.\n\n"
                                                                                              "SetSelectedOutputStringOn must have been set to True.\n"
                                                                                              ":returns: The number of lines.\n"
                                                                                              ":see: GetSelectedOutputStringLine, SetSelectedOutputStringOn")

        .def("GetSelectedOutputStringOn", &IPhreeqc::GetSelectedOutputStringOn, "Retrieve the value of the current selected output string switch.\n\n"
                                                                                ":returns: True if SELECTED_OUTPUT is stored; False otherwise.\n"
                                                                                ":see: SetSelectedOutputStringOn")

        .def("GetSelectedOutputValue", [](IPhreeqc &self, int row, int col) -> py::object
             {
                 ScopedVAR sv;
                 VRESULT result = self.GetSelectedOutputValue(row, col, &sv.var);
                 switch (result) {
                     case VR_OK:          return var_to_py(sv.var);
                     case VR_OUTOFMEMORY: throw std::bad_alloc();
                     case VR_BADVARTYPE:  throw std::invalid_argument("Invalid VAR type");
                     case VR_INVALIDARG:  throw std::invalid_argument("Invalid argument");
                     case VR_INVALIDROW:  throw std::out_of_range("Row index out of range: " + std::to_string(row));
                     default:             throw std::out_of_range("Column index out of range: " + std::to_string(col));
                 } }, py::arg("row"), py::arg("col"), "Return the value at the specified row and column of the selected output.\n\n"
                                                  "Row 0 contains column headings; data starts at row 1. The return type\n"
                                                  "is int, float, or str depending on the cell content.\n"
                                                  ":param row: The row index.\n"
                                                  ":param col: The column index.\n"
                                                  ":returns: An int, float, or str depending on the cell type.\n"
                                                  ":raises IndexError: If row or column is out of range.\n"
                                                  ":raises ValueError: If the argument or VAR type is invalid.\n"
                                                  ":raises MemoryError: If memory allocation fails.\n"
                                                  ":see: GetSelectedOutputColumnCount, GetSelectedOutputRowCount")

        .def("SetCurrentSelectedOutputUserNumber", [](IPhreeqc &self, int n)
             {
                 if (self.SetCurrentSelectedOutputUserNumber(n) == VR_INVALIDARG)
                     throw std::invalid_argument(
                         "SELECTED_OUTPUT user number has not been defined: " + std::to_string(n)); }, py::arg("n"), "Set the current SELECTED_OUTPUT user number. Initial setting is 1.\n\n"
                                "Subsequent calls to GetSelectedOutput* routines use this user number.\n"
                                ":param n: The user number as specified in the SELECTED_OUTPUT block.\n"
                                ":raises ValueError: If the given user number has not been defined.\n"
                                ":see: GetCurrentSelectedOutputUserNumber")

        .def("SetSelectedOutputFileName", &IPhreeqc::SetSelectedOutputFileName, py::arg("filename"), "Set the name of the current selected output file.\n\n"
                                                                                                     "Default is 'selected_n.id.out' where id is obtained from GetId.\n"
                                                                                                     ":param filename: The name of the file to write SELECTED_OUTPUT to.\n"
                                                                                                     ":see: GetSelectedOutputFileName, SetSelectedOutputFileOn, SetSelectedOutputStringOn")

        .def("SetSelectedOutputFileOn", &IPhreeqc::SetSelectedOutputFileOn, py::arg("value"), "Set the selected-output file switch on or off. Initial setting is False.\n\n"
                                                                                              ":param value: True to write SELECTED_OUTPUT to file; False to suppress.\n"
                                                                                              ":see: GetSelectedOutputFileOn")

        .def("SetSelectedOutputStringOn", &IPhreeqc::SetSelectedOutputStringOn, py::arg("value"), "Set the selected output string switch on or off. Initial setting is False.\n\n"
                                                                                                  ":param value: True to capture SELECTED_OUTPUT to a string buffer; False otherwise.\n"
                                                                                                  ":see: GetSelectedOutputString, SetSelectedOutputFileOn")

        // ── Dump ──────────────────────────────────────────────────────────────
        .def("GetDumpFileName", &IPhreeqc::GetDumpFileName, "Retrieve the name of the dump file.\n\n"
                                                            "Default is 'dump.id.out' where id is obtained from GetId.\n"
                                                            ":returns: The name of the file to write DUMP output to.\n"
                                                            ":see: SetDumpFileName, SetDumpFileOn, SetDumpStringOn")

        .def("GetDumpFileOn", &IPhreeqc::GetDumpFileOn, "Retrieve the current value of the dump file switch.\n\n"
                                                        ":returns: True if output is written to the DUMP file; False otherwise.\n"
                                                        ":see: SetDumpFileOn, SetDumpStringOn")

        .def("GetDumpString", &IPhreeqc::GetDumpString, "Retrieve the string buffer containing DUMP output.\n\n"
                                                        "SetDumpStringOn must have been set to True to receive DUMP output.\n"
                                                        ":returns: A string containing DUMP output.\n"
                                                        ":see: GetDumpStringLine, GetDumpStringLineCount, SetDumpStringOn")

        .def("GetDumpStringLine", &IPhreeqc::GetDumpStringLine, py::arg("n"), "Retrieve the given dump line.\n\n"
                                                                              "SetDumpStringOn must have been set to True.\n"
                                                                              ":param n: The zero-based index of the line to retrieve.\n"
                                                                              ":returns: The given line, or an empty string if n is out of range.\n"
                                                                              ":see: GetDumpStringLineCount, SetDumpStringOn")

        .def("GetDumpStringLineCount", &IPhreeqc::GetDumpStringLineCount, "Retrieve the number of lines in the current dump string buffer.\n\n"
                                                                          "SetDumpStringOn must have been set to True.\n"
                                                                          ":returns: The number of lines.\n"
                                                                          ":see: GetDumpStringLine, SetDumpStringOn")

        .def("GetDumpStringOn", &IPhreeqc::GetDumpStringOn, "Retrieve the current value of the dump string switch.\n\n"
                                                            ":returns: True if DUMP output is stored; False otherwise.\n"
                                                            ":see: SetDumpStringOn, SetDumpFileOn")

        .def("SetDumpFileName", &IPhreeqc::SetDumpFileName, py::arg("filename"), "Set the name of the dump file.\n\n"
                                                                                 "Default is 'dump.id.out' where id is obtained from GetId.\n"
                                                                                 ":param filename: The name of the file to write DUMP output to.\n"
                                                                                 ":see: GetDumpFileName, SetDumpFileOn, SetDumpStringOn")

        .def("SetDumpFileOn", &IPhreeqc::SetDumpFileOn, py::arg("value"), "Set the dump file switch on or off. Initial setting is False.\n\n"
                                                                          ":param value: True to write DUMP output to file; False to suppress.\n"
                                                                          ":see: GetDumpFileOn, SetDumpStringOn")

        .def("SetDumpStringOn", &IPhreeqc::SetDumpStringOn, py::arg("value"), "Set the dump string switch on or off. Initial setting is False.\n\n"
                                                                              ":param value: True to capture DUMP output to a string buffer; False otherwise.\n"
                                                                              ":see: GetDumpString, SetDumpFileOn")

        // ── Log ───────────────────────────────────────────────────────────────
        .def("GetLogFileName", &IPhreeqc::GetLogFileName, "Retrieve the name of the log file.\n\n"
                                                          "Default is 'phreeqc.id.log' where id is obtained from GetId.\n"
                                                          ":returns: The name of the log file.\n"
                                                          ":see: SetLogFileName, SetLogFileOn, SetLogStringOn")

        .def("GetLogFileOn", &IPhreeqc::GetLogFileOn, "Retrieve the current value of the log file switch.\n\n"
                                                      "Logging must be enabled through the KNOBS -logfile option.\n"
                                                      ":returns: True if log messages are written to file; False otherwise.\n"
                                                      ":see: SetLogFileOn")

        .def("GetLogString", &IPhreeqc::GetLogString, "Retrieve the string buffer containing phreeqc log output.\n\n"
                                                      "SetLogStringOn must be True and KNOBS -logfile must be enabled.\n"
                                                      ":returns: A string containing log output.\n"
                                                      ":see: GetLogStringLine, GetLogStringLineCount, SetLogStringOn")

        .def("GetLogStringLine", &IPhreeqc::GetLogStringLine, py::arg("n"), "Retrieve the given log line.\n\n"
                                                                            "SetLogStringOn must be True and KNOBS -logfile must be enabled.\n"
                                                                            ":param n: The zero-based index of the line to retrieve.\n"
                                                                            ":returns: The given line, or an empty string if n is out of range.\n"
                                                                            ":see: GetLogStringLineCount, SetLogStringOn")

        .def("GetLogStringLineCount", &IPhreeqc::GetLogStringLineCount, "Retrieve the number of lines in the current log string buffer.\n\n"
                                                                        "SetLogStringOn must be True and KNOBS -logfile must be enabled.\n"
                                                                        ":returns: The number of lines.\n"
                                                                        ":see: GetLogStringLine, SetLogStringOn")

        .def("GetLogStringOn", &IPhreeqc::GetLogStringOn, "Retrieve the current value of the log string switch.\n\n"
                                                          ":returns: True if log output is stored; False otherwise.\n"
                                                          ":see: SetLogStringOn")

        .def("SetLogFileName", &IPhreeqc::SetLogFileName, py::arg("filename"), "Set the name of the log file.\n\n"
                                                                               "Default is 'phreeqc.id.log' where id is obtained from GetId.\n"
                                                                               ":param filename: The name of the file to write log output to.\n"
                                                                               ":see: GetLogFileName, SetLogFileOn, SetLogStringOn")

        .def("SetLogFileOn", &IPhreeqc::SetLogFileOn, py::arg("value"), "Set the log file switch on or off. Initial setting is False.\n\n"
                                                                        "Logging must be enabled through the KNOBS -logfile option.\n"
                                                                        ":param value: True to write log messages to file; False to suppress.\n"
                                                                        ":see: GetLogFileOn")

        .def("SetLogStringOn", &IPhreeqc::SetLogStringOn, py::arg("value"), "Set the log string switch on or off. Initial setting is False.\n\n"
                                                                            ":param value: True to capture log output to a string buffer; False otherwise.\n"
                                                                            ":see: GetLogString, SetLogFileOn")

        // ── Output ────────────────────────────────────────────────────────────
        .def("GetOutputFileName", &IPhreeqc::GetOutputFileName, "Retrieve the name of the output file.\n\n"
                                                                "Default is 'phreeqc.id.out' where id is obtained from GetId.\n"
                                                                ":returns: The name of the output file.\n"
                                                                ":see: SetOutputFileName, SetOutputFileOn, SetOutputStringOn")

        .def("GetOutputFileOn", &IPhreeqc::GetOutputFileOn, "Retrieve the current value of the output file switch.\n\n"
                                                            ":returns: True if output is written to file; False otherwise.\n"
                                                            ":see: SetOutputFileOn")

        .def("GetOutputString", &IPhreeqc::GetOutputString, "Retrieve the string buffer containing phreeqc output.\n\n"
                                                            "SetOutputStringOn must have been set to True to receive output.\n"
                                                            ":returns: A string containing phreeqc output.\n"
                                                            ":see: GetOutputStringLine, GetOutputStringLineCount, SetOutputStringOn")

        .def("GetOutputStringLine", &IPhreeqc::GetOutputStringLine, py::arg("n"), "Retrieve the given output line.\n\n"
                                                                                  "SetOutputStringOn must have been set to True.\n"
                                                                                  ":param n: The zero-based index of the line to retrieve.\n"
                                                                                  ":returns: The given line, or an empty string if n is out of range.\n"
                                                                                  ":see: GetOutputStringLineCount, SetOutputStringOn")

        .def("GetOutputStringLineCount", &IPhreeqc::GetOutputStringLineCount, "Retrieve the number of lines in the current output string buffer.\n\n"
                                                                              "SetOutputStringOn must have been set to True.\n"
                                                                              ":returns: The number of lines.\n"
                                                                              ":see: GetOutputStringLine, SetOutputStringOn")

        .def("GetOutputStringOn", &IPhreeqc::GetOutputStringOn, "Retrieve the current value of the output string switch.\n\n"
                                                                ":returns: True if phreeqc output is stored; False otherwise.\n"
                                                                ":see: SetOutputStringOn")

        .def("SetOutputFileName", &IPhreeqc::SetOutputFileName, py::arg("filename"), "Set the name of the output file.\n\n"
                                                                                     "Default is 'phreeqc.id.out' where id is obtained from GetId.\n"
                                                                                     ":param filename: The name of the file to write phreeqc output to.\n"
                                                                                     ":see: GetOutputFileName, SetOutputFileOn, SetOutputStringOn")

        .def("SetOutputFileOn", &IPhreeqc::SetOutputFileOn, py::arg("value"), "Set the output file switch on or off. Initial setting is False.\n\n"
                                                                              ":param value: True to write phreeqc output to file; False to suppress.\n"
                                                                              ":see: GetOutputFileOn")

        .def("SetOutputStringOn", &IPhreeqc::SetOutputStringOn, py::arg("value"), "Set the output string switch on or off. Initial setting is False.\n\n"
                                                                                  ":param value: True to capture output to a string buffer; False otherwise.\n"
                                                                                  ":see: GetOutputString, SetOutputFileOn")

        // ── Instance / Version ────────────────────────────────────────────────
        .def("GetId", &IPhreeqc::GetId, "Retrieve the id of this instance.\n\n"
                                        "Each instance receives a unique id incremented from zero.\n"
                                        ":returns: The id.")

        .def_static("GetVersionString", &IPhreeqc::GetVersionString, "Retrieve the IPhreeqc version string in the form X.X.X-XXXX.\n\n"
                                                                     ":returns: The version string.");

    m.attr("__version__") = "0.2.1";
}
