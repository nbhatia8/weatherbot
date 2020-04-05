

class LUISCompositeEntityChild:
    '''
    LUIS Composite Entity Child Class.
    Describes the LUIS Composite Entity Child structure.
    '''

    def __init__(self, composite_entity_child):
        '''
        A constructor for the LUISCompositeEntityChild class.
        :param composite_entity: A dictionary containing the composite entity child data.
        '''
        self._type = composite_entity_child['type']
        self._value = composite_entity_child['value']

    def get_type(self):
        '''
        A getter for the composite entity child's type.
        :return: Composite Entity Child's type.
        '''
        return self._type

    def get_value(self):
        '''
        A getter for the composite entity child's value.
        :return: Composite Entity Child's value.
        '''
        return self._value
