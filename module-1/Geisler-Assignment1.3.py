## Cece Geisler
## CSD 325
## Assignment 1.3
## 12/04/2025

## START

## Asking the user how many bottles of beer are on the wall
bottles = int(input("How many bottles of beer are on the wall? "))

## For loop to print the song
def song():
    for i in range(bottles, 0, -1):
      if i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")

      elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")

      elif i == 2: ## special case for 2 bottles
         print("2 bottles of beer on the wall, 2 bottles of beer.")
         print("Take one down and pass it around, only 1 bottle of beer on the wall.")

      else:
         print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
         print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")

song()
## END