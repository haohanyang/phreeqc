from typing import List, Dict

class Phreeqc:
    def accumulate_line(self, line: str) -> None:
        """
        Accumlulate line(s) for input to phreeqc.

        :param line: The line(s) to add for input to phreeqc.

        """
        ...

    def add_error(self, error_msg: str) -> int:
        """
        Appends the given error message and increments the error count. Internally used to create an error condition.

        :param error_msg: The error message to display.

        """
        ...

    def add_warning(self, warning_msg: str) -> int:
        """
        Appends the given warning message and increments the warning count. Internally used to create a warning condition.

        :param warning_msg: The warning message to display.

        """
        ...

    def clear_accumulated_lines(self) -> None:
        """
        Clears the accumulated input buffer. Input buffer is accumulated from calls to .

        """
        ...

    def get_accumulated_lines(self) -> str:
        """
        Retrieve the accumulated input string. The accumulated input string can be run with .

        """
        ...

    def get_component(self, n: int) -> str:
        """
        Retrieves the given component.

        :param n: The zero-based index of the component to retrieve.
        """
        ...

    def get_component_count(self) -> int:
        """
        Retrieves the number of components in the current list of components.
        """
        ...

    def get_current_selected_output_user_number(self) -> int:
        """
        Retrieves the current  user number. The initial setting is 1.
        """
        ...

    def get_dump_file_name(self) -> str:
        """
        Retrieves the name of the dump file.  This file name is used if not specified within <B>DUMP</B> input.
            The default value is <B><I>dump.id.out</I></B>, where id is obtained from GetId.
        """
        ...

    def get_dump_file_on(self) -> bool:
        """
        Retrieves the current value of the dump file switch.

        :return: true: Output is written to the DUMP (dump.id.out if unspecified, where id is obtained from GetId) file., false: No output is written.,
        """
        ...

    def get_dump_string(self) -> str:
        """
        Retrieves the string buffer containing  output.


        """
        ...

    def get_dump_string_line(self, n: int) -> str:
        """
        Retrieves the given dump line.

        :param n: The zero-based index of the line to retrieve.

        """
        ...

    def get_dump_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current dump string buffer.


        """
        ...

    def get_dump_string_on(self) -> bool:
        """
        Retrieves the current value of the dump string switch.

        :return: true: Output defined by the DUMP keyword is stored., false: No output is stored.,
        """
        ...

    def get_error_file_name(self) -> str:
        """
        Retrieves the name of the error file. The default value is , where id is obtained from .


        """
        ...

    def get_error_file_on(self) -> bool:
        """
        Retrieves the current value of the error file switch.

        :return: true: Errors are written to the phreeqc.id.err (where id is obtained from GetId) file., false: No errors are written.,
        """
        ...

    def get_error_on(self) -> bool:
        """
        Retrieves the current value of the error switch.

        :return: true: Error messages are sent to the error file and to the string buffer, false: No errors are sent.,
        """
        ...

    def get_error_string(self) -> str:
        """
        Retrieves the error messages from the last call to , , , , or .


        """
        ...

    def get_error_string_line(self, n: int) -> str:
        """
        Retrieves the given error line.

        :param n: The zero-based index of the line to retrieve.

        """
        ...

    def get_error_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current error string buffer.


        """
        ...

    def get_error_string_on(self) -> bool:
        """
        Retrieves the current value of the error string switch.

        :return: true: Error output is stored., false: No error output is stored.,
        """
        ...

    def get_id(self) -> int:
        """
        Retrieves the id of this object. Each instance receives an id which is incremented for each instance starting with the value zero.


        """
        ...

    def get_log_file_name(self) -> str:
        """
        Retrieves the name of the log file. The default value is , where id is obtained from .

        """
        ...

    def get_log_file_on(self) -> bool:
        """
        Retrieves the current value of the log file switch.

        :return: true: Log messages are written to the phreeqc.id.log (where id is obtained from GetId) file., false: No log messages are written.,
        """
        ...

    def get_log_string(self) -> str:
        """
        Retrieves the string buffer containing phreeqc log output.

        """
        ...

    def get_log_string_line(self, n: int) -> str:
        """
        Retrieves the given log line.

        :param n: The zero-based index of the line to retrieve.

        """
        ...

    def get_log_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current log string buffer.

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

        :return: true: Log output is stored., false: No log output is stored.,
        """
        ...

    def get_nth_selected_output_user_number(self, n: int) -> int:
        """
        Retrieves the nth user number of the currently defined  blocks.

        :param n: The zero-based index of the SELECTED_OUTPUT user number to retrieve.

        """
        ...

    def get_output_file_name(self) -> str:
        """
        Retrieves the name of the output file. The default value is , where id is obtained from .

        """
        ...

    def get_output_file_on(self) -> bool:
        """
        Retrieves the current value of the output file switch.

        :return: true: Output is written to the phreeqc.id.out (where id is obtained from GetId) file., false: No output is written.,
        """
        ...

    def get_output_string(self) -> str:
        """
        Retrieves the string buffer containing phreeqc output.

        """
        ...

    def get_output_string_line(self, n: int) -> str:
        """
        Retrieves the given output line.

        :param n: The zero-based index of the line to retrieve.

        """
        ...

    def get_output_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current output string buffer.


        """
        ...

    def get_output_string_on(self) -> bool:
        """
        Retrieves the current value of the output string switch.

        :return: true: Phreeqc output is stored., false: No phreeqc output is stored.,
        """
        ...

    def get_selected_output_column_count(self) -> int:
        """
        Retrieves the number of columns in the current selected-output buffer.

        """
        ...

    def get_selected_output_count(self) -> int:
        """
        Retrieves the count of  blocks that are currently defined.

        """
        ...

    def get_selected_output_file_name(self) -> str:
        """
        Retrieves the name of the current selected output file. This file name is used if not specified within  input. The default value is , where id is obtained from .

        """
        ...

    def get_selected_output_file_on(self) -> bool:
        """
        Retrieves the current selected-output file switch.

        :return: true: Output is written to the selected-output (selected_n.id.out if unspecified, where id is obtained from GetId) file., false: No output is written.,
        """
        ...

    def get_selected_output_row_count(self) -> int:
        """
        Retrieves the number of rows in the current selected-output buffer.


        """
        ...

    def get_selected_output_string(self) -> str:
        """
        Retrieves the string buffer containing  for the currently selected user number.

        """
        ...

    def get_selected_output_string_line(self, n: int) -> str:
        """
        Retrieves the given selected output line of the currently selected user number.

        :param n: The zero-based index of the line to retrieve.
        """
        ...

    def get_selected_output_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current selected output string buffer.
        """
        ...

    def get_selected_output_string_on(self) -> bool:
        """
        Retrieves the value of the current selected output string switch.

        :return: true: Output defined by the SELECTED_OUTPUT keyword is stored; false: No output is stored.,
        """
        ...

    def get_selected_output_value(self, row: int, col: int) -> int | float | str:
        """
        Returns the value associated with the specified row and column.

        :param row: The row index.
        :param col: The column index.
        """
        ...

    def get_warning_string(self) -> str:
        """
        Retrieves the warning messages from the last call to RunAccumulated, RunFile, RunString, LoadDatabase, or LoadDatabaseString.
        """
        ...

    def get_warning_string_line(self, n: int) -> str:
        """
        Retrieves the given warning line.

        :param n: The zero-based index of the line to retrieve.

        """
        ...

    def get_warning_string_line_count(self) -> int:
        """
        Retrieves the number of lines in the current warning string buffer.

        """
        ...

    def list_components(self) -> List[str]:
        """
        Retrieves the current list of components.
        """
        ...

    def load_database(self, filename: str) -> int:
        """
        Load the specified database file into phreeqc.

        :param filename: The name of the phreeqc database to load. The full path (or relative path with respect to the working directory) will be required if the file is not in the current working directory.
        """
        ...

    def load_database_string(self, input: str) -> int:
        """
        Load the specified string as a database into phreeqc.

        :param input: String containing data to be used as the phreeqc database.
        """
        ...

    def output_accumulated_lines(self) -> None:
        """
        Output the accumulated input buffer to stdout. The input buffer can be run with a call to .
        """
        ...

    def output_error_string(self) -> None:
        """
        Output the error messages normally stored in the  (where id is obtained from ) file to stdout.
        """
        ...

    def output_warning_string(self) -> None:
        """
        Output the warning messages to stdout.
        """
        ...

    def run_accumulated(self) -> int:
        """
        Runs the input buffer as defined by calls to .

        """
        ...

    def run_file(self, filename: str) -> int:
        """
        Runs the specified phreeqc input file.

        :param filename: The name of the phreeqc input file to run.

        """
        ...

    def run_string(self, input: str) -> int:
        """
        Runs the specified string as input to phreeqc.

        :param input: String containing phreeqc input.

        """
        ...

    def set_current_selected_output_user_number(self, n: int) -> VRESULT:
        """
        Sets the current <B>SELECTED_OUTPUT</B> user number for use in subsequent calls to (GetSelectedOutputColumnCount,
        GetSelectedOutputFileName,  GetSelectedOutputRowCount, GetSelectedOutputString, GetSelectedOutputStringLine,
        GetSelectedOutputStringLineCount, GetSelectedOutputValue, GetSelectedOutputValue2) routines.

        The initial setting is 1.

        :param n: The user number as specified in the SELECTED_OUTPUT block.
        :return: VR_OK: Success; VR_INVALIDARG: The given user number has not been defined.
        """
        ...

    def set_dump_file_name(self, filename: str) -> None:
        """
        Sets the name of the dump file. This file name is used if not specified within  input. The default value is , where id is obtained from .

        :param filename: The name of the file to write DUMP output to.

        """
        ...

    def set_dump_file_on(self, bValue: bool) -> None:
        """
        Sets the dump file switch on or off. This switch controls whether or not phreeqc writes to the  ( if unspecified, where id is obtained from ) file. The initial setting is false.

        :param bValue: If true, turns on output to the DUMP file; if false, turns off output to the DUMP file.

        """
        ...

    def set_dump_string_on(self, bValue: bool) -> None:
        """
        Sets the dump string switch on or off. This switch controls whether or not the data normally sent to the dump file are stored in a buffer for retrieval. The initial setting is false.

        :param bValue: If true, captures the output defined by the DUMP keyword into a string buffer; if false, output defined by the DUMP keyword is not captured to a string buffer.

        """
        ...

    def set_error_file_name(self, filename: str) -> None:
        """
        Sets the name of the error file. The default value is , where id is obtained from .

        :param filename: The name of the file to write error output to.

        """
        ...

    def set_error_file_on(self, bValue: bool) -> None:
        """
        Sets the error file switch on or off. This switch controls whether or not error messages are written to the  (where id is obtained from ) file. The initial setting is true.

        :param bValue: If true, writes errors to the error file; if false, no errors are written to the error file.

        """
        ...

    def set_error_on(self, bValue: bool) -> None:
        """
        Sets the error switch on or off. This switch controls whether error messages are are generated and displayed. The initial setting is true.

        :param bValue: If true, error messages are sent to the error file and error string buffer; if false, no error messages are generated.

        """
        ...

    def set_error_string_on(self, bValue: bool) -> None:
        """
        Sets the error string switch on or off. This switch controls whether or not the data normally sent to the error file are stored in a buffer for retrieval. The initial setting is true.

        :param bValue: If true, captures error output into a string buffer; if false, error output is not captured to a string buffer.

        """
        ...

    def set_log_file_name(self, filename: str) -> None:
        """
        Sets the name of the log file. The default value is , where id is obtained from .

        :param filename: The name of the file to write log output to.

        """
        ...

    def set_log_file_on(self, bValue: bool) -> None:
        """
        Sets the log file switch on or off. This switch controls whether or not phreeqc writes log messages to the  (where id is obtained from ) file. The initial setting is false.

        :param bValue: If true, turns on output to the log file; if false, no log messages are written to the log file.

        """
        ...

    def set_log_string_on(self, bValue: bool) -> None:
        """
        Sets the log string switch on or off. This switch controls whether or not the data normally sent to the log file are stored in a buffer for retrieval. The initial setting is false.

        :param bValue: If true, captures log output into a string buffer; if false, log output is not captured to a string buffer.

        """
        ...

    def set_output_file_name(self, filename: str) -> None:
        """
        Sets the name of the output file. The default value is , where id is obtained from .

        :param filename: The name of the file to write phreeqc output to.

        """
        ...

    def set_output_file_on(self, bValue: bool) -> None:
        """
        Sets the output file switch on or off. This switch controls whether or not phreeqc writes to the  file (where id is obtained from ). This is the output that is normally generated when phreeqc is run. The initial setting is false.

        :param bValue: If true, writes output to the output file; if false, no output is written to the output file.

        """
        ...

    def set_output_string_on(self, bValue: bool) -> None:
        """
        Sets the output string switch on or off. This switch controls whether or not the data normally sent to the output file are stored in a buffer for retrieval. The initial setting is false.

        :param bValue: If true, captures output into a string buffer; if false, output is not captured to a string buffer.

        """
        ...

    def set_selected_output_file_name(self, filename: str) -> None:
        """
        Sets the name of the current selected output file. This file name is used if not specified within  input. The default value is , where id is obtained from .

        :param filename: The name of the file to write SELECTED_OUTPUT output to.

        """
        ...

    def set_selected_output_file_on(self, bValue: bool) -> None:
        """
        Sets the selected-output file switch on or off. This switch controls whether or not phreeqc writes output to the current  ( if unspecified, where id is obtained from ) file. The initial setting is false.

        :param bValue: If true, writes output to the selected-output file; if false, no output is written to the selected-output file.

        """
        ...

    def set_selected_output_string_on(self, bValue: bool) -> None:
        """
        Sets the selected output string switch on or off. This switch controls whether or not the data normally sent to the current  file are stored in a buffer for retrieval. The initial setting is false.

        :param bValue: If true, captures the output defined by the SELECTED_OUTPUT keyword into a string buffer; if false, output defined by the SELECTED_OUTPUT keyword is not captured to a string buffer.

        """
        ...
