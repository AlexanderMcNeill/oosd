import os, re, threading, Queue


class PingCheck(threading.Thread):
    received_packages = re.compile(r"(\d) received")

    def __init__ (self,in_q, out_q, print_function):
        threading.Thread.__init__(self)
        self.in_q = in_q
        self.out_q = out_q
        self.daemon = True
        self.print_function = print_function

    def run(self):
        while True:
            ip = self.in_q.get()
            self.print_function(ip)
            result = self.get_ping_result(ip)

            self.out_q.put(result)
            self.in_q.task_done()

    def get_ping_result(self, ip):
        ping_out = os.popen("ping -q -c2 " + ip, "r")
        line = ""

        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = re.findall(self.received_packages, line)
            result = "IP address {0}: {1} received".format(ip, n_received)

        return result


class Reporter(threading.Thread):

    def __init__(self, out_q, print_function):
        threading.Thread.__init__(self)
        self.out_q = out_q
        self.print_function = print_function

    def run(self):
        while True:
            result = self.out_q.get()
            self.print_function(result)
            self.out_q.task_done()


def get_locked_print():
    lock = threading.Lock()

    def print_locked(input):
        lock.acquire()
        print(input)
        lock.release()
    return print_locked

if __name__ == "__main__":
    in_queue = Queue.Queue()
    out_queue = Queue.Queue()

    for suffix in range(1,255):
        ip = "10.25.1."+str(suffix)
        in_queue.put(ip)

    locked_print_function = get_locked_print()

    for n in xrange(10):
        check = PingCheck(in_queue, out_queue, locked_print_function)
        check.start()

    for n in xrange(10):
        reporter = Reporter(out_queue, locked_print_function)
        reporter.start()

    out = raw_input()
