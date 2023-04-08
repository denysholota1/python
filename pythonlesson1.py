
with open("users.txt", "a") as file:
    while True:
        
        name = input("Введіть ім'я користувача (або 'q' для виходу): ")
        if name == 'q':
           
            break
        else:
            
            file.write(name + '\n')
            print("Ім'я користувача додано до файлу.")

print("Програма завершила роботу.")