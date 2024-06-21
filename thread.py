# from time import sleep
# class A:
#     def run(self):
#         for i in range(5):
#             print("shivam")
#             sleep(1)
# class B:
#     def run(self):
#         for i in range(5):
#             print("mishra")
#             sleep(1)
            
# t1=A()
# t2=B()

# t1.run()
# t2.run()
from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("shivam")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print("mishra")
            sleep(1)
            
t1=A()
t2=B()

t1.start()
t2.start() 