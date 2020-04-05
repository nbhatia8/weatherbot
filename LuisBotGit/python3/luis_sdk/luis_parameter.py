
from .luis_parametervalue import LUISParameterValue

class LUISParameter:
    '''
    LUIS Parameter Class.
    Describes the LUIS Parameter structure.
    '''

    def __init__(self, parameter):
        '''
        A constructor for the LUISParameter class.
        :param parameter: A dictionary containing the parameter data.
        '''
        self._name = parameter['name']
        self._required = parameter['required']
        self._parameter_values = []
        if parameter['value']:
            for parameter_value in parameter['value']:
                self._parameter_values.append(LUISParameterValue(parameter_value))

    def get_name(self):
        '''
        A getter for the parameter's name.
        :return: Parameter's name.
        '''
        return self._name

    def get_required(self):
        '''
        A getter for the parameter's required flag.
        :return: A boolean that expresses whether the parameter is required or not.
        '''
        return self._required

    def get_parameter_values(self):
        '''
        A getter for the parameters's values.
        :return: A list of parameter values.
        '''
        return self._parameter_values
