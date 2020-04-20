import string

letters_to_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,
'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
numbers_to_letters = dict([[v, k] for k,v in letters_to_num.items() ])
def frequency_table(cipher_text):
    """[it outputs a frequency table of how many times every letter has occurd]

    Arguments:
        cipher_text {[string]} -- [The encrypted text]
    """ 
    m = list(cipher_text)
    frequency_table = []
    for letter in string.ascii_uppercase: 
        frequency_table.append([letter, m.count(letter)])
    table = dict(frequency_table)
    frequency_table =sorted (table.items(), key= lambda kv:[kv[1], kv[0]])
    frequency_table.reverse()
    return frequency_table

         

def Vigenere_Key(key_word):
    """pass a word and gives you a list_key
    
    Arguments:
        key_word {string} -- [the key]
    

    
    Returns:
        [list] -- [key list]
    """ 
    key_word = key_word.upper()
    l = []
    for letter in key_word:
        if letter in string.punctuation or letter == " ":
            pass
        else:
            l.append(letters_to_num[letter])

    return l 

def Vigenere_Encryption(Message, key):
    
    Message = Message.upper()
    i = 0
    Cipher_text = ""
    for letter in Message:
        if letter in string.ascii_uppercase:
            Cipher_text += numbers_to_letters[(key[i] + letters_to_num[letter])%26]
            i = (i + 1)%len(key)
    return Cipher_text

def Vigenere_Decryption(Message, key):
    Message = Message.upper()
    key = Vigenere_Key(key)
    i = 0
    decrypted_text = ""
    for letter in Message:
        if letter in string.ascii_uppercase:
            decrypted_text += numbers_to_letters[(letters_to_num[letter]- key[i])%26]
            i = (i + 1)%len(key)

    return decrypted_text  


def grouping(Crypted_text, length):
    groups = {}
    for i in range(length):
        g =[]
        for index, letter in enumerate(Crypted_text):
            
            if index % length == i:
                g.append(letter)
        groups.update({i:"".join(g)})
    return groups

Mas = 'He buried her beside her husband. After the services were over and the few mourners had gone, he stood alone in a cold November wind and looked at the two graves, one open to its burden and the other mounded and covered by a thin fuzz of grass. He turned on the bare, treeless little plot that held others like his mother and father and looked across the flat land in the direction of the farm where he had been born, where his mother and father had spent their years. He thought of the cost exacted, year after year, by the soil; and it remained as it had been—a little more barren, perhaps, a little more frugal of increase. Nothing had changed. Their lives had been expended in cheerless labor, their wills broken, their intelligences numbed. Now they were in the earth to which they had given their lives; and slowly, year by year, the earth would take them. Slowly the damp and rot would infest the pine boxes which held their bodies, and slowly it would touch their flesh, and finally it would consume the last vestiges of their substances. And they would become a meaningless part of that stubborn earth to which they had long ago given themselves. He once thought it himself, that he might die with grief: for his wife, his daughters, his sisters, his father and master the cardinal. But pulse, obdurate, keeps its rhythm. You think you cannot keep breathing, but your ribcage has other ideas, rising and falling, emitting sighs. You must thrive in spite of yourself; and so that you may do it, God takes out your heart of flesh, and gives you a heart of stone. Everything failed to subdue me. Soon everything seemed dull: another sunrise, the lives of heroes, failing love, war, the discoveries people made about each other. The only thing that didn’t bore me, obviously enough, was how much money Tim Price made, and yet in its obviousness it did. There wasn’t a clear, identifiable emotion within me, except for greed and possibly, total disgust. I had all the characteristics of a human being–flesh, blood, skin, hair–but my depersonalization was so intense, had gone so deep, that the normal ability to feel compassion had been eradicated, the victim of a slow, purposeful erasure. I was simply imitating reality, a rough resemblance of a human being, with only a dim corner of my mind functioning. Something horrible was happening and yet I couldn’t figure out why–couldn’t put my finger on it. The only thing that calmed me was the satisfying sound of ice being dropped into a glass of J&B. Eventually I drowned the chow, which Evelyn didn’t miss; she didn’t even notice its absence, not even when I threw it in the walk-in freezer, wrapped in one of her sweaters from Bergdorf Goodman. We had to leave the Hamptons because I would find myself standing over our bed in the hours before dawn, with an ice pick gripped in my fist, waiting for Evelyn to open her eyes. At my suggestion, one morning over breakfast, she agreed, and on the last Sunday before Labor Day we returned to Manhattan by helicopter.But just as I didn’t want to resent my kids, I also didn’t want to find myself too much in love with them. There are parents who don’t like to hear their little girl crying at night, at the vast approaching dark of sleep, and so in their torment think why not feed her a lollipop, and a few years later that kid’s got seven cavities and a pulled tooth. This is how we’ve arrived at the point where we give every kid on the team a trophy in the name of participation. I didn’t want to love my kids so much that I was blind to their shortcomings, limitations, and mediocre personalities, not to mention character flaws and criminal leanings. But I could, I thought, I could love a kid that much. A kid really could be everything, and that scared me. Because once a kid is everything, not only might you lose all perspective and start proudly displaying his participation trophies, you might also fear for that kid’s life every time he leaves your sight. I didn’t want to live in perpetual fear. People don’t recover from the death of a child. I knew I wouldn’t. I knew that having a kid would be my chance to improve upon my shitty childhood, that it would be a repudiation of my dad’s suicide and a celebration of life, but if that kid taught me how to love him, how to love, period, and then I lost him as I lost my dad, that would be it for me. I’d toss in the towel. Fuck it, fuck this world and all its heartbreak. I’d tell that to Connie, and she’d tell me that if that was how I felt I was already a slave to the fear, and good luck. Christ, he thinks, by my age I ought to know. You don’t get on by being original. You don’t get on by being bright. You don’t get on by being strong. You get on by being a subtle crook; somehow he thinks that’s what Norris is, and he feels an irrational dislike taking root, and he tries to dismiss it, because he prefers his dislikes rational, but after all, these circumstances are extreme, the cardinal in the mud, the humiliating tussle to get him back in the saddle, the talking, talking on the barge, and worse, the talking, talking on his knees, as if Wolsey’s unravelling, in a great unweaving of scarlet thread that might lead you back into a scarlet labyrinth, with a dying monster at its heart. Your only chance of survival, if you are sincerely smitten, lies in hiding this fact from the woman you love, of feigning a casual detachment under all circumstances. What sadness there is in this simple observation! What an accusation against man! However, it had never occurred to me to contest this law, nor to imagine disobeying it: love makes you weak, and the weaker of the two is oppressed, tortured and finally killed by the other, who in his or her turn oppresses, tortures and kills without having evil intentions, without even getting pleasure from it, with complete indifference; that’s what men, normally, call love. During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living.'
key =  Vigenere_Key("OMEGA")
enc = Vigenere_Encryption(Mas,key)
print(enc)
groups = grouping(enc, 5) 
def attempted_breaking(Crypted_text, length):
    groups = grouping(Crypted_text,length) 
    brokenKey = []
    for i in range(length):
        text = groups[i]

        brokenKey.append(numbers_to_letters[(letters_to_num[frequency_table(text)[0][0]]- 4)%26])
    return brokenKey
print(attempted_breaking(enc, 5))
print(Vigenere_Decryption(enc, "OMEGA"))