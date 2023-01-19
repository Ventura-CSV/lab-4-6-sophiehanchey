import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '3'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    regex_string = r'[\w,\W]*0[\w,\W]*0[\w,\W]*'
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*1[\w,\W]*0[\w,\W]*[\w,\W]*1[\w,\W]*1[\w,\W]*'
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*2[\w,\W]*0[\w,\W]*[\w,\W]*2[\w,\W]*1[\w,\W]*[\w,\W]*2[\w,\W]*2[\w,\W]*'
    res = re.search(regex_string, lines[2])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '5'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*' + str(minval) + r'[\w,\W]*'
    # res = re.search(regex_string, lines[0])
    regex_string = r'[\w,\W]*0[\w,\W]*0[\w,\W]*'
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*1[\w,\W]*0[\w,\W]*[\w,\W]*1[\w,\W]*1[\w,\W]*'
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*2[\w,\W]*0[\w,\W]*[\w,\W]*2[\w,\W]*1[\w,\W]*[\w,\W]*2[\w,\W]*2[\w,\W]*'
    res = re.search(regex_string, lines[2])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*3[\w,\W]*0[\w,\W]*[\w,\W]*3[\w,\W]*1[\w,\W]*[\w,\W]*3[\w,\W]*2[\w,\W]*[\w,\W]*3[\w,\W]*[\w,\W]*3[\w,\W]*'
    res = re.search(regex_string, lines[3])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*4[\w,\W]*0[\w,\W]*[\w,\W]*4[\w,\W]*1[\w,\W]*[\w,\W]*4[\w,\W]*2[\w,\W]*[\w,\W]*4[\w,\W]*[\w,\W]*3[\w,\W]*[\w,\W]*4[\w,\W]*[\w,\W]*4[\w,\W]*'
    res = re.search(regex_string, lines[4])
    assert res != None
    print(res.group())
