# Interview-Prep #

**Problem 1 :**  Product of array except itself 

>Solutions <br>

`Algorithm-1 using division O(2n)`
`Alogrithm-2 using extraspace O(3n)`
`Algorithm-3 without extraspace O(2n)`

**Problem 2 :** First non repeating character

>Solutions<br>

`Algorithm-1 using Brute Force O(n2)`
`Algorithm-2 using hashmap O(2n)`

**Problem 3 :** Maximum Sum Sub-array (Kadanne's algo)
>Solutions<br>

`Algorithm-1 using Brute Force O(n2)`
`Algorithm-2 Kadanne's Algorithm O(n)`

**Problem 4 :** Valid Anagram 
>Solution<br>

`Algorithm-1 O(n)`

**Problem 5 :** Valid Paranthesis ( ( ), { }, [ ] )<br>

>**Stack**<br>
_Table for information regarding stack_

|Method|Description|
|---|---| 
|empty() | Returns whether the stack is empty – **Time Complexity : O(1)**|
|size() | Returns the size of the stack – **Time Complexity : O(1)**|
|top() | Returns a reference to the top most element of the stack – **Time Complexity : O(1)**|
|push(g) | Adds the element ‘g’ at the top of the stack – **Time Complexity : O(1)**|
|pop() | Deletes the top most element of the stack – **Time Complexity : O(1)**|
<br>

>Solution<br>

`Algorithm-1 using stack/list`

**Problem 6 :** Sum of Two <br>

_returns true if sum of one from array a and one from array b is equals to the given value v else returns false_

>Solutions<br>

`Algorithm-1 using brute force O(n2)`
`Algorithm-2 using datastructure (set) O(2n)`

**Problem 7 :** Sorted square array<br>

_To return sorted square array of the given input. Input may contain negative numbers and is sorted initially._

>Solutions<br>

`Algorithm-1 using sort method O(nlogn)`
`Algorithm-2 using two pointers O(n)`

**Problem 8 :** First Duplicate<br>

_To return the value of the first duplicate in the given array._

>Solutions<br>

`Algorithm-1 using brute force O(n2)`
`Algorithm-2 using set O(n)`
`Algorithm-3 without set O(n)`


**Problem 9 :** Valid Sudoku<br>

_To return true if the given sudoku is valid else false. Given Input is 2d arrays of 9x9 squares with blank represented as "." _

`Example : [
    ['7','5','.','.','.','.','4','.','9'],
    ['1','2','.','.','.','.','4','.','9'],
    ['3','.','.','.','.','.','4','.','9'],
    ['6','4','.','.','.','.','4','.','9'],
    ['2','.','.','.','.','.','4','.','9'],
    ['.','8','.','.','.','.','4','.','9'],
    ['.','1','.','.','.','.','4','.','9'],
    ['4','5','.','.','.','.','4','.','9'],
    ['.','5','.','.','.','.','4','.','9'],
]`

>Solution<br>

`Algorithm-1 using set O(1) as given input 9x9.`

**Problem 10 :** Longest Palindromic substring<br>

_To return Longest palindrome substring from given string. eg- baabad -> aba_

>Solution<br>

`Algorithm-1 O(n2)`

**Problem 11 :** Count of subarray sum equals to k<br>

_To return the number of times the sum is equal to k in the given array_

>Solution<br>

`Algorithm-1 using dictionary(hashmap)`

**Problem 12 :** Find all the duplicates in the given array<br>

_We make negative the arr[abs(arr[value])-1] so that if the duplicate occurs in array then we can traverse the duplicate one as it have different sign_.

>Solution<br>

`Algorithm-1 without using extraspace and have time complexityO(n)`

**Problem 13 :** Task Scheduler (Leet Code 621 refer for more info)<br>

_Example : ['A','A','A','B','B','B']<br>
'A' and 'B' are given two task and n(cooling period) = 2.<br>
Output - 8 (A->B -> idle -> A->B -> idle -> A->B)_<br>

>Solution<br>

`Algorithm-1 O(2n)`

**Problem 14 :** Longest Continuous Subsequence (Sliding window approach)<br>

_Example : Input : [1,3,5,4,7] will return 3 output. 4 length is not valid answer as it is seperated by 4 in the given input._

>Solution<br>

`Algorithm-1 O(n) using sliding window approach`

**Problem 15 :** Longest word in dictionary <br>
_This problem needs revision_
>Solution<br>

`Algorithm 1 using set O(n)`

**Problem 16 :** Minimum size subarray sum<br>
_This Problem needs revision_
>Solution<br>

`Algorithm 1 O(nlogn)`

**Problem 17 :** Valid Perfect Square<br>
_To return true for valid pefect square input and false for not a valid pefect square number. Also don't use sqrt() method._

>Solution <br>

`Algorithm-1 O(logn) using binary search and n is the input`
`Algorithm-2 O(logn) using Newton's method`

**Problem 18 :** Convert Roman Number to Integer

>SOlution <br>

`Algorithm-1 O(n)`