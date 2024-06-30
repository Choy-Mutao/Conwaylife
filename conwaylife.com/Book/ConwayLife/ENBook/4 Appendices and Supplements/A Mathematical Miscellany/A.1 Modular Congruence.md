When we divide two integers by each other, we get a quotient(i.e., the interger result of division) and a remainder(i.e., a piece that is left over from the integer division). For example, dividing 7 by 3 gives the quotient  $q =\lfloor 7 / 3 \rfloor = 2$  with a remainder of $r = 1$. The number that we divide by (3 in this example) is called the modulus, and the remainder is always between 0 (inclusive) and the modulus (exclusive).

Modular congruence is a way of grouping numbers together based on their remainder upon division by a given modulus $n\ge2$ . For example, if the modulus is $n = 3$ then we say that 1, 4, 7,10 and so on are all congruent modulo 3, since they all have the same remainder (1) upon division by 3. Equivalently, we say that two integers a and b are congruent modulo n if a - b is an interger multiple of n, and in this case we write

$$
a \equiv b\mod n .
$$

For example, $7 \equiv 1 \mod 3$ since $7 - 1  = 6$ is a multiple of 3.

Congruence modulo n provides a way partitioning the set of integers into n disjoint sets, called congruence classes, each consisting of all integers that are congruent to each other. For example, if n = 2 then there are two congruence classes: the set of  even integers and the set of odd integers. If n = 3 then there are three congruence classes:
$$
\{\dots, -6, -3, 0, 3, 6, 9 \}, \{\dots, -5, -2, 1,4, 7,10 ,\dots\}, and \{\dots, -4,-1,2,5,8,11,\dots\}
$$

Since every integer a belongs to (exactly) one of the congruence classes, if we are given another member $b$ of that congruence class then we can find an integer $k$ so that $a = kn + b$

One of the most promient uses of modular congruence in the Game of Life arises when making timing and spacing adjustments in Life circuitry. For example, if we know of some way to delay a signal by 3 generations, then we can repeat that reaction n times in order to delay the signal by 3n generations. If we also know of methods of delaying the signal by, say, 5 and 7 generations, then we can delay it by any (sufficiently large) amount of our choosing: every mod-3 congruence class contains either $3,5, or 7$, so every integer can be written in the form $3n, 3n+5$, or $3n+7.$


A slightly more realistic scenario that occurs in the Game of Life makes use of mod-8 arithmetic. It is often easy to delay a glider by any multiple of 8 generations, so to be able to implement arbitrary delays we "just" need to find ways of delaying it by amounts that cover the other 7 congruence classes. We collect glider-delaying reactions like this in two different places in the main text: Tables 5.5 and 7.2


