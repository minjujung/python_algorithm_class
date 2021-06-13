# 5번 라인은 클래스를 생성했을 때, 즉 Person()이 호출되는 순간에 
# class Person내부의 함수가 불리게 되면서 실행됨
class Person:
    def __init__(self,param_name):
        print("I am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다!")

person_1 = Person("한지민")
print(person_1.name)
person_1.talk()
person_2 = Person("이나영")
print(person_2.name)
person_2.talk()