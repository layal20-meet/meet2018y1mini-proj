Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=['she', 'selld', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> b="selfish shellfish"
>>> c=[1, 1, 2, 3, 5, 8, 13]
>>> b[3:4]
'f'
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[2]
'sea'
>>> a[2:4]
['sea', 'shells']
>>> c[1]
1
>>> c[1]+c[2]
3
>>> a[3]
'shells'
>>> " "+a[3]
' shells'
>>> a*3
['she', 'selld', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'selld', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'selld', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> 'self'in b
True
>>> one=[1,2,3,4]
>>> two=[7,6,5,4]
>>> three=["y1", "friends", "fun"]
>>> print(one=two)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(one=two)
TypeError: 'one' is an invalid keyword argument for this function
>>> print(one+two)
[1, 2, 3, 4, 7, 6, 5, 4]
>>> print(one[3])
4
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> one.append(4)
>>> print(one)
[1, 2, 3, 4]
>>> 
