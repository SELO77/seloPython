class Parent(object):

    def print_name(name):
        print "name is %s" % name

class Child(Parent):

    def child_method(*args, **kwargs):
        self.print_name("SELO")
        print args
        print kwargs

Child().child_method()
