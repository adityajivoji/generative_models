==========
Question 1
==========

VNIT has organized an inter-club competition wherein it has locked the workspaces of all the clubs with a smart lock. Whichever club unlocks the lock in the least time, wins the competition.

The smart lock can be opened only using a password which is the number of possible strings of a given length n, formed using lowercase alphabets (a-z). It is further given that the strings should be palindromes and shouldn't contain consecutive vowels.

ACM Club needs your help to find the password in the least time.

Since the answer might be too large, return it modulo (109 + 7).

Note:

A string is a Palindrome if it reads the same as its reverse. Ex: "aaa", "abcba", "hiih".
Input Format

Single line which contains the length of strings n.

Constraints

1 ≤ n ≤ 105

Output Format

Single line containing the password (modulo (109 + 7)).

Sample Input 0

1
Sample Output 0

26
Explanation 0

The length of the string is 1. Possible strings are: "a", "b",...,"z".

Sample Input 1

2
Sample Output 1

21
Explanation 1

The length of the string is 2. Possible strings of length 2, which are palindromes are: "aa", "bb",...,"zz".

Since, no two consecutive alphabets can be vowels The strings "aa", "ee", "ii", "oo", "uu" are excluded.


=========
Question 2
=========


VNIT has organized an inter-club competition wherein it has locked the workspaces of all the clubs with a smart lock. Whichever club unlocks the lock in the least time, wins the competition.

The smart lock can be opened only using a password which is the number of possible strings of a given length n, formed using lowercase alphabets (a-z). It is further given that the strings should be palindromes and shouldn't contain consecutive vowels.

ACM Club needs your help to find the password in the least time.

Since the answer might be too large, return it modulo (109 + 7).

Note:

A string is a Palindrome if it reads the same as its reverse. Ex: "aaa", "abcba", "hiih".
Input Format

Single line which contains the length of strings n.

Constraints

1 ≤ n ≤ 105

Output Format

Single line containing the password (modulo (109 + 7)).

Sample Input 0

1
Sample Output 0

26
Explanation 0

The length of the string is 1. Possible strings are: "a", "b",...,"z".

Sample Input 1

2
Sample Output 1

21
Explanation 1

The length of the string is 2. Possible strings of length 2, which are palindromes are: "aa", "bb",...,"zz".

Since, no two consecutive alphabets can be vowels The strings "aa", "ee", "ii", "oo", "uu" are excluded.


========
Question 3
========

Charlie wants to work at the chocolate factory. To get a job there, he wrote a mail to Willy Wonka, but the email got corrupted because of a bug created by the Oompa Loompas. Charlie is devastated by hearing this news.

The bug has done a series of the following operations in any order:

It randomly converted some lowercase letters to uppercase letters.
It randomly inserted some digits, special characters.
It also appended extra spaces at the start and end of the mail. (possibly 0)
Help Charlie to get the job by doing the following:

Convert all the letters to lowercase.
Remove all digits, special characters except '.' and ','
Remove all extra leading and trailing spaces.
Note:

The test cases follow all the above conditions and the email contains a single paragraph with no new lines.
Input Format

First line contains s, a string which contains the corrupted email.

Constraints

1 ≤ s.length ≤ 103

Output Format

A string containing the original email.

Sample Input 0

   Hi, I aM CHarlie. I* am frOm3490 Wonkaville99.   
Sample Output 0

hi, i am charlie. i am from wonkaville.
Explanation 0

Note that the input string has leading and trailing spaces


============
Question 4
============


Assume you work for a business called (Pine)Apple, which makes computer chips. Your goal is to create a software that can name as many chips as the regulations allow.

Your input will consist of a string of n digits.

A perfect chip number is made up of four integers separated by a single dash. Each integer has a range of 0 to 512 (inclusive) with no leading zeros.

"0-1-2-201" and "192-168-1-1" for example, are legal, while "0-011-255-245" , "192-168-1-612", and "192-168@1-1" are not.

All potential optimal chip numbers will be output.

NOTE : the output should have each string on a new line and they must be in sorted order.

Input Format

String s containing digits

Constraints

1 ≤ n ≤ 20

String consists of digits only.

Output Format

List of all possible strings.

Sample Input 0

0000
Sample Output 0

0-0-0-0
Sample Input 1

101023
Sample Output 1

1-0-10-23
1-0-102-3
10-1-0-23
10-10-2-3
101-0-2-3

==========
Question 5
==========

Binod gives a number N to Xavier and challenges him to find a smallest positive integer X such that X should satisfy the following conditions :

X should have more than 3 divisors.
The difference between any two of the divisors of X should be greater than or equal to N.
Help Xavier find the smallest positive integer X such that it satisfies the above conditions.

Input Format

Input contains a single number N.

Constraints

1 ≤ N ≤ 105

Output Format

Print the smallest positive integer X such that it satisfies the above conditions.

Sample Input 0

2
Sample Output 0

15
Explanation 0

Integer 15 have following divisors: [1,3,5,15]. There are 4 of them and the difference between any two of them is at least 2.

Sample Input 1

3
Sample Output 1

55