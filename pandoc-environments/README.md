# Pandoc LaTeX environment filter

A minimal pandoc filter for transforming divs into LaTeX environments.

It turns this:

``` markdown
:::{.theorem #thm:euclid name="Euclid's theorem"}
There are infinitely many prime numbers.
:::
```

into this:

``` latex
\begin{theorem}[Euclid's theorem]
\label{thm:euclid}
There are infinitely many prime numbers.
\end{theorem}
```

## Usage

You need [`pandoc`](http://pandoc.org/installing.html) 2 or greater, [Haskell](https://www.haskell.org/) and [pandoc-types](https://hackage.haskell.org/package/pandoc-types).
You can use it then just like any other filter:

``` shell
pandoc -F ./env.hs example.md -o example.pdf
```



