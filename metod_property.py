#Создан класс KgToPounds с параметром kg, куда передается
#определенное количество килограмм, а с помощью метода
#to_pounds() они переводятся в фунты. Чтобы закрыть доступ
#к переменной kg реализованы методы set_kg() – для задания
#нового значения килограммов, get_kg() – для вывода текущего
#значения кг. Из-за этого возникло неудобство: нам нужно теперь
#использовать эти 2 метода для задания и вывода значений.
#Помогите переделать класс с использованием свойств-декораторов
#@property. Код приведен ниже.

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg * 2.205 #переводятся в фунты

    def set_kg(self, new_kg):#задания нового значения килограммов
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg * 2.205
        else:
            print('Килограммы задаются только числами')
    
    def get_kg(self):#вывода текущего значения кг
        return self.__kg

a = KgToPounds(50)
print(a.get_kg())
a.set_kg(60)
print(a.get_kg())

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg * 2.205 #переводятся в фунты

    def set_kg(self, new_kg):#задания нового значения килограммов
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg * 2.205
        else:
            print('Килограммы задаются только числами')
    
    def get_kg(self):#вывода текущего значения кг
        return self.__kg

    kg = property(fget = get_kg, fset = set_kg)#ф #возвращающяя экземпляр класса

a = KgToPounds(50)
print(a.kg)
a.kg = 60
print(a.kg)


class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg * 2.205 #переводятся в фунты
   
    
    def get_kg(self):#вывода текущего значения кг
        return self.__kg

    def set_kg(self, new_kg):#задания нового значения килограммов
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg * 2.205
        else:
            print('Килограммы задаются только числами')  

    kg = property() #позволяет использовать методы в качестве свойств объектов
    kg = kg.getter(get_kg)
    kg = kg.setter(set_kg)

a = KgToPounds(50)
print(a.kg)
a.kg = 60
print(a.kg)



class KgToPounds:

    def __init__(self, name, kg):
        self.__kg = kg * 2.205 #переводятся в фунты
        self.__name = name
    @property
    def met_kg(self):#вывода текущего значения кг
        return self.__name,self.__kg

    @met_kg.setter
    def met_kg(self, new_values):## Свойство для получения текущих значений
        new_name, new_kg = new_values
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg * 2.205
            self.__name = new_name
        else:
            print('Килограммы задаются только числами')  

   
a = KgToPounds('serg', 50)
print(a.met_kg)
a.met_kg = 'ivan', 60
print(a.met_kg)



















