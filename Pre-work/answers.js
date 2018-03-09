//Page 16////////////////////////////////////////////////

// Setting and Swapping
//Set myNumber to 42. Set myName to your name.Now swap myNumber into myName & vice versa.

var myNumber = 42

var myName = “Victor De Vera”

myNumber = myName

myName = myNumber

//Print -52 - 1066
//Print integers from -52 to 1066 using a FOR loop.

for( var i=-52; i<1067; i++)
{
console.log(i);
}

//Don’t Worry, Be Happy
//Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

beCheerful()
{
for( var i = 1; i <99; i++) 
	{
		console.log(“good morning!”)
	}
}

//Multiples of Three – but Not All
//Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for( var i = -300; i<1; i = i+3)
{
if( i == -3 || i == -6)
	{
		Continue;
	}
	console.log(i);
}

//Printing Integers with While
//Print integers from 2000 to 5280, using a WHILE.

var num= 2000;

while( num < 5281)
{
	console.log(num);
	num += 1;
}

//You Say It’s Your Birthday
//If 2 given numbers represent your birth month and day in either order, log "How did you know?", 
//else log "Just another day...."

if( month == 4 && day == 24)
{
	console.log(“How did you know?”)
}
else;
{
	console.log(“Just another day….”)
}

// Leap Year
//Write a function that determines whether a given year is a leap year. If a year is divisible by four,
// it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.

function leapYear()
{
	if( year % 4 == 0);
	{
		if( year % 100 == 0)
		{
			console.log(“not leap year”);
		}
		else
		{
			console.log(“leap year”);
		}
	}
	else  if ( year % 400 == 0)
	{
		console.log(“leap year”)
	}
	else 
	{	
		console.log(“not leap year”)
	}
}

//Print and Count
//Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

var sum = 0;

for( var i=512; i<4097; i = i+5)
{
	console.log(i);
	sum = sum + 1
}

console.log(sum)

//Multiples of Six
//Print multiples of 6 up to 60,000, using a WHILE.

var num = 6;

while( num<60,001)
{
	console.log(num);
	num = num + 6
}

//Counting, the Dojo Way
//Print integers 1 to 100. If divisible by 5, print
//"Coding" instead. If by 10, also print " Dojo".

for( var i=1; i<101; i++)
{
	if( i % 5 ==0)
	{
		console.log("Coding")
		continue;
	}
	else if( i % 10 ==0)
	{
		console.log("Dojo")
		continue;
	}
	console.log(i)
}

//What Do You Know?
//Your function will be given an input parameter
//incoming. Please console.log this value.

function whatDoYouKnow (parameter)
{
	if( parameter == "incoming")
	{
		console.log("incoming")
	}

}

//Whoa, That Sucker’s Huge…
//Add odd integers from -300,000 to 300,000, and
//console.log the final sum. Is there a shortcut?

var sum = 0;

for( var i = -300001; i< 300001; i = i+2)
{
	sum = sum + i;
}
return sum;

//Countdown by Fours
//Log positive numbers starting at 2016, counting
//down by fours (exclude 0), without a FOR loop.

var num = 2016;

while( num >= 8)
{
	console.log(num);
	num = num - 4;
}

//Flexible Countdown
//Based on earlier “Countdown by Fours”, given
//lowNum, highNum, mult, print multiples of mult
//from highNum down to lowNum, using a FOR.
//For (2,9,3), print 9 6 3 (on successive lines).

var arr = [4,2016,4];

for( var i=2016, i>=4, i = i-4)
{
	console.log(i)
}



//The Final Countdown
//This is based on "Flexible Countdown". The parameter names are not as helpful,
//but the problem is essentially identical; don't be thrown off! Given 4 parameters 
//(param1, param2, param3, param4) print the multiples of param1,
//starting at param2 and exteding to param3. One expectation: if a multiple is equal
//to param4, then skip ( don't print) it. Do this using a WHILE. Given (3,5,17,9) ,
//print 6, 12, 15 (which are all of the multiples of 3 between 5 and 17, and exculding the value 9).

var arr = [param1,param2,param3,param4];

var num = param3

while( param2 < param3)
{
	if( param3 % param1 == 0 && param3 != param4)
	{
		console.log(param3);
		param3 = param3 - param1; 
	}
	else
	{
		param3 = param3 - 1;
		if( param3 % param1 ==0 $$ param3 != param4)
		{
			console.log(param3);
			param3 = param3 - param1; 
		}
	}
}

//Page 20///////////////////////////////////////////////////////

//Countdown
//Create a function that accepts a number as an input. Return a new array that counts down by one, from
//the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array? 

function countDown (num)
{
	var newArr = [];
	for( var i = num; i >=0; i--)
	{
		newArr.push(i)
	}
	return newArr;
}
//the length of the arry would be the value of num 

//Print and Return
//Your function will receive an array with two numbers. Print the first value, and return the second. 

function printAndReturn(arr)
{
	print(arr[0]);
	return(arr[1]);
}

//First Plus Length
//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if
//the array’s first value is not a number, but a string (like "what?") or a boolean (like false). 

var sum = arr[0] + arr.length 
//what?(arr.length), arr.length 

//Values Greater than Second
//For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is. 

var arr = [1,3,5,7,9,13];

var sum = 0;

for( var i = 0; i < arr.length; i++)
{
	if( arr[i] > arr[1])
	{
		console.log(arr[i]);
		sum = sum + 1;
	}
}

return sum; 

//Values Greater than Second, Generalized
//Write a function that accepts any array, and returns a new array with the array values that are greater
//than its 2nd value. Print how many values this is. What will you do if the array is only one element long? 

var newArr = [];

var sum = 0;

function anyArr(arr)
{
	for( var i = 0; i < arr.length; i++)
	{
		if( arr[i] > arr[1])
		{
			newarr.push(arr[i]);
			sum = sum + 1;
		}
	}
}

return newArr;

return sum;

//This Length, That Value
//Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

var num1 = arr.length 

for( var i = 0; i < arr.length; i++)
{
	var num2 = arr[i];
	if( num1 = num2)
	{
		console.log("Jinx!");
	}
}

//Fit the First Value
//Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!";
//if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!". 

function fitTheFirstArr(arr)
{
	if( arr[0] > arr.length)
	{
		console.log("Too big!");
	}
	if( arr[0] < arr.length)
	{
		console.log("Too small!")
	}
	if( arr[0] == arr.length)
	{
		console.log("Just right!")
	}
}

//Fahrenheit to Celsius
//Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees)
//that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed
//in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

function farhrenheitToCelsius(fDegrees)
{
	fDegrees = fDegrees - 32;
	fDegrees = fDegrees * 1.8;
	return fDegrees;
}

//Celsius to Fahrenheit
//Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns
//the equivalent temperature expressed in Fahrenheit degrees.

function celsiusToFahrenheit(cDegrees)
{
	cDegrees = cDegrees * 1.8;
	cDegrees += 32;
	return cDegrees;
}

//Page 22////////////////////////////////////////////

//Biggie Size
//Given an array, write a function that changes all
//positive numbers in the array to “big”. Example:
//makeItBig([-1,3,5,-5]) returns that same
//array, changed to [-1,"big","big",-5].  

function biggieSize(arr)
{
	for( var i = 0; i < arr.length; i++)
	{
		if( arr[i] > 0)
		{
			arr[i] = "big";
		}
	}
}

//Print Low, Return High
//Create a function that takes array of numbers.
//The function should print the lowest value in the
//array, and return the highest value in the array.

function printLowReturnHigh(arr)
{
	var low = arr[0];

	for( var i = 1; i < arr.length; i ++)
	{
		if( arr[i] < low)
		{
			low = arr[i];
		}
	}

	var high = arr[0];

	for( var p = 1; p < arr.length; p ++)
	{
		if( arr[p] > high)
		{
			high = arr[p];
		}
	}

	console.log(low); 
	return high;
}

//Print One, Return Another
//Build a function that takes array of numbers. The
//function should print second-to-last value in the
//array, and return first odd value in the array.

function printOneReturnAnother(arr)
{
	console.log(arr[arr.length-2]);

	var fOdd = 0

	for( var i = 0; i < arr.length; i++)
	{
		if( arr[i] % 2 = 1)
		{
			fOdd = arr[i];
			return fOdd;
			break;
		}
	}
}

//Double Vision
//Given array, create a function to return a new
//array where each value in the original has been
//doubled. Calling double([1,2,3]) should
//return [2,4,6] without changing original.

function doubleVision(arr)
{
	var newArr = [];

	for( var i = 0; i < arr.length; i++)
	{
		arr[i] = arr[i] * 2;
		newArr.push(arr[i]);
	}

	return newArr; 
}

//Count Positives
//Given array of numbers, create function to
//replace last value with number of positive values.
//Example, countPositives([-1,1,1,1])
//changes array to [-1,1,1,3] and returns it.

function countPositives(arr)
{
	var pos = 0;

	for( var i = 0; i < arr.length; i++)
	{
		if( arr[i] > 0)
		{
			pos += 1;
		}
	}

	arr[arr.length - 1] = pos;

	return arr;
}

//Evens and Odds
//Create a function that accepts an array. Every
//time that array has three odd values in a row,
//print "That’s odd!" Every time the array has
//three evens in a row, print "Even more so!"

function evensAndOdds(arr)
{
	for( var i = 0; i < arr.length; i++)
	{
		if( arr[i] % 2 = 1)
		{
			if( arr[i + 1] % 2 = 1)
			{
				if( arr[i + 2] % 2 = 1)
				{
					console.log("That’s odd!");
				}
			}
		}
	}
	for ( var o = 0; o < arr.length; o++)
	{
		if( arr[o] % 2 = 0)
		{
			if( arr[o + 1] % 2 = 0)
			{
				if( arr[o + 2] % 2 = 0)
				{
					console.log("Even more so!");
				}
			}
		}	
	}
}

//Increment the Seconds
//Given arr, add 1 to odd elements ([1], [3],
//etc.), console.log all values and return arr.

function incrementTheSeconds(arr)
{
	for( var i =0; i<arr.length; i++)
	{
		if( arr[i] % 2 = 1)
		{
			arr[i] += 1;
			console.log(arr[i]);
		}
	}
	return arr; 
}

//Previous Lengths
//You are passed an array containing strings.
//Working within that same array, replace each
//string with a number – the length of the string at
//previous array index – and return the array.


function previousLengths(arr)
{
	for( var i =0; i<arr.length; i++)
	{
		arr[i] = arr[i].length;
	}
	return arr;
}

//Add Seven to Most
//Build function that accepts array. Return a new
//array with all values except first, adding 7 to
//each. Do not alter the original array.

function addSevenToMost(arr)
{
	var newArr= [];

	for( var i =1; 1<arr.length; i++)
	{
		arr[i] += 7;
		newArr.push(arr[i]);
		arr[i] -= 7;
	}

	return newArr;
}

//Reverse Array
//Given array, write a function to reverse values,
//in-place. Example: reverse([3,1,6,4,2])
//returns same array, containing [2,4,6,1,3]. 

function reverseArray(arr)
{
	var newArr = [];

	for( var i = arr.length-1; i>=0; i--)
	{
		newArr.push(arr[i]);
	}
	arr = newArr

	return arr; 
}

//Outlook: Negative
//Given an array, create and return a new one
//containing all the values of the provided array,
//made negative (not simply multiplied by -1).
//Given [1,-3,5], return [-1,-3,-5]. 

function outlookNegative(arr)
{
	for( var i=0; i<arr.length; i++)
	{
		if( arr[i] >0)
		{
			arr[i]= arr[i]*(-1)
		}
	}

	return arr;
}

//Always Hungry
//Create a function that accepts an array, and
//prints "yummy" each time one of the values is
//equal to "food". If no array elements are
//"food", then print "I'm hungry" once. 

function alwaysHungry(arr)
{
	var meal = 0;

	for( var i=0; i<arr.length; i++)
	{
		if( arr[i] != "food")
		{
			continue
		}
		else if( arr[i] = "food")
		{
			meal += 1
			console.log("yummy");
		}
	}

	if( meal = 0)
	{
		console.log("I'm hungry");
	}
}

//Swap Toward the Center
//Given array, swap first and last, third and third-tolast,
//etc. Input[true,42,"Ada",2,"pizza"]
//becomes ["pizza",42,"Ada",2,true].
//Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

function swapTowardTheCenter(arr)
{
	var temp1 = arr[0];
	arr[0] = arr[arr.length-1];
	arr[arr.length-1] = temp1;
	var temp2 = arr[2];
	arr[2] = arr[arr.length-3];
	arr[arr.length-3] = temp2;

	return arr;
}

//Scale the Array
//Given array arr and number num, multiply each arr value by num,
//return the changed arr

function scaeTheArray(arr)
{
	for( var i=0; i<arr.length; i++)
	{
		arr[i] *= num;
	}
	return arr;
}














































