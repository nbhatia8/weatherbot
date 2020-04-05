
class LUISParameterValue:
    '''
    LUIS Paramater Value Class.
    Describes the LUIS Paramter Value structure.
    '''

    def __init__(self, parameter_value):
        '''
        A constructor for the LUISAction class.
        :param parameter_value: A dictionary containing the parameter value data.
        '''
        self._name = parameter_value['entity']
        self._type = parameter_value['type']
        if 'score' in parameter_value:
            self._score = parameter_value['score']
        else:
            self._score = None
        if 'resolution' in parameter_value:
            self._resolution = parameter_value['resolution']
        else:
            self._resolution = None


    def get_name(self):
        '''
        A getter for the parameter value's name.
        :return: Parameter value's name.
        '''
        return self._name

    def get_type(self):
        '''
        A getter for the parameter value's type.
        :return: Parameter value's type.
        '''
        return self._type

    def get_score(self):
        '''
        A getter for the parameter value's score.
        :return: Parameter value's score.
        '''
        return self._score

    def get_resolution(self):
        '''
        A getter for the parameter value's resolution.
        :return: Parameter value's resolution.
        '''
        return self._resolution
