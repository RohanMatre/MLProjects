import sys
import logging

# message should like the file with CustomException
def error_message_details(error,error_detail:sys):
    # Probably Give us all the errors in which file it occur
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # search it on Custom Exception Handling in python
    error_message = "Error Occured in Python Script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message

#if __name__ == "__main__":

#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Divide by ZeroError")
#        raise CustomException(e,sys)