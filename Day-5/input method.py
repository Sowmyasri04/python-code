Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
a
>>> a
'a'
>>> 5
5
>>> type(a)
<class 'str'>
>>> a=int(input())
5
>>> a
5
>>> type(a)
<class 'int'>
>>> a=int(input("Enter a integer:))
	    
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> a=int(input("Enter a integer:"))
Enter a integer:8
>>> a
8
>>> a=float(input())
15
>>> a
15.0
>>> a=float(input("Enter a float:"))
Enter a float:12
>>> a
12.0
>>> type(a)
<class 'float'>
>>> a=input().split()
12 23 45 788
>>> a
['12', '23', '45', '788']
>>> a=list(map(int,input().split()))
12 5677 688 75
>>> a
[12, 5677, 688, 75]
>>> a=list(map(float,input().split()))
44 77 865 23
>>> a
[44.0, 77.0, 865.0, 23.0]
>>> a=tuple(input().split())
23 68 34 78
>>> a
('23', '68', '34', '78')
>>> a=tuple(map(int,input().split()))
13 567 743 08
>>> a
(13, 567, 743, 8)
>>> a=tuple(map(float,input().split()))
23 56 98 33
>>> a
(23.0, 56.0, 98.0, 33.0)
>>> a=set(input().split())
13 87 25 92
>>> a
{'92', '87', '25', '13'}
>>> a=set(map(int,input().split()))
25 87 249 24
>>> a
{24, 25, 249, 87}
>>> a=set(map(float,input().split()))
265 86 2154 878
>>> a
{265.0, 2154.0, 878.0, 86.0}
>>> a,b,c=list(map(int,input().split()))
1 2 3
>>> a
1
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c=list(map(float,input().split()))
12.3 23.4 54
>>> a
12.3
>>> b
23.4
>>> c
54.0
>>> a,b,c=input().split()
a,b,c=input().split()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a,b,c=input().split()
ValueError: not enough values to unpack (expected 3, got 1)
>>> email,password=input().split()
sowmya@gmail.com 1234
>>> email
'sowmya@gmail.com'
>>> password
'1234'
>>> #eval function
>>> #eval function
>>> a=eval(input())
12
>>> a
12
>>> a=eval(input())
23.7
>>> a
23.7
>>> a=eval(input())
"sowmya"
>>> a
'sowmya'
>>> a=eval(input())
[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a=eval(input())
12+8j
>>> a
(12+8j)
>>> a=eval(input())
(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> a=eval(input())
{1,2,3}
>>> a
{1, 2, 3}
>>> a=eval(input())
{1:2,3:4,5:6}
>>> a
{1: 2, 3: 4, 5: 6}
>>> a=eval(input())
True
>>> a
True
>>> 