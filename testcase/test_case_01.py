import pytest

class TestCase():
    age = 10
    @pytest.mark.run(order=3)
    def test_jiajia(self):
        print("jiajia")

    # @pytest.mark.skipif(age< 11, reason='就不执行')
    @pytest.mark.run(order=2)
    def test_pengpeng(self, my_fixture):
        print("pengpeng")
        print(my_fixture)
        # assert 1==2

    @pytest.mark.run(order=1)
    def test_dingding(self):
        print("dingding")

    def test_xixi(self):
        print("xixi")

if __name__ == '__main__':
    # pass
    pytest.main([ 'test_case_01.py'])
    # pytest.main(['-vs', '../testcase/test_case_01.py::TestCase::test_pengpeng'])
    # pytest.main(['-vs', '../testcase', '-n=2', '--maxfail=2', '--html=../report/report.html'])