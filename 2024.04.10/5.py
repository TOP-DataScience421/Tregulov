
telegram_message = input("Введите текст телеграммы:")

message = telegram_message.replace(" ", "")
    
num_characters = len(message)  
#print(num_characters)

cost_per_character = 30  # в копейках
    
total_cost_kopecks = num_characters * cost_per_character 

rubles = total_cost_kopecks // 100  
kopecks = total_cost_kopecks % 100  

    
print(f"{rubles} руб. {kopecks} коп.")

# Введите текст телеграммы:грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.