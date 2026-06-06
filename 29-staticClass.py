class Demo:
    x=10
    def __init__(self):
        self.y=20
        self.z=30

    def instance_method(self):
        print(self.y)
        print(self.z)

    @staticmethod
    def static_method():
        print(Demo.x)

    @classmethod
    def class_method(cls):
        print("python")
        print(Demo.x)

Demo.static_method()
Demo.class_method()
d1=Demo()
d1.instance_method()