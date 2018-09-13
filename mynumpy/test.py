
class Animal(object):
    def run(self):
        print('Animal is running...')

class Timer(object):
    def run(self):
        print('Start...')


def run_twice(animal):
    animal.run()
    animal.run()


print(run_twice(Timer()))