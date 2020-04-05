
from .luis_composite_entity_child import LUISCompositeEntityChild

class LUISCompositeEntity:
    '''
    LUIS Composite Entity Class.
    Describes the LUIS Composite Entity structure.
    '''

    def __init__(self, composite_entity):
        '''
        A constructor for the LUISCompositeEntity class.
        :param composite_entity: A dictionary containing the composite entity data.
        '''
        self._parent_type = composite_entity['parentType']
        self._value = composite_entity['value']
        self._composite_entity_children = []
        for composite_entity_child in composite_entity['children']:
            self._composite_entity_children.append(LUISCompositeEntityChild(composite_entity_child))

    def get_parent_type(self):
        '''
        A getter for the composite entity's parent type.
        :return: Composite Entity's parent type.
        '''
        return self._parent_type

    def get_value(self):
        '''
        A getter for the composite entity's value.
        :return: Composite Entity's value.
        '''
        return self._value

    def get_children(self):
        '''
        A getter for the composite entity's children.
        :return: Composite_Entity's children.
        '''
        return self._composite_entity_children
