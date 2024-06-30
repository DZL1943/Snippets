#!/bin/bash

folders=(asm c cpp rust go java scala kotlin python ruby lua shell erlang haskell lisp javascript css html)

for folder in "${folders[@]}"; do mkdir -p "$folder"; touch "$folder"/.gitkeep; done
