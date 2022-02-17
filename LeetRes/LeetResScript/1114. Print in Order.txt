import threading
class Foo:
    def __init__(self):
            self.lock = threading.Lock()
        self.lock.acquire()
        self.lock2 = threading.Lock()
        self.lock2.acquire()
        def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
                    printFirst()
        self.lock.release()
    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock.acquire()
        printSecond()
        self.lock2.release()
            def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.lock2.acquire()
        printThird()
        