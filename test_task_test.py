import test_task
output = test_task.test_fun()

def test1():
    assert type(output) == dict

def test2():
    assert output['cat'] == 'C2'

def test3():
    assert output['cs1Label'] == 'subcat'

def test4():
    assert output['cs3'] == 'USA,Finance'

def test5():
    assert output['dst'] == '1.1.1.1'

def test6():
    assert len(output) == 14

def test7():
    assert output.get('dhost') == 'bad.com'

def test8():
    assert output.get('cs41') == None



