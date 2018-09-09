from Common import DictOperations


class Query:

    def __init__(self, table_name):
        self.table_name = table_name
        self.query_built = ''
        self.table_alias = {}

    @classmethod
    def init(cls):
        cls('')

    def select(self):
        self.query_built += 'Select'
        return self

    def columns(self, column_names):
        self.query_built += ' {}'.format(column_names)
        return self

    def table(self, table_name):
        self.query_built += ' {}'.format(table_name)

    def column(self, column):
        self.query_built += ' ' + column
        return self

    def from_table(self, table_name=None):
        if table_name is not None and table_name != '' and table_name != ' ':
            self.table_name = table_name
        self.query_built += ' From {}'.format(self.table_name)
        return self

    def in_op(self):
        self.query_built += ' in'
        return self

    def not_null(self):
        self.query_built += ' not null'
        return self

    def is_null(self):
        self.query_built += ' is null'
        return self

    def exists(self):
        self.query_built += ' exists'
        return self

    def not_in(self):
        self.query_built += ' not in'
        return self

    def where(self):
        self.query_built += ' where'
        return self

    def where_column_operator_value(self, column, operator, value):
        self.query_built += ' Where {} {} {}'.format(column, operator, value)
        return self

    def where_column(self, column):
        self.query_built += ' Where {}'.format(column)
        return self

    def equals(self):
        self.query_built += ' ='
        return self

    def value(self, value):
        self.query_built += ' {}'.format(str(value))
        return self

    def where_null(self, column):
        self.query_built += ' where {} is null'.format(column)
        return self

    def where_not_null(self, column):
        self.query_built += ' where {} is not null'.format(column)
        return self

    def where_in_values(self, column, list_values_comma_seperated):
        if type(list_values_comma_seperated) is not list:
            self.query_built += ' where {} in ({})'.format(column, list_values_comma_seperated)
        return self

    def where_in(self, column):
        self.query_built += 'where {} in '.format(column)
        return self

    def where_not_in(self, column):
        self.query_built += ' Where {} not in '.format(column)
        return self

    def open_brackets(self):
        self.query_built += " ("
        return self

    def close_brackets(self):
        self.query_built += " )"
        return self

    def where_not_in_values(self, columns, list_values_comma_seperated):
        if type(list_values_comma_seperated) is not list:
            self.query_built += ' Where {} not in ({})'.format(columns, list_values_comma_seperated)
        return self

    def where_column_relates_another_column(self, column, operator, another_column):
        self.query_built += ' where {} {} {}'.format(column, operator, another_column)
        return self

    def where_column_relates_value(self, column, operator, value):
        self.query_built += ' where {} {} {}'.format(column, operator, value)
        return self

    def alias(self, alias_name):
        self.table_alias[self.table_name] = alias_name
        self.query_built += ' as {}'.format(alias_name)
        return self

    def join(self, join_table_name, alias_name):
        self.table_alias[join_table_name] = alias_name
        self.query_built += ' join {} as {}'.format(join_table_name, alias_name)
        return self

    def on(self):
        self.query_built += ' on'
        return self

    def join_column(self, table_name, column_name):
        self.query_built += ' {}.{}'.format(self.table_alias[table_name], column_name)
        return self

    def condition(self, condition):
        self.query_built += ' {}'.format(condition)
        return self

    def or_op(self):
        self.query_built += ' Or'
        return self

    def and_op(self):
        self.query_built += ' And'
        return self

    def greater_than(self):
        self.query_built += ' >'
        return self

    def greater_than_or_equal_to(self):
        self.query_built += ' >='
        return self

    def less_than(self):
        self.query_built += ' <'
        return self

    def less_than_or_equal_to(self):
        self.query_built += ' <='
        return self

    def another_column_condition(self, column):
        self.query_built += ' {}'.format(column)
        return self

    def union(self):
        self.query_built += ' {} '.format('union')
        return self

    def intersect(self):
        self.query_built += ' {} '.format('intersect')
        return self

    def insert_multiple(self, table_name, key_values):
        if type(key_values) is not list:
            raise TypeError('Expected list of dictionary')
        key_str = str(DictOperations.DictExtensions.extract_keys_as_string_from_dictionary(key_values, 0))
        values_str_list = []
        value_str = ''
        for indexer in range(0, len(key_values)):
            values_str_list.append(
                DictOperations.DictExtensions.extract_values_as_single_quote_string_from_dictionary(key_values,
                                                                                                    indexer))
        if values_str_list is not None and len(values_str_list):
            value_str = ', '.join(values_str_list)
        self.query_built += "Insert into {} {} values {}".format(table_name, key_str.replace("'", ""), value_str)

    def update(self):
        self.query_built += 'Update '
        return self

    def set_op(self):
        self.query_built += ' Set'
        return self

    def insert(self):
        self.query_built += 'Insert'
        return self

    def values(self):
        self.query_built += ' values'
        return self

    def delete(self):
        self.query_built += 'Delete '
        return self
