first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_func = lambda x, y: [False if x[i] != y[i] else True for i in range(len(x))]
print(*list(map(lambda_func, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
