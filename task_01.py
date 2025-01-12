import pickle
country_dict = {
    'Russia' : 'Moscow',
    'USA' : 'WashingtonDC',
    'Belarus' : 'Minsk',
    'Germany' : 'Berlin'
    }
class MethodDict:

    def __init__(self,country_dict):
        self.country_dict = country_dict

    def data_insert(self,dictionary,data_insert_keys,data_insert_value):
        dictionary[data_insert_keys] = data_insert_value
        return dictionary

    def data_delete(self,dictionary,data_delete):
        del dictionary[data_delete]
        return dictionary

    def data_searching(self,dictionary,data_search):
        for i in dictionary:
            if i == data_search:
                return dictionary[data_search]
            else:
                return 'Данных нет'

    def data_refactor(self, data_search,data_refactor,dictionary):
        dictionary[data_search] = data_refactor
        return dictionary

    def pickle_data(self):
        with open('country_pickle.pkl', 'wb') as fp:
                pickle.dump(country_dict, fp, pickle.HIGHEST_PROTOCOL)
        return 'Произведен пиклинг в файл'

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileNotFoundError:
            return 'Файл не найден'
        return unpickle_data



method_dict = MethodDict(country_dict)

print(method_dict.data_insert(country_dict,'France','Paris'))
print(method_dict.data_delete(country_dict,'Russia'))
print(method_dict.data_searching(country_dict,'Germ'))
print(method_dict.data_refactor('Germany','Praga',country_dict))
print(method_dict.pickle_data())
print(method_dict.unpickle_file('country_pickle.pkl'))