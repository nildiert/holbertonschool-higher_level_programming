# Javascript
![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png)

----
## What is Javascript?
see [Wikipedia](https://en.wikipedia.org/wiki/JavaScript)

> Not to be confused with Java (programming language), Java (software platform), JScript, or Javanese script.
For the uses of JavaScript on Wikipedia, see Wikipedia:Javascript.".

----
## JavaScript - Syntax

JavaScript can be implemented using JavaScript statements that are placed within the **<script>... </script>** HTML tags in a web page.

You can place the **<script>** tags, containing your JavaScript, anywhere within your web page, but it is normally recommended that you should keep it within the **<head>** tags.

The <script> tag alerts the browser program to start interpreting all the text between these tags as a script. A simple syntax of your JavaScript will appear as follows.


```javascript
<script ...>
   JavaScript code
</script>

```

The script tag takes two important attributes −

* **Languaje**  − This attribute specifies what scripting language you are using. Typically, its value will be javascript. Although recent versions of HTML (and XHTML, its successor) have phased out the use of this attribute.
* **Type** − This attribute is what is now recommended to indicate the scripting language in use and its value should be set to "text/javascript".

So your JavaScript segment will look like −

```javascript
<script language = "javascript" type = "text/javascript">
   JavaScript code
</script>
```

## First JavaScript Code
```html
<html>
   <body>   
      <script language = "javascript" type = "text/javascript">
         <!--
            document.write("Hello World!")
         //-->
      </script>      
   </body>
</html>
```
This code will produce the following result 
```
Hello World!
```
## Semicolons are Optional
Simple statements in JavaScript are generally followed by a semicolon character, just as they are in C, C++, and Java. JavaScript, however, allows you to omit this semicolon if each of your statements are placed on a separate line. For example, the following code could be written without semicolons.

```javascript
<script language = "javascript" type = "text/javascript">
   <!--
      var1 = 10
      var2 = 20
   //-->
</script>
```

But when formatted in a single line as follows, you must use semicolons −

```javascript
<script language = "javascript" type = "text/javascript">
   <!--
      var1 = 10; var2 = 20;
   //-->
</script>

```

## Comments in JavaScript

The following example shows how to use comments in JavaScript

```javascript
<script language = "javascript" type = "text/javascript">
   <!--
      // This is a comment. It is similar to comments in C++
   
      /*
      * This is a multi-line comment in JavaScript
      * It is very similar to comments in C Programming
      */
   //-->
</script>

```

## JavaScript - Variables
### JavaScript Datatypes
One of the most fundamental characteristics of a programming language is the set of data types it supports. These are the type of values that can be represented and manipulated in a programming language.

JavaScript allows you to work with three primitive data types −

* **Numbers** eg. 123, 120.50 etc.
* **Strings** of text e.g. "This text string" etc.
* **Boolean** e.g. true or false.

JavaScript also defines two trivial data types, **null** and **undefined**, each of which defines only a single value. In addition to these primitive data types, JavaScript supports a composite data type known as object. We will cover objects in detail in a separate chapter.

### JavaScript Variables

Before you use a variable in a JavaScript program, you must declare it. Variables are declared with the var keyword as follows.

```javascript
<script type = "text/javascript">
   <!--
      var money;
      var name;
   //-->
</script>

```

You can also declare multiple variables with the same var keyword as follows −


```javascript
<script type = "text/javascript">
   <!--
      var money, name;
   //-->
</script>

```

### JavaScript Variable Scope

The scope of a variable is the region of your program in which it is defined. JavaScript variables have only two scopes.

* **Global Variables** − A global variable has global scope which means it can be defined anywhere in your JavaScript code.

* **Local Variables** − A local variable will be visible only within a function where it is defined. Function parameters are always local to that function.


### JavaScript Variable Names

While naming your variables in JavaScript, keep the following rules in mind.

* You should not use any of the JavaScript reserved keywords as a variable name. These keywords are mentioned in the next section. For example, **break** or **boolean** variable names are not valid.
* JavaScript variable names should not start with a numeral (0-9). They must begin with a letter or an underscore character. For example, **123test** is an invalid variable name but **_123test** is a valid one.

* JavaScript variable names are case-sensitive. For example, **Name** and **name** are two different variables.


## JavaScript - Operators
### Arithmetic Operators

* **+ (Addition)** Adds two operands
* **- (Subtraction)** Subtracts the second operand from the first
* *** (Multiplication)** Multiply both operands

* **/ (Division)** Divide the numerator by the denominator
 	
* **% (Modulus)** Outputs the remainder of an integer division
* **++ (Increment)**Increases an integer value by one
* **-- (Decrement)** Decreases an integer value by one

### Comparison Operators
* **= = (Equal)** Checks if the value of two operands are equal or not, if yes, then the condition becomes true.
* **!= (Not Equal)** Checks if the value of two operands are equal or not, if the values are not equal, then the condition becomes true.
* **> (Greater than)** Checks if the value of the left operand is greater than the value of the right operand, if yes, then the condition becomes true.
* **< (Less than)** Checks if the value of the left operand is less than the value of the right operand, if yes, then the condition becomes true.
* **>= (Greater than or Equal to)** Checks if the value of the left operand is greater than or equal to the value of the right operand, if yes, then the condition becomes true.
* **<= (Less than or Equal to)** Checks if the value of the left operand is greater than or equal to the value of the right operand, if yes, then the condition becomes true.

### Logical Operators
* **&& (Logical AND)** If both the operands are non-zero, then the condition becomes true.
* **|| (Logical OR)** If any of the two operands are non-zero, then the condition becomes true.
* **! (Logical NOT)**Reverses the logical state of its operand. If a condition is true, then the Logical NOT operator will make it false.
 	

## JavaScript - if...else Statement
### if statement
```
if (expression) {
   Statement(s) to be executed if expression is true
}
```
### if...else statement
```
if (expression) {
   Statement(s) to be executed if expression is true
} else {
   Statement(s) to be executed if expression is false
}
```
### if...else if... statement
```
if (expression 1) {
   Statement(s) to be executed if expression 1 is true
} else if (expression 2) {
   Statement(s) to be executed if expression 2 is true
} else if (expression 3) {
   Statement(s) to be executed if expression 3 is true
} else {
   Statement(s) to be executed if no expression is true
}
```
## JavaScript - Switch Case
```
switch (expression) {
   case condition 1: statement(s)
   break;
   
   case condition 2: statement(s)
   break;
   ...
   
   case condition n: statement(s)
   break;
   
   default: statement(s)
}
```

## JavaScript - While Loops
### The while Loop
```
while (expression) {
   Statement(s) to be executed if expression is true
}
```
### The do...while Loop
```
do {
   Statement(s) to be executed;
} while (expression)
```
### JavaScript - For Loop
```
for (initialization; test condition; iteration statement) {
   Statement(s) to be executed if test condition is true
}
```

### JavaScript for...in loop
```
for (variablename in object) {
   statement or block to execute
}
```
## JavaScript - Functions

### Function Definition
}
```
<script type = "text/javascript">
   <!--
      function functionname(parameter-list) {
         statements
      }
   //-->
</script>
}
```

1. Write markdown text in this textarea.
2. Click 'HTML Preview' button.

----
## Authors
* Nildiert Jimenez

----
## Changelog
* 17-Sep-2019 

----
## Thanks
* [Tutorialspoint](https://www.tutorialspoint.com/javascript/javascript_quick_guide.htm
)

* [markdown-js](https://github.com/evilstreak/markdown-js)

