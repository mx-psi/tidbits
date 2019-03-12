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

You need [`pandoc`](http://pandoc.org/installing.html) 2 or greater, and [stack](https://docs.haskellstack.org).
You can use it then just like any other filter:

``` shell
pandoc -F ./env.hs example.md -o example.pdf
```

## Troubleshooting

**It is taking too long to run**
: The first time you run the script `stack` will download and install Haskell's compiler (~1.5GB) and the necessary dependencies, which might take a while. Subsequent runs should be almost instantaneous.
If you don't like this setup, replace `stack` by `runghc` on the first line of the script.


