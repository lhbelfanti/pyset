Compiler to handle my own set theory languaje.<br/>

Languaje: Languaje Oriented to Set Theory of <b>Integer Numbers</b>.<br/>

Languaje definitions:<br/>

- Variables: 
	- Definition: 'var a' 		(only lowercase)
	- Assignation: 'var a = 4'	(assign 4 to a)

- Operations:
	- Set()
		- Set({1,2,3,4})		(<b>Returns</b> a Set with 4 elements)
		- Set([1,10])			(<b>Returns</b> a Set with 10 elements, from 1 to 10)
	- Print()
		- Print(a) 				(Print the value of a)
		- Print(s) 				(Print the set s)
		- Print('hi') 			(Print the string 'hi'. String concatenations are not allowed)
	- Int()
		- Int(a,b)				(<b>Returns</b> the intersection between a and b)
	- Uni()
		- Uni(a,b)				(<b>Returns</b> the union between a and b)
	- Len()
		- Len(a)					(<b>Returns</b> the quantity of elements of a)
	- Med()
		- Med(a)				(<b>Returns</b> the average of all the elements of a)
	- Max()
		- Max(a)				(<b>Returns</b> the maximun element of a)
	- Min()
		- Min(a)				(<b>Returns</b> the the minimun element of a)
	- Ext()
		- Ext(a,b)				(Extract all the elements of a from b, and <b>returns</b> it)	
	- Push()
		- Push(a,5)				(Add the element 5 to a)

- Conditional:<br/>
	If condition Then<br/>
		...<br/>
	Endif<br/>

- Loop:<br/>
	For e In a Do<br/>
		...<br/>
	Endfor<br/>
