print("Welcome to General Quiz Game!!!")

gaming = input("Are you ready? ")

if gaming.lower() != "yes":
    print("Try next time!")
    quit()

print("Awesome! Let's begin")
score = 0

response = input("1. What is AI in full? ")
if response.lower() == "artificial intelligence":
    print("Passed")
    score += 1
else:
    print("Failed")


response = input("2. What is UI in full? ")
if response.lower() == "user interface":
    print("Passed")
    score += 1
else:
    print("Failed")


response = input("3. What is RAM in full? ")
if response.lower() == "random access memory":
    print("Passed")
    score =+ 1
else:
    print("Failed")


response = input("4. What is DBA in full? ")
if response.lower() == "database administrator":
    print("Passed")
    score += 1
else:
    print("Failed")


response = input("5. What is IT in full? ")
if response.lower() == "information technology":
    print("Passed")
    score += 1
else:
    print("Failed")

print("You have completed the quiz ")

result = (score/5)*100
print("Your score is " + str(score) + "/5 that is " + str(result) + "%")

quit()
