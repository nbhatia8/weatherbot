
from .luis_parameter import LUISParameter

class LUISAction:
    '''
    LUIS Action Class.
    Describes the LUIS Action structure.
    '''

    def __init__(self, action):
        '''
        A constructor for the LUISAction class.
        :param action: A dictionary containing the action data.
        '''
        self._name = action['name']
        self._triggered = action['triggered']
        self._parameters = []
        for parameter in action['parameters']:
            self._parameters.append(LUISParameter(parameter))

    def get_name(self):
        '''
        A getter for the action's name.
        :return: Actions's name.
        '''
        return self._name

    def get_triggered(self):
        '''
        A getter for the action's triggered flag.
        :return: A boolean that expresses whether the action was trigerred or not.
        '''
        return self._triggered

    def get_parameters(self):
        '''
        A getter for the action's parameters.
        :return: A list of parameter.
        '''
        return self._parameters
