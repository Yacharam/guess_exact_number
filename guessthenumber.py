exact_number=10
attempts=0
while True:
    attempts+=1
    guess=int(input("guess the number:"))
    if guess<exact_number:
        print("guess is too low")
    elif guess>exact_number:
        print("guess is too high")
    else:
        print(f"you guessed the exact number in {attempts} attempts")
        break
print("thanks for playing")
    
        
    