#!/usr/bin/env runhaskell

{-
Author: Pablo Baeyens (@mx-psi)
Usage: pandoc -F ./$0 yourfile.md -o yourfile.pdf
Description: Transforms divs into environments
Depends: pandoc-types
-}

import Text.Pandoc.JSON
import qualified Data.Map as Map

main :: IO ()
main = toJSONFilter envtify

raw = (: []) . RawBlock (Format "tex")
command name val = raw $ "\\" ++ name ++ "{" ++ val ++"}"
begin  name opts = raw $ "\\begin{" ++ name ++"}" ++ (maybe "" (\x -> "[" ++ x ++ "]") opts)
end              = command "end"
label ident      = if Prelude.null ident then [] else command "label" ident


envtify :: Block -> [Block]
envtify (Div (ident, [name], values) contents) =
  begin name opts ++ label ident ++ contents ++ end name
  where opts  = Map.lookup "name" (Map.fromList values)
envtify b = [b]
