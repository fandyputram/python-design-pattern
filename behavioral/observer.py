class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Observer:
    def update(self, subject):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        self._state = subject.state
        print(f"{self._name} has been notified with new state: {self._state}")


# Example usage
subject = ConcreteSubject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.state = 10
subject.state = 20

subject.detach(observer2)

subject.state = 30
