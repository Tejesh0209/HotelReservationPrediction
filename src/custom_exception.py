import traceback
import sys

class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.message = message
        self.error_detail = error_detail

    @staticmethod
    def get_detailed_message(error_message, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_lineno if exc_tb else 'Unknown'
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else 'Unknown'
        return f"Error occurred in file: {file_name} at line: {line_number} | Message: {error_message}"
    
    def __str__(self):
        detailed_message = self.get_detailed_message(self.message, self.error_detail)
        return detailed_message
