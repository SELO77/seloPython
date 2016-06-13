class LifeCycleClass():

  def __init__(self):
    print("__init__")

  def __await__(self):
    print("__await")

  def __exit__(self, exc_type, exc_val, exc_tb):
    print("__exit__")