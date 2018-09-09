class DictExtensions:

    @staticmethod
    def extract_values_as_single_quote_string_from_dictionary(dict, index):
        try:
            return str(tuple(['{}'.format(str(sv)) for sv in tuple(dict[index].values())]))
        except IndexError:
            return None

    @staticmethod
    def extract_keys_as_string_from_dictionary(dict, index):
        try:
            return tuple(dict[index].keys())
        except IndexError:
            return None
