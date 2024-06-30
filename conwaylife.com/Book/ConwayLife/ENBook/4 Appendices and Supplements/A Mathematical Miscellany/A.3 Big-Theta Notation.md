When describing the long-term behavior of a Life pattern, we often just want to focus on the "big picture", while suppressing the "fine details". For example, the pattern displayed in Figure A.1 grows extremely quickly, filling the entire Life plane with zebra stripes as its four corners expand outward. Patterns that fill the plane like this are called spacefillers, and this one is called max.

To communicate how quickly this pattern grows, we could of course give an explicit formula for its population $p(t)$ in generation t, which has the following form:

$$
\begin{equation} 
p(t) = \frac{t^2}{4} + 
\begin{cases} 
21t/2 + 209, & \text{if } t \equiv 0 \pmod{4} 
\\ 21t/2 + 215, & \text{if } t \equiv 2 \pmod{4} 
\\ 10t + 923/4, & \text{otherwise}.
\end{cases} \end{equation}
$$
However, this formula is quite technical and has many details that we typically do not actually care about. Its "most important" piece is the $t^2/4$ term at the front --- in the long run(i.e., when t is large), that term has the biggest effect on the population. For this reason, we would typically just say that $p(t)$ "grows like $t^2/4$", or even that $p(t)$ "is proportional to $t^2$". Bit-$\Theta$ notation provides a way of making this terminology precise:

> Definition A.1 --- Bit - $\Theta$ Notation
> Suppose f and g area real-valued functions. We say "f(x) is $\Theta(g(x))$" if there exist positive scalars c, C, and N such that
> $cg(x) \le f(x) \le Cg(x) whenever X\ge N$.

Informally, the phrase "f(x) is $\Theta((g(x)))$"