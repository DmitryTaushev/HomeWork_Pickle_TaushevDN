import pickle
music_band_dict = {
    'Led Zeppelin' : 'Led Zeppelin 2',
    'AC/DC' : 'Back in Black',
    'Black Sabbath' : 'Black Sabbath',
    'Guns n Roses' : 'Appetite for Destruction'
    }
class MethodDict:

    def __init__(self,music_band_dict):
        self.music_band_dict = music_band_dict

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
        with open('music_band_pickle.pkl', 'wb') as fp:
                pickle.dump(music_band_dict, fp, pickle.HIGHEST_PROTOCOL)
        return 'Произведен пиклинг в файл'

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileNotFoundError:
            return 'Файл не найден'
        return unpickle_data

method_dict = MethodDict(music_band_dict)

print(method_dict.data_insert(music_band_dict,'Black Keys','Attack and Release'))
print(method_dict.data_delete(music_band_dict,'AC/DC'))
print(method_dict.data_searching(music_band_dict,'Led Zeppelin'))
print(method_dict.data_refactor('Black Sabbath','Paranoid',music_band_dict))
print(method_dict.pickle_data())
print(method_dict.unpickle_file('music_band_pickle.pkl'))