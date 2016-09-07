class TestClass(object):
    INVITE_SCORE_SYSTEM = [(10, 50), (100, 50), (1000, 50), (float('inf'), 50)]

    def test(self):
        score_system = getattr(self, "{0}_SCORE_SYSTEM".format("INVITE"))
        print score_system

if __name__ == "__main__":
    TestClass().test()
