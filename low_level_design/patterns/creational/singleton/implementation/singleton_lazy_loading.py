#implementation of singleton design pattern


#lazy loading- the singleton instance is created only when it's first needed initially instance is none then first time it is created

from typing_extensions import Self


class LazySingleton:
    _instance=None   #using class variable and keeping private although not using double underscore, it will work with double underscore also , but in python we treat single underscore variable is used for internal purpose only like private

    def __new__(cls) -> Self: #Singleton
        if cls._instance==None:
            # if instance is none means no object has been created then only it will create object otherwise not
            cls._instance=super().__new__(cls)

        return cls._instance
    

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls() #:-> Singleton()
        return cls._instance

def run_lazy_initialization_singleton():

    obj1=LazySingleton.get_instance()
    obj2=LazySingleton.get_instance()

    print(obj1 is obj2)
    print(obj1)
    print(obj2) #will still give first instance


