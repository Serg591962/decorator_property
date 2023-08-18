#для чего проперти
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks)
st.name = "Anusha"
print(st.name)
print(st.gotmarks)#gotmarks, осталось таким же,
 #каким он был во время инициализации объекта student.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks())
st.name = "Anusha"
print(st.name)
print(st.gotmarks())#gotmarks изменяется во время вызова


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property#превращает метод в отрибут
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks)
st.name = "Anusha"
print(st.name)
print(st.gotmarks)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, marks = sentence.split(' ')
        self.name = name
        self.marks = marks

st = Student("Jaki", "25")
print(st.name)#Jaki
print(st.marks)#25
print(st.gotmarks)#Jaki obtained 25 marks
print("##################")
st.name = "Anusha"
print(st.name)#Anusha
print(st.gotmarks)#Anusha obtained 25 marks
print("##################")
st.gotmarks = 'Golam 36'
print(st.gotmarks)#Golam obtained 36 marks
print(st.name)#Golam
print(st.marks)#36

#Поскольку мы хотим обновить значение имени и меток, когда
#мы устанавливаем значение gotmarks. Итак, используя установщик
#декоратора @proprety, мы можем добиться этого.
#Обратите внимание, что мы написали @ gotmarks.setter, что
#означает, что мы применяем сеттер к методу gotmarks.
#Затем мы разбиваем предложение и обновляем значение имени и оценок.





