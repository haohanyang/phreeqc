from typing import List, Dict

class Phreeqc:
    def __init__(self) -> None:
        """
        Constructor.
        """
        ...

    def accumulate_line(self, line: str) -> bool:
        """
        Accumlulate line(s) for input to phreeqc.
        @param line             The line(s) to add for input to phreeqc.
        @retval True            Success
        @retval False           Out of memory
        @see                    ClearAccumulatedLines, OutputAccumulatedLines, RunAccumulated

        """
        ...

    def add_error(self, error_msg: str) -> int:
        """
        Appends the given error message and increments the error count.
        Internally used to create an error condition.
        @param error_msg        The error message to display.
        @return                 The current error count.
        @see                    GetErrorString, GetErrorStringLine, GetErrorStringLineCount, OutputErrorString

        """
        ...

    def add_warning(self, warning_msg: str) -> int:
        """
        Appends the given warning message and increments the warning count.
        Internally used to create a warning condition.
        @param warning_msg      The warning message to display.
        @return                 The current warning count.
        @see                    GetWarningString, GetWarningStringLine, GetWarningStringLineCount, OutputWarningString

        """
        ...

    def clear_accumulated_lines(self) -> None:
        """
        Clears the accumulated input buffer.  Input buffer is accumulated from calls to @ref AccumulateLine.
        @see                    AccumulateLine, GetAccumulatedLines, OutputAccumulatedLines, RunAccumulated

        """
        ...

    def get_accumulated_lines(self) -> str:
        """
        Retrieve the accumulated input string.  The accumulated input string can be run
        with @ref RunAccumulated.
        @return                 The accumulated input string.
        @see                    AccumulateLine, ClearAccumulatedLines, OutputAccumulatedLines, RunAccumulated

        """
        ...

    def get_component(self, n: int) -> str:
        """
        Retrieves the given component.
        @param n                The zero-based index of the component to retrieve.
        @return                 A null terminated string containing the given component.
                                Returns an empty string if n is out of range.
        @see                    GetComponentCount, ListComponents

        """
        ...

    def get_component_count(self) -> int:
        """
        Retrieves the number of components in the current list of components.
        @return                 The current count of components.
        @see                    GetComponent, ListComponents

        """
        ...

    def get_current_selected_output_user_number(self) -> int:
        """
        Retrieves the current <B>SELECTED_OUTPUT</B> user number.  The initial setting is 1.
        @return                 The current <b>SELECTED_OUTPUT</b> user number.
        @see                    GetSelectedOutputColumnCount, GetSelectedOutputFileName, GetSelectedOutputRowCount, GetSelectedOutputString, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, GetSelectedOutputValue, SetCurrentSelectedOutputUserNumber

        """
        ...

    def get_dump_file_name(self) -> str:
        """
        Retrieves the name of the dump file.  This file name is used if not specified within <B>DUMP</B> input.
        The default value is <B><I>dump.id.out</I></B>, where id is obtained from @ref GetId.
        @return filename        The name of the file to write <B>DUMP</B> output to.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringOn, GetDumpStringLine, GetDumpStringLineCount, SetDumpFileName, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_dump_file_on(self) -> bool:
        """
        Retrieves the current value of the dump file switch.
        @retval True            Output is written to the <B>DUMP</B> (<B><I>dump.id.out</I></B> if unspecified, where id is obtained from @ref GetId) file.
        @retval False           No output is written.
        @see                    GetDumpStringLine, GetDumpStringLineCount, GetDumpStringOn, GetDumpString, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_dump_string(self) -> str:
        """
        Retrieves the string buffer containing <b>DUMP</b> output.
        @return                 A null terminated string containing <b>DUMP</b> output.
        @pre
            @ref SetDumpStringOn must have been set to True in order to receive <b>DUMP</b> output.
        @see                    GetDumpStringLine, GetDumpFileOn, GetDumpStringLineCount, GetDumpStringOn, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_dump_string_line(self, n: int) -> str:
        """
        Retrieves the given dump line.
        @param n                The zero-based index of the line to retrieve.
        @return                 A null terminated string containing the given line.
                                Returns an empty string if n is out of range.
        @pre                    @ref SetDumpStringOn must have been set to True.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringLineCount, GetDumpStringOn, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_dump_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current dump string buffer.
        @return                 The number of lines.
        @pre                    @ref SetDumpStringOn must have been set to True.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringLine, GetDumpStringOn, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_dump_string_on(self) -> bool:
        """
        Retrieves the current value of the dump string switch.
        @retval True            Output defined by the <B>DUMP</B> keyword is stored.
        @retval False           No output is stored.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringLine, GetDumpStringLineCount, SetDumpFileOn, SetDumpStringOn

        """
        ...

    def get_error_file_name(self) -> str:
        """
        Retrieves the name of the error file. The default value is <B><I>phreeqc.id.err</I></B>, where id is obtained from @ref GetId.
        @return filename        The name of the file to write to.
        @see                    GetErrorFileOn, GetErrorString, GetErrorStringOn, GetErrorStringLine, GetErrorStringLineCount, SetErrorFileName, SetErrorFileOn, SetErrorStringOn

        """
        ...

    def get_error_file_on(self) -> bool:
        """
        Retrieves the current value of the error file switch.
        @retval True            Errors are written to the <B><I>phreeqc.id.err</I></B> (where id is obtained from @ref GetId) file.
        @retval False           No errors are written.
        @see                    SetErrorFileOn

        """
        ...

    def get_error_on(self) -> bool:
        """
        Retrieves the current value of the error switch.
        @retval True            Error messages are sent to the error file and to the string buffer
        @retval False           No errors are sent.
        @see                    SetErrorOn

        """
        ...

    def get_error_string(self) -> str:
        """
        Retrieves the error messages from the last call to @ref RunAccumulated, @ref RunFile, @ref RunString, @ref LoadDatabase, or @ref LoadDatabaseString.
        @return                 A null terminated string containing error messages.
        @see                    GetErrorStringLine, GetErrorStringLineCount, GetErrorFileOn, OutputErrorString, SetErrorFileOn

        """
        ...

    def get_error_string_line(self, n: int) -> str:
        """
        Retrieves the given error line.
        @return                 A null terminated string containing the given line of the error string buffer.
        @param n                The zero-based index of the line to retrieve.
        @see                    GetErrorStringLineCount, OutputErrorString

        """
        ...

    def get_error_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current error string buffer.
        @return                 The number of lines.
        @see                    GetErrorStringLine, OutputErrorString

        """
        ...

    def get_error_string_on(self) -> bool:
        """
        Retrieves the current value of the error string switch.
        @retval True            Error output is stored.
        @retval False           No error output is stored.
        @see                    GetErrorFileOn, GetErrorString, GetErrorStringLine, GetErrorStringLineCount, SetErrorFileOn, SetErrorStringOn

        """
        ...

    def get_id(self) -> int:
        """
        Retrieves the id of this object.  Each instance receives an id which is incremented for each instance
        starting with the value zero.
        @return                 The id.

        """
        ...

    def get_log_file_name(self) -> str:
        """
        Retrieves the name of the log file. The default value is <B><I>phreeqc.id.log</I></B>, where id is obtained from @ref GetId.
        @return filename        The name of the file to write to.
        @see                    GetLogFileOn, GetLogString, GetLogStringOn, GetLogStringLine, GetLogStringLineCount, SetLogFileName, SetLogFileOn, SetLogStringOn

        """
        ...

    def get_log_file_on(self) -> bool:
        """
        Retrieves the current value of the log file switch.
        @retval True            Log messages are written to the <B><I>phreeqc.id.log</I></B> (where id is obtained from @ref GetId) file.
        @retval False           No log messages are written.
        @remarks
            Logging must be enabled through the use of the KNOBS -logfile option in order to receive any log messages.
        @see                    SetLogFileOn

        """
        ...

    def get_log_string(self) -> str:
        """
        Retrieves the string buffer containing phreeqc log output.
        @return                 A null terminated string containing log output.
        @pre
            @ref SetLogStringOn must have been set to True and enabled through the use of the KNOBS -logfile option in order to receive any log messages.
        @see                    GetLogStringLine, GetLogFileOn, GetLogStringLineCount, GetLogStringOn, SetLogFileOn, SetLogStringOn

        """
        ...

    def get_log_string_line(self, n: int) -> str:
        """
        Retrieves the given log line.
        @param n                The zero-based index of the line to retrieve.
        @return                 A null terminated string containing the given line.
                                Returns an empty string if n is out of range.
        @pre                    @ref SetLogStringOn must have been set to True and enabled through the use of the KNOBS -logfile option in order to receive any log messages.
        @see                    GetLogFileOn, GetLogString, GetLogStringLineCount, GetLogStringOn, SetLogFileOn, SetLogStringOn

        """
        ...

    def get_log_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current log string buffer.
        @return                 The number of lines.
        @pre                    @ref SetLogStringOn must have been set to True and enabled through the use of the KNOBS -logfile option in order to receive any log messages.
        @see                    GetLogFileOn, GetLogString, GetLogStringLine, GetLogStringOn, SetLogFileOn, SetLogStringOn

        """
        ...

    def get_selected_output(self) -> Dict[str, List[int | float | str]]:
        """
        Returns the selected output value in dict
        """
        ...

    def get_log_string_on(self) -> bool:
        """
        Retrieves the current value of the log string switch.
        @retval True            Log output is stored.
        @retval False           No log output is stored.
        @see                    GetLogFileOn, GetLogString, GetLogStringLine, GetLogStringLineCount, SetLogFileOn, SetLogStringOn

        """
        ...

    def get_nth_selected_output_user_number(self, n: int) -> int:
        """
        Retrieves the nth user number of the currently defined <B>SELECTED_OUTPUT</B> blocks.
        @param n                The zero-based index of the <B>SELECTED_OUTPUT</B> user number to retrieve.
        @return                 The nth defined user number; a negative value indicates an error occured.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputCount, SetCurrentSelectedOutputUserNumber

        """
        ...

    def get_output_file_name(self) -> str:
        """
        Retrieves the name of the output file. The default value is <B><I>phreeqc.id.out</I></B>, where id is obtained from @ref GetId.
        @return filename        The name of the file to write phreeqc output to.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringOn, GetOutputStringLine, GetOutputStringLineCount, SetOutputFileName, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_output_file_on(self) -> bool:
        """
        Retrieves the current value of the output file switch.
        @retval True            Output is written to the <B><I>phreeqc.id.out</I></B> (where id is obtained from @ref GetId) file.
        @retval False           No output is written.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringOn, GetOutputStringLine, GetOutputStringLineCount, SetOutputFileName, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_output_string(self) -> str:
        """
        Retrieves the string buffer containing phreeqc output.
        @return                 A null terminated string containing phreeqc output.
        @pre
            @ref SetOutputStringOn must have been set to True in order to receive output.
        @see                    GetOutputStringLine, GetOutputFileOn, GetOutputStringLineCount, GetOutputStringOn, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_output_string_line(self, n: int) -> str:
        """
        Retrieves the given output line.
        @param n                The zero-based index of the line to retrieve.
        @return                 A null terminated string containing the given line.
                                Returns an empty string if n is out of range.
        @pre                    @ref SetOutputStringOn must have been set to True.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringLineCount, GetOutputStringOn, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_output_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current output string buffer.
        @return                 The number of lines.
        @pre                    @ref SetOutputStringOn must have been set to True.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringLine, GetOutputStringOn, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_output_string_on(self) -> bool:
        """
        Retrieves the current value of the output string switch.
        @retval True            Phreeqc output is stored.
        @retval False           No phreeqc output is stored.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringLine, GetOutputStringLineCount, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def get_selected_output_column_count(self) -> int:
        """
        Retrieves the number of columns in the current selected-output buffer (see @ref SetCurrentSelectedOutputUserNumber).
        @return                 The number of columns.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputRowCount, GetSelectedOutputValue, SetCurrentSelectedOutputUserNumber

        """
        ...

    def get_selected_output_count(self) -> int:
        """
        Retrieves the count of <B>SELECTED_OUTPUT</B> blocks that are currently defined.
        @return                 The number of <B>SELECTED_OUTPUT</B> blocks.
        @see                    GetCurrentSelectedOutputUserNumber, GetNthSelectedOutputUserNumber, SetCurrentSelectedOutputUserNumber

        """
        ...

    def get_selected_output_file_name(self) -> str:
        """
        Retrieves the name of the current selected output file (see @ref SetCurrentSelectedOutputUserNumber).  This file name is used if not specified within <B>SELECTED_OUTPUT</B> input.
        The default value is <B><I>selected_n.id.out</I></B>, where id is obtained from @ref GetId.
        @return filename        The name of the file to write to.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringOn, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileName, SetSelectedOutputFileOn, SetSelectedOutputStringOn

        """
        ...

    def get_selected_output_file_on(self) -> bool:
        """
        Retrieves the current selected-output file switch (see @ref SetCurrentSelectedOutputUserNumber).
        @retval True            Output is written to the selected-output (<B><I>selected_n.id.out</I></B> if unspecified, where id is obtained from @ref GetId) file.
        @retval False           No output is written.
        @see                    GetSelectedOutputValue, GetSelectedOutputColumnCount, GetSelectedOutputRowCount, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn

        """
        ...

    def get_selected_output_row_count(self) -> int:
        """
        Retrieves the number of rows in the current selected-output buffer (see @ref SetCurrentSelectedOutputUserNumber).
        @return                 The number of rows.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputColumnCount, GetSelectedOutputFileOn, GetSelectedOutputValue, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn

        """
        ...

    def get_selected_output_string(self) -> str:
        """
        Retrieves the string buffer containing <b>SELECTED_OUTPUT</b> for the currently selected user number (see @ref SetCurrentSelectedOutputUserNumber).
        @return                 A null terminated string containing <b>SELECTED_OUTPUT</b>.
        @pre
            @ref SetSelectedOutputStringOn must have been set to True in order to receive <b>SELECTED_OUTPUT</b>.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputStringLine, GetSelectedOutputFileOn, GetSelectedOutputStringLineCount, GetSelectedOutputStringOn, GetSelectedOutputString, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn, SetSelectedOutputStringOn

        """
        ...

    def get_selected_output_string_line(self, n: int) -> str:
        """
        Retrieves the given selected output line of the currently selected user number (see @ref SetCurrentSelectedOutputUserNumber).
        @param n                The zero-based index of the line to retrieve.
        @return                 A null terminated string containing the given line.
                                Returns an empty string if n is out of range.
        @pre                    @ref SetSelectedOutputStringOn must have been set to True.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringLineCount, GetSelectedOutputStringOn, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn, SetSelectedOutputStringOn

        """
        ...

    def get_selected_output_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current selected output string buffer (see @ref SetCurrentSelectedOutputUserNumber).
        @return                 The number of lines.
        @pre                    @ref SetSelectedOutputStringOn must have been set to True.
        @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringLine, GetSelectedOutputStringOn, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn, SetSelectedOutputStringOn

        """
        ...

    def get_selected_output_string_on(self) -> bool:
        """
        Retrieves the value of the current selected output string switch (see @ref SetCurrentSelectedOutputUserNumber).
        @retval True            Output defined by the <B>SELECTED_OUTPUT</B> keyword is stored.
        @retval False           No output is stored.
        @see                    GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn, SetSelectedOutputStringOn

        """
        ...

    def get_selected_output_value(self, row: int, col: int) -> int | float | str:
        """
           Returns the @c VAR associated with the specified row and column.  The current <b>SELECTED_OUTPUT</b> block is set using the @ref SetCurrentSelectedOutputUserNumber method.
           @param row              The row index.
           @param col              The column index.

           @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputColumnCount, GetSelectedOutputFileOn, GetSelectedOutputRowCount, GetSelectedOutputValue2, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn
           @remarks
               Row 0 contains the column headings to the selected_ouput.
           @par Examples:
           The headings will include a suffix and/or prefix in order to differentiate the
           columns.
           @htmlonly
        <p>
        <table border=1>

        <TR VALIGN="top">
        <TH width=65%>
        Input
        </TH>
        <TH width=35%>
        Headings
        </TH>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -totals Ca Na
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          Ca(mol/kgw)  Na(mol/kgw)
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -molalities Fe+2 Hfo_sOZn+
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          m_Fe+2(mol/kgw)  m_Hfo_sOZn+(mol/kgw)
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -activities H+ Ca+2
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          la_H+  la_Ca+2
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -equilibrium_phases Calcite Dolomite
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          Calcite  d_Calcite  Dolomite  d_Dolomite
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -saturation_indices CO2(g) Siderite
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          si_CO2(g)  si_Siderite
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -gases CO2(g) N2(g)
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          pressure "total mol" volume g_CO2(g) g_N2(g)
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -kinetic_reactants CH2O Pyrite
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          k_CH2O dk_CH2O k_Pyrite dk_Pyrite
        </PRE></CODE>
        </TD>
        </TR>

        <TR VALIGN="top">
        <TD width=65%>
        <CODE><PRE>
          SELECTED_OUTPUT
                -reset False
                -solid_solutions CaSO4 SrSO4
        </PRE></CODE>
        </TD>
        <TD width=35%>
        <CODE><PRE>
          s_CaSO4 s_SrSO4
        </PRE></CODE>
        </TD>
        </TR>

        </table>
           @endhtmlonly

        """
        ...

    @staticmethod
    def get_version_string() -> str:
        """
        Retrieves the string buffer containing the version in the form of X.X.X-XXXX.
        @return                 A null terminated string containing the IPhreeqc version number.

        """
        ...

    def get_warning_string(self) -> str:
        """
        Retrieves the warning messages from the last call to @ref RunAccumulated, @ref RunFile, @ref RunString, @ref LoadDatabase, or @ref LoadDatabaseString.
        @return                 A null terminated string containing warning messages.
        @see                    GetWarningStringLine, GetWarningStringLineCount, OutputWarningString

        """
        ...

    def get_warning_string_line(self, n: int) -> str:
        """
        Retrieves the given warning line.
        @param n                The zero-based index of the line to retrieve.
        @return                 A null terminated string containing the given warning line message.
        @see                    GetWarningStringLineCount, OutputWarningString

        """
        ...

    def get_warning_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current warning string buffer.
        @return                 The number of lines.
        @see                    GetWarningStringLine, GetWarningString, OutputWarningString

        """
        ...

    def list_components(self) -> List[str]:
        """
        Retrieves the current list of components.
        @return                 The current list of components.
        @see                    GetComponent, GetComponentCount

        """
        ...

    def load_database(self, filename: str) -> int:
        """
        Load the specified database file into phreeqc.
        @param filename         The name of the phreeqc database to load.
                                The full path (or relative path with respect to the working directory) will be required if the file is not
                                in the current working directory.
        @return                 The number of errors encountered.
        @see                    LoadDatabaseString
        @remarks
            All previous definitions are cleared.

        """
        ...

    def load_database_string(self, input: str) -> int:
        """
        Load the specified string as a database into phreeqc.
        @param input            String containing data to be used as the phreeqc database.
        @return                 The number of errors encountered.
        @see                    LoadDatabaseString
        @remarks
            All previous definitions are cleared.

        """
        ...

    def output_accumulated_lines(self) -> None:
        """
        Output the accumulated input buffer to stdout.  The input buffer can be run with a call to @ref RunAccumulated.
        @see                    AccumulateLine, ClearAccumulatedLines, RunAccumulated

        """
        ...

    def output_error_string(self) -> None:
        """
        Output the error messages normally stored in the <B><I>phreeqc.id.err</I></B> (where id is obtained from @ref GetId)
        file to stdout.
        @see                    GetErrorStringLine, GetErrorStringLineCount, GetErrorFileOn, SetErrorFileOn

        """
        ...

    def output_warning_string(self) -> None:
        """
        Output the warning messages to stdout.
        @see                    GetWarningStringLine, GetWarningStringLineCount, GetWarningString

        """
        ...

    def run_accumulated(self) -> int:
        """
        Runs the input buffer as defined by calls to @ref AccumulateLine.
        @return                 The number of errors encountered.
        @see                    AccumulateLine, ClearAccumulatedLines, OutputAccumulatedLines, RunFile, RunString
        @remarks
            The accumulated input is cleared at the next call to @ref AccumulateLine.
        @pre
            @ref LoadDatabase/@ref LoadDatabaseString must have been called and returned 0 (zero) errors.

        """
        ...

    def run_file(self, filename: str) -> int:
        """
        Runs the specified phreeqc input file.
        @param filename         The name of the phreeqc input file to run.
        @return                 The number of errors encountered during the run.
        @see                    RunAccumulated, RunString
        @pre
            @ref LoadDatabase/@ref LoadDatabaseString must have been called and returned 0 (zero) errors.

        """
        ...

    def run_string(self, input: str) -> int:
        """
        Runs the specified string as input to phreeqc.
        @param input            String containing phreeqc input.
        @return                 The number of errors encountered during the run.
        @see                    RunAccumulated, RunFile
        @pre
            @ref LoadDatabase/@ref LoadDatabaseString must have been called and returned 0 (zero) errors.

        """
        ...

    def set_current_selected_output_user_number(self, n: int) -> bool:
        """
            Sets the current <B>SELECTED_OUTPUT</B> user number for use in subsequent calls to (@ref GetSelectedOutputColumnCount,
        @ref GetSelectedOutputFileName, @ref GetSelectedOutputRowCount, @ref GetSelectedOutputString, @ref GetSelectedOutputStringLine,
        @ref GetSelectedOutputStringLineCount, @ref GetSelectedOutputValue, @ref GetSelectedOutputValue2) routines.
            The initial setting is 1.
            @param n                The user number as specified in the <B>SELECTED_OUTPUT</B> block.
            @retval True            Success
            @retval False           The given user number has not been defined.
            @see                    GetCurrentSelectedOutputUserNumber, GetSelectedOutputColumnCount, GetSelectedOutputFileName, GetSelectedOutputRowCount, GetSelectedOutputString, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, GetSelectedOutputValue

        """
        ...

    def set_dump_file_name(self, filename: str) -> None:
        """
        Sets the name of the dump file.  This file name is used if not specified within <B>DUMP</B> input.
        The default value is <B><I>dump.id.out</I></B>, where id is obtained from @ref GetId.
        @param filename         The name of the file to write <B>DUMP</B> output to.
        @see                    GetDumpFileName, GetDumpFileOn, GetDumpString, GetDumpStringOn, GetDumpStringLine, GetDumpStringLineCount, SetDumpStringOn

        """
        ...

    def set_dump_file_on(self, b_value: bool) -> None:
        """
        Sets the dump file switch on or off.  This switch controls whether or not phreeqc writes to the <B>DUMP</B> (<B><I>dump.id.out</I></B>
        if unspecified, where id is obtained from @ref GetId) file.
        The initial setting is False.
        @param bValue           If True, turns on output to the <B>DUMP</B> file;
                                if False, turns off output to the <B>DUMP</B> file.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringOn, GetDumpStringLine, GetDumpStringLineCount, SetDumpStringOn

        """
        ...

    def set_dump_string_on(self, b_value: bool) -> None:
        """
        Sets the dump string switch on or off.  This switch controls whether or not the data normally sent
        to the dump file are stored in a buffer for retrieval.  The initial setting is False.
        @param bValue           If True, captures the output defined by the <B>DUMP</B> keyword into a string buffer;
                                if False, output defined by the <B>DUMP</B> keyword is not captured to a string buffer.
        @see                    GetDumpFileOn, GetDumpString, GetDumpStringOn, GetDumpStringLine, GetDumpStringLineCount, SetDumpFileOn

        """
        ...

    def set_error_file_name(self, filename: str) -> None:
        """
        Sets the name of the error file. The default value is <B><I>phreeqc.id.err</I></B>, where id is obtained from @ref GetId.
        @param filename         The name of the file to write error output to.
        @see                    GetErrorFileName, GetErrorFileOn, GetErrorString, GetErrorStringOn, GetErrorStringLine, GetErrorStringLineCount, SetErrorFileOn, SetErrorStringOn

        """
        ...

    def set_error_file_on(self, b_value: bool) -> None:
        """
        Sets the error file switch on or off.  This switch controls whether or not
        error messages are written to the <B><I>phreeqc.id.err</I></B> (where id is obtained from @ref GetId) file.
        The initial setting is True.
        @param bValue           If True, writes errors to the error file; if False, no errors are written to the error file.
        @see                    GetErrorStringLine, GetErrorStringLineCount, GetErrorFileOn, OutputErrorString

        """
        ...

    def set_error_on(self, b_value: bool) -> None:
        """
        Sets the error switch on or off.  This switch controls whether
        error messages are are generated and displayed.
        The initial setting is True.
        @param bValue           If True, error messages are sent to the error file and error string buffer; if False, no error messages are generated.
        @see                    GetErrorOn, GetErrorStringLine, GetErrorStringLineCount, GetErrorFileOn, OutputErrorString

        """
        ...

    def set_error_string_on(self, b_value: bool) -> None:
        """
        Sets the error string switch on or off.  This switch controls whether or not the data normally sent
        to the error file are stored in a buffer for retrieval.  The initial setting is True.
        @param bValue           If True, captures error output into a string buffer; if False, error output is not captured to a string buffer.
        @see                    GetErrorFileOn, GetErrorString, GetErrorStringOn, GetErrorStringLine, GetErrorStringLineCount, SetErrorFileOn

        """
        ...

    def set_log_file_name(self, filename: str) -> None:
        """
        Sets the name of the log file. The default value is <B><I>phreeqc.id.log</I></B>, where id is obtained from @ref GetId.
        @param filename         The name of the file to write log output to.
        @see                    GetLogFileName, GetLogFileOn, GetLogString, GetLogStringOn, GetLogStringLine, GetLogStringLineCount, SetLogFileOn, SetLogStringOn

        """
        ...

    def set_log_file_on(self, b_value: bool) -> None:
        """
        Sets the log file switch on or off.  This switch controls whether or not phreeqc
        writes log messages to the <B><I>phreeqc.id.log</I></B> (where id is obtained from @ref GetId) file.  The initial setting is False.
        @param bValue           If True, turns on output to the log file; if False, no log messages are written to the log file.
        @remarks
            Logging must be enabled through the use of the KNOBS -logfile option in order to receive any log messages.
        @see                    GetLogFileOn

        """
        ...

    def set_log_string_on(self, b_value: bool) -> None:
        """
        Sets the log string switch on or off.  This switch controls whether or not the data normally sent
        to the log file are stored in a buffer for retrieval.  The initial setting is False.
        @param bValue           If True, captures log output into a string buffer; if False, log output is not captured to a string buffer.
        @see                    GetLogFileOn, GetLogString, GetLogStringOn, GetLogStringLine, GetLogStringLineCount, SetLogFileOn

        """
        ...

    def set_output_file_name(self, filename: str) -> None:
        """
        Sets the name of the output file. The default value is <B><I>phreeqc.id.out</I></B>, where id is obtained from @ref GetId.
        @param filename         The name of the file to write phreeqc output to.
        @see                    GetOutputFileName, GetOutputFileOn, GetOutputString, GetOutputStringOn, GetOutputStringLine, GetOutputStringLineCount, SetOutputFileOn, SetOutputStringOn

        """
        ...

    def set_output_file_on(self, b_value: bool) -> None:
        """
        Sets the output file switch on or off.  This switch controls whether or not phreeqc
        writes to the <B><I>phreeqc.id.out</I></B> file (where id is obtained from @ref GetId).  This is the output that is normally generated
        when phreeqc is run.  The initial setting is False.
        @param bValue           If True, writes output to the output file; if False, no output is written to the output file.
        @see                    GetOutputFileOn

        """
        ...

    def set_output_string_on(self, b_value: bool) -> None:
        """
        Sets the output string switch on or off.  This switch controls whether or not the data normally sent
        to the output file are stored in a buffer for retrieval.  The initial setting is False.
        @param bValue           If True, captures output into a string buffer; if False, output is not captured to a string buffer.
        @see                    GetOutputFileOn, GetOutputString, GetOutputStringOn, GetOutputStringLine, GetOutputStringLineCount, SetOutputFileOn

        """
        ...

    def set_selected_output_file_name(self, filename: str) -> None:
        """
        Sets the name of the current selected output file (see @ref SetCurrentSelectedOutputUserNumber).  This file name is used if not specified within <B>SELECTED_OUTPUT</B> input.
        The default value is <B><I>selected_n.id.out</I></B>, where id is obtained from @ref GetId.
        @param filename         The name of the file to write <B>SELECTED_OUTPUT</B> output to.
        @see                    GetSelectedOutputFileName, GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringOn, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, SetCurrentSelectedOutputUserNumber, SetSelectedOutputStringOn

        """
        ...

    def set_selected_output_file_on(self, b_value: bool) -> None:
        """
        Sets the selected-output file switch on or off.  This switch controls whether or not phreeqc writes output to
        the current <B>SELECTED_OUTPUT</B> (<B><I>selected_n.id.out</I></B> if unspecified, where id is obtained from @ref GetId) file.
        The initial setting is False.
        @param bValue           If True, writes output to the selected-output file; if False, no output is written to the selected-output file.
        @see                    GetSelectedOutputColumnCount, GetSelectedOutputFileOn, GetSelectedOutputRowCount, GetSelectedOutputValue, SetCurrentSelectedOutputUserNumber

        """
        ...

    def set_selected_output_string_on(self, b_value: bool) -> None:
        """
        Sets the selected output string switch on or off.  This switch controls whether or not the data normally sent
        to the current <B>SELECTED_OUTPUT</B> file (see @ref SetCurrentSelectedOutputUserNumber) are stored in a buffer for retrieval.
        The initial setting is False.
        @param bValue           If True, captures the output defined by the <B>SELECTED_OUTPUT</B> keyword into a string buffer;
                                if False, output defined by the <B>SELECTED_OUTPUT</B> keyword is not captured to a string buffer.
        @see                    GetSelectedOutputFileOn, GetSelectedOutputString, GetSelectedOutputStringOn, GetSelectedOutputStringLine, GetSelectedOutputStringLineCount, SetCurrentSelectedOutputUserNumber, SetSelectedOutputFileOn

        """
        ...
