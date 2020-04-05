

class LUISDialog:
    '''
    LUIS Dialog Class.
    Describes the LUIS Action structure.
    '''

    def __init__(self, dialog):
        '''
        A constructor for the LUISDialog class.
        :param action: A dictionary containing the dialog data.
        '''
        if 'prompt' in dialog:
            self._prompt = dialog['prompt']
        else:
            self._prompt = None

        if 'parameterName' in dialog:
            self._parameter_name = dialog['parameterName']
        else:
            self._parameter_name = None

        self._context_id = dialog['contextId']
        self._status = dialog['status']
        self._finished = self._status == 'Finished'

    def get_prompt(self):
        '''
        A getter for the dialog's prompt.
        :return: Dialog's prompt.
        '''
        return self._prompt

    def get_parameter_name(self):
        '''
        A getter for the dialog's parameter name.
        :return: Dialog's parameter name.
        '''
        return self._parameter_name

    def get_context_id(self):
        '''
        A getter for the dialog's context Id.
        :return: Dialog's prompt.
        '''
        return self._context_id

    def get_status(self):
        '''
        A getter for the dialog's status.
        :return: Dialog's status.
        '''
        return self._status

    def is_finished(self):
        '''
        Checks whether the dialog has finished or not.
        :return: A boolean that expresses whether the dialog has finished or not.
        '''
        return self._finished
