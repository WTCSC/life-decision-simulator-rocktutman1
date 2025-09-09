print ("Welcome to the decision tree!")

def real_answer_machine (first_choice, second_choice, user_choice):
    if user_choice == first_choice or user_choice == second_choice:
        return True
    else:
        return False
def main_function ():
    q1 = False
    q2 = False
    q3 = False
    q4 = False
    while q1 == False:
        first = input("What do you want to eat for breakfast?, SigmaSteak or Cereal? ")
        q1 = real_answer_machine ("SigmaSteak", "Cereal", first)
    if first == "SigmaSteak":
        while q2 == False:
            second = input("Do you want to drink SkibidiSoup with your breakfeast, YES or NO? ")
            q2 = real_answer_machine ("YES", "NO", second)
        if second == "YES":
            print ("After finishing breakfast you drink some still water and jamacian smile before you decide how to continue your morning")
            while q3 == False:
                third = input ("Do you want to go to your j*b and w*rk today, YES or NO? ")
                q3 = real_answer_machine ("YES", "NO", third)
            while q4 == False:
                fourth = input ("How long does it take you to drive to w*rk, 20 mins or 67 hours?")
                q4 = real_answer_machine ("20 mins", "67 hours", fourth)
        elif second == "NO":
            print ("You decided not to have SigmaSteak eithier")
            first = "Cereal"
            q2 = False
    if first == "Cereal":
        print ("You dont have any Diddyblud aura")
        while q2 == False:
            second = input("Go for a run to get aura back, YES or NO? ")
            q2 = real_answer_machine ("YES", "NO", second)
        if second == "NO":
            print("You decided not to go for a run so you just watch TV instead")
            third = input ("What do you do, watch Real Housewives of mangostein or Doomscroll? ")
            if third == "watch Real Housewives of Mangostein" or "Doomscroll":
                print ("You wasted your entire morning and are now late to school!!")
                while q4 == False:
                    fourth = input ("Do you still want to go to school, YES or NO? ")
                    q4 = real_answer_machine("YES", "NO", fourth)
                if (fourth == "YES"):
                    print ("You go to school and are bored all day")
                    print ("Finally getting home you go to bed, knowing that you'll have to try escpaing the matrix again tommrow")
                    main_function()
                elif (fourth == "NO"):
                    print ("Knowing that none of your teachers drive a rari you dont go to school so you can escape the matrix and dropship from ali-baba")
                    print ("A man walks up to you offering you a red pill or a blue pill")
                    input ("Which do you take, Red or Blue? ")
                    print ("It was fent")
            else:
                print(f"You are the first ever person to watch {third}, It's such a good show that you decide to write a review about it")
                print(f"Your review blows up and you make a ton of money!!!! Everyone is bewildered by how good {third} is!!!")
        elif second == "YES":
            print ("You get so much aura back that the ruzz (running huzz) asks if you want to help her make a newgen slang dictionary")
            while q3 == False:
                third = input("Do you, YES or NO? ")
                q3 = real_answer_machine ("YES", "NO", third)
            if third == "YES":
                brainrot_score = 0
                ##answers from https://genppt.com/blog/gen-alpha-slang
                print ("You prepare for the brainrot test, This will be hard, a 3/5 is required to pass ")
                bq1 = input ("What does Gyatt mean? ")
                if bq1 == "Refers to showing off or highlighting a large butt. Often used in a surprised or impressed tone.":
                    brainrot_score += 1
                bq2 = input ("What does fr mean? ")
                if bq2 == "For real; honestly, truthfully.":
                    brainrot_score += 1
                bq3 = input ("What does no cap mean? ")
                if bq3 == "No lie, for real, honestly.":
                    brainrot_score += 1
                bq4 = input ("What does put the fries in the bag mean? ")
                if bq4 == "An idiom meaning get to the point or do the job efficiently.":
                    brainrot_score += 1
                bq5 = input ("What does Get cooked mean? ")
                if bq5 == "To be thoroughly defeated, embarrassed, outdone, or insulted.":
                    brainrot_score += 1
                print (f"Your brainrot score is {brainrot_score} out of 5")
                if brainrot_score >= 3:
                    print ("Coungradulations, you are a true brainrot professor")
                else:
                    print ("minus infinity aura, you are never recovering from this aura debt")
            elif third == "NO":
                print ("You realize that your aura grinding is paying off and decide to tactically aura gambit and not accept the side quest")
                print ("To keep farming more aura you decide to double your mileage for the day")
                print ("While running through the woods near the halfway point of your run a bear comes out of the bushes")
                print ("Game recognizes Game, and Aura Farmer recognizes Aura Farmer, The bear sees you aura farming and decides that mauling you would give it aura which it desperately needs")
main_function()