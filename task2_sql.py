'''Task
====

Write a wrapper class TableData for database table, that when initialized with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
 -  `len(presidents)` will give current amount of rows in presidents table in database
 -  `presidents['Yeltsin']` should return single data row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data. If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.

'''

'''Задача
====

Напишите класс-оболочку tableData для таблицы базы данных, который при инициализации именем базы данных и таблицей действует как объект сбора (реализует протокол сбора).
Предположим, что все данные имеют уникальные значения в столбце "имя".
Итак, если президенты = табличные данные(имя_базы_данных='example.sqlite', имя_таблицы='президенты')

затем
 - `len(президенты)` выдаст текущее количество строк в таблице президентов в базе данных
 - `президенты["Ельцин"]" должны возвращать одну строку данных для президента с именем Ельцин
 - `Ельцин" в разделе "президенты" должен возвращать, если в таблице есть президент с таким именем
 - object реализует протокол итераций. т.е. вы могли бы использовать его в циклах for::
       для president в presidents:
           print(president['имя'])
 - все вышеупомянутые вызовы должны отражать самые последние данные. Если данные в таблице изменились после того, как вы создали экземпляр collection, ваши вызовы должны возвращать обновленные данные.

Избегайте чтения всей таблицы в память. При повторном просмотре записей начните чтение с первой записи, затем переходите к следующей, пока записи не будут исчерпаны.
При написании тестов не всегда необходимо полностью имитировать вызовы базы данных. Используйте предоставленный файл example.sqlite в качестве файла настроек базы данных.'''



import sqlite3


class TableData():


    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()


    def __len__(self):
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        return self.cursor.fetchone()[0]


    def __getitem__(self, name):
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE name = '{name}'")
        row = self.cursor.fetchone()
        if row is None:
            raise KeyError(f"No entry found for name: {name}")
        return row


    def __contains__(self, name):
        self.cursor.execute(f"SELECT 1 FROM {self.table_name} WHERE name = '{name}'")
        return self.cursor.fetchone() is not None


    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor:
            yield row


if __name__ == "__main__":
    presidents = TableData(database_name='1103/example.sqlite', table_name='presidents')
    print(len(presidents)) 
    print(presidents['Yeltsin'])
    print('Yeltsin' in presidents)
    for president in presidents:
        print(president) 