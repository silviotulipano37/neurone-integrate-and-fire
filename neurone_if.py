import random

soglia = 10
potenziale = 0

for i in range(20):
    stimolo = random.randint(0, 5)
    potenziale += stimolo
    print(f"Stimolo {i+1}: {stimolo}, Potenziale: {potenziale}")
    if potenziale >= soglia:
        print("🎯 Il neurone spara!")
        potenziale = 0
        
