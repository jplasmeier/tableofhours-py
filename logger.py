# Logger for warnings and errors
import os


print_mode = True
text_file_mode = False

log_file_dir = os.getcwd()
error_text_file_name = 'error_log.txt'
error_file_path = os.path.join(log_file_dir, error_text_file_name)
warning_text_file_name = 'warning_log.txt'
warning_file_path = os.path.join(log_file_dir, warning_text_file_name)


def append_line_to_file(path, line_string):
    if not os.path.isfile(path):
        with open(path, 'w') as fp:
            fp.write('Log: \n')

    with open(path, 'a') as fp:
        fp.write(line_string + "\n")


def log_error(category, text):
    """
    Log an error with a specified category.
    :param category:
    :param text:
    :return:
    """
    error_msg = "Error in {0}: {1}".format(category, text)
    if print_mode:
        print(error_msg)
    if text_file_mode:
        append_line_to_file(error_file_path, error_msg)


def log_warning(category, text):
    warning_msg = "Warning in {0}: {1}".format(category, text)
    if print_mode:
        print(warning_msg)
    if text_file_mode:
        append_line_to_file(error_file_path, warning_msg)