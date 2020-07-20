# 実行結果
# Hello, I am Alice
# I am 18 years old


# クラス定義を変更してはいけません
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def showName(self) :
        print("Hello, I am " + self.name)
        
    def showAge(self) :
        print("I am " + str(self.age) + " years old")

# インスタンスの作成
person1 = Person("Alice", 18)

# 以下の部分にインスタンスを利用して、メソッドを呼び出す処理を作成します
# 「showName」メソッドと「showAge」メソッドを呼び出す処理を作成します


