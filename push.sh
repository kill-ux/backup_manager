#!/bin/bash

echo "
push() {
git add .
git commit -m "\$1" 
git push 
git push github main
}" >> ~/.zshrc