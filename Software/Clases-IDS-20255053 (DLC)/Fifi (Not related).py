judge = ""

while judge != "y":
    print("""Is fifi cute?
Yay or Nay""")
    judge = input()[0].lower()

    if judge == "y":
        print("Yea she cute")
    elif judge == "n":
        print("Fuck you")
    else:
        print("???")
        
fifi = {
    "size":"fat",
    "color":"negro",
    "disposition":"loud"
}