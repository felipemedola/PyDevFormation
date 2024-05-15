LIMITE_TWEET = 140

T = input("No que está pensando hoje?\nTweet: ")

quantidade_caracteres = len(T)

if quantidade_caracteres <= LIMITE_TWEET:
    print("Seu texto cabe perfeitamente em um tuíte!")
    print("* TWEET *")
else:
    print("Oops! Seu texto ultrapassou o limite de 140 caracteres.")
    print("* MUTAR *")