define p = Character ('Me:', kind = nvl, color ="3f9fff")
define j = Character ('Jordan:', kind = nvl, color = "c8ffc8")
define l = Character ('Luke:', kind = nvl,color ="c9fe9b")
define s = Character ('Shawnee:',kind = nvl, color = "89c1c4")
define ja = Character ('July:', kind = nvl, color ="cacda1")
define k = Character ('Katie Kat:',kind = nvl, color = "36c4ce")
define a = Character ("Aoi:", kind = nvl, color = "03ca13")
define u = Character ("Stranger:", kind = nvl, color = "ff0000")
define narrator = nvl_narrator
define menu = nvl_menu
define config.nvl_paged_rollback = False
define config.rollback_enabled = False


label start:
    scene bg umeglechat with fade

    "What should I talk about today..."

    #day 1 

    menu:
        "Here are some topics that have been heavily searched in the last few hours."
        "cats":
            jump kk1
        "gaming":
            jump luke1
        "travel":
            jump aoi1
            
label kk1:
    nvl hide dissolve
    nvl clear 
    "You are now talking to a random stranger!"
    u "hey :)"
    u "do you have a cat?"
    p "I have a cat!"
    
    menu:
        p "and"
        "her name is Rachel":
            jump rachel
        "her name is Cat":
            jump cat
                    
label rachel:
    p "her name is Rachel"
    u "OMG I love rachel already"
    u "but human names are kind of weird"
    u "I'm not sure they're appropriate XD"
    u "I mean imagine calling for Rachel"
    u "like the other day I told my friend who was sleeping over :P"
    u "Pants might try to sleep with you, so please keep the door shut"
    u "now imagine if that was Rachel LOOOOOOOOOL :P"
    u "Hey, Rachel might try to sleep with you, so please keep the door shut!"
    jump kk11
            
label cat:
    p "her name is Cat"
    u "omg, tell Cat that I love her already!"
    u "heehee, I'm in love with mine, his game is Pants. He acts more like a dog tho."
    u "he plays fetch, and he slept in my laundry when he was a kitten"
    u "I found him inside a pant leg"
    u "tada!! a name."
    jump kk11
            
label kk11:
    u "anyway asl?"
    u "I'm Katie Kat, but that's just my online name"
    u "you can call me Katie or kitkat or just Kitty"
    u "I'm a gamer girl xD you should watch my stream sometime"
    u "ok but back to cats! Do you"
    u "think"
    u "cats should wear pants on their hind legs only or on all their legs?"
    u "I'm trying to make a tally"
            
    menu:
        p "hmmm.."
        "all their legs":
            jump allLegs
        "just back legs":
            jump backLegs
        "cats shouldn't wear pants":
            jump kk12
                    
label allLegs:
    p "all their legs"
    u "oh, you're in the minority"
    u "then where would their coat go?just on their back?"
    u "anyways pants refuses to wear clothing"
    u "what a little freeloader"
    u ":3"
    jump kk12
            
label backLegs:
    p "just back legs"
    u "yey! I think so too"
    u "cuz then they can wear their coat on their front legs"
    u "and when they sit up its so cute"
    u ":)"
    jump kk12
                
label kk12:
    p "cats shouldn't wear pants"
    u "soooooo"
    u "asl? I forgot to let you answer. "
    p "I'm Kittie Cat, you can call me Cattie or KatKit for short"
    u "no wait for realllllll"
    p "nah just a stage name"
    u "you're a big fat liar :("
    p ":)"
    u "will you tell me who you really are?"
    
    menu:
        p "hmm..."
        "only if you add me as a friend":
            jump friend1
        "nah, you're probably some dude who's gonna send me a dick pic":
            jump dickPic
            
label dickPic:
        p "nah, you're probably some dude who's gonna send me a dick pic"
        u "wow that's so mean"
        u "i would neverrr :'("
        jump kk13     

label friend1:
    p "only if you add me as a friend"
    u "ok fine, you like cats so I'm sure that we'll be besttttt friends"
    u "but you gotta promise"
    u "you cant ignore me"
    u "and you gotta be ok with me sending you pictures of pants"
    p "pants?"
    u "MY"
    u "C"
    u "A"
    u "T"
    u "geez"
    u "pls"
    u "pay attention"
    p "ohhhk got it"
                
    menu: 
        "I promise"
        "all cats are angels":
            jump kkfriend
        "I'd never say no to pics of your pussy":
            jump pussy
                                
label pussy:
    p "I'd never say no to pics of your pussy"
    u "not impressed"
    jump kk13   
                   
label kkfriend:
    ##kk new friend day 1 route
    p "all cats are angels"
    u "yey!"
    u "new friend"
    u "ok, so this is my first time adding a friend on Umegle"
    u "let me see if I can figure this out"
    u "........."
    u "..."
    u "..."
    u "got it!"
                
    menu:
        "Katie Kat has sent you a friend request"
        "accept?":
            jump kkaccepted
        "deny":
            jump kkdenied

label kkaccepted:
    "you have accepted this user's friend request. You may now view each other on UmegleFriends and send images."
    jump kk13
    
label kkdenied:
    "you have denied this user's friends request. You hurt their feelings :("
    jump kk13
            
label kk13: 
    u "ttyl, s t r a n g e r"
    return
                    
label luke1:
    nvl hide dissolve
    nvl clear 
    "You are now talking to a random stranger!"
    u "What's your LEgion?"
    p "wut"
    u "YOUR LEGION in Legions of Legendaries"
    p "OH"
    p "uhhhh iron"
    u "wow, trash player"
    u "but I can carry you"
    u "GIT GUD"
    u "jk you FELL FOR IT"
    u "you dumb"
    u "weewooweewoo"
    u "that's the sound of the ambulance running away"
    u "because I broke my back"
    u "trying 2 carry this conversation 2"
    u "BYE"
    return

    
label aoi1:
    nvl hide dissolve
    nvl clear 
    "You are now talking to a random stranger!"
    u "heyyyy :) where you at?"
    u "I'm flying over India rn"
    p "wth?"
    p "you have wifi?"
    u "hahahha yeah :P"
    u "first class, private jet"
    p "wow, rich"
    u "nah! My family is comfortable. We're not rich."
    p "..."
    u "WHere are you from"
       
    menu:
        p "I'm from "
        "Toronto":
            jump toronto
        "Murica":
            jump usa
    
label toronto:
    u "no way, that's so cool!"
    u "I was literally there last weekend"
    u "The Toronno hoopball lizards really are something!"
    u "As a fan since July 2019, that last game really meant a lott to me!"
    p "LOL"
    p "I also know nothing about basketball "
    p "so that last game meant a lot to me too"
    u "ehaha L:) we have somethings in common!"
    jump aoi12
    
label usa:
    u "omg, my family has a penthouse suite in Utah! "
    p "why utah"
    u "idk, Utah is so pretty! All the rocks. And people who climb them"
    u "yknow?"
    p "sure, but wouldnt you rather go to dc"
    u "washington?"
    p "no, dc dc"
    u "ok, nah. I once went to a business meeting tthere. not many memoeires."
    u "not multicultureal"
    jump aoi12
    
label aoi12:
    u "do you like hot climates or warm climates?"
    menu:
        p "Idk, probably,"
        "warm places. I hate snow.":
            jump warm
        "cold climates. Nothing poisonous survives":
            jump cold
label warm:
    u "cool, My favourite place is Hawaii."
    u "I want to go there someday"
    u "and just stay"
    u "eat spam and pineapple rice allll day"
    u "lifeeee :):"
    p "sounds like you're already living the life"
    p "riding first class and stuff"
    jump aoi13
    
label cold:
    u "O CANADA here we come."
    u "That's a freezing place"
    u "the locals told me there's only 2 seasons in canada: winter and construction"
    p "lmao that's pretty accurate"
    p "we also have a week of spring, but it's usually a "
    p "false spring. cuz"
    p "it just"
    p "leaves and winter returns"
    u "haha :)"
    u "You're funny"
    jump aoi13
    
label aoi13:
    u "I wish people had a sense of humour"
    u "laughter cures the soul, it really does."
    u "anyway I'm so happy I got to talk with you"
    u "nobody eveeeer wants to have a decent convo in these parts of tthe net"
    p "tell me about it"
    u "have you met any weirdos yet?"
    menu:
        "just some egirl":
            jump egirl
        "literally nobody":
            jump nobody
        "yes. so. many.":
            jump aoi14
            
label egirl:
    u "I want to dieee"
    u "all they want to talk about is cats and shit"
    u "I'm all for nature but"
    u "I'm not interested in only cats"
    jump aoi14
    
label nobody:
    u "so this is your first time on Umegle?"
    u "welcome!"
    u "I'm glad you meet me fist then"
    u "MET ME FIRST****"
    u "ahhhhh"
    p "hahaha"
    p "typo?"
    u "yes, it happens a lot. uh"
    u "turbulance?"
    jump aoi14

label aoi14:
    u "do you have a favourite historic place?"
    u "do you like food?"
    u "?nature"
   
    menu:
        p "my favourite things are"
        "food":
            jump food
        "nature":
            jump nature
        "ancient architecture":
            jump buildings
label food:
    u "same???!!!"
    u "I love dessert!"
    u "flan, pudding, eggs"
    p "I don't think eggs are a dessert."
    u "YES THEY ARE"
    u "eggs can be"
    p "I've literally never had eggs for a dessert LOOOOOL"
    u "actually..."
    u "same but I like them. "
    p "LOL you're kind of funny too"
    u "in a good way?"
    p "uhmmmm..."
    u "wOw that's so r00d"
    p "I DIDN'T SAY NO"
    u "you meant it :("
    u "but I didn't say it"
    u ":(((((((((("
    u "you jump to conclusions faster than my lastt girlfriend"
    u ":(((((((((((((((((((((((((((((((("
    u "... actually"
    u "can I friend you?"
    u "I wanna show you my food!"
    
    menu: 
        "..."
        "Only if you let me share cat photos with you!":
            jump rabbit
        "I will alwayyyys be down for food porn":
            jump afriend
                                
label rabbit:
    u "uhmmmm ok"
    u "I'm more of a rabbit person"
    p "I like rabbits too!"
    u "yeah, they're delicious"
    p "............."
    u "sorry, the truth is"
    u "I like nature but"
    u "I don't want nature in my house ok?"
    p "yeah i get that"
    jump aoi15   
                   
label afriend:
    #aoi new friend day 1 route
   
    menu:
        "Travel4Eva has sent you a friend request"
        "accept?":
            jump aoi15
        "deny":
            jump aoi15
            # aoi sends food pic
    
label nature:
    u "Do you wanna go for a hike sometime?"
    p "with you?"
    u "bro, I just met you"
    p "you didn't specify"
    u "I just wanted to know if you'd send me nice nature pics on UmgeleFriends"
    p "Yeah, I'd do thatt"
    jump aoi15
        
label buildings:
    u "I dont really understnd architeture"
    u "but they always are nice photo ops"
    p "how many countries have you been to?"
    u "a number, I don't count."
    u ".... maybe 30"
    p "30?????"
    u "business meetings :P"
    p "wow... can I send you my resume? You hiring?"
    u "hahahah not at the moment"
    u "I don't know if you could survive my line of work"
    p "so... you do work"
    u "obviously!"
    u "I'm not rich! :("
    p "first class"
    u "everyone uses first class when there's business tot be done"
    u "to*"
    p "I don't think I've ever flew outside of economy"
    u "that's so cool! What a life that must be"
    u "sometimes I try to imagine what life like that is like"
    u "is that weird?"
    u "but I don't want to give up my wine and dine comfort"
    jump aoi15
    
label aoi15:
    
    u "well"
    u "since you're a commoner"
    u "I've always wanted to ask"
    u "Do you like mom and pop stores or fine dining?"
    p "you... cchanged the topic"
    u "I know :P"
    u "My thoughts just go everywhereeeee weee"
    p "just like your plane?"
    u "hahahha, yeah"    
    u "let them eat cake."
    
    menu:
        "I'm more into..."
        "hole-in-the-wall rare gems":
            jump momnpops
        "artistic, well-plated gourmet food":
            jump aoi16
            # aoi sends another food pic
            
label momnpops:
    u "That's so cooool"
    u "I sometimes think about wandering around and just"
    u "seeing the sights"
    u "and putting myself into other people's shoes"
    u "but i just cant do it"
    u "It's kinda dangerous"
    p "what are you afraid of?"
    u "LOL people"
    u "I hate peopleeee"
    u "they're so judgemental"
    u "people treat me differently"
    u "but I dont care"
    jump aoi16
    
label aoi16:
    u "anyways, gourmet food always makes me feel like"
    u "I can experience something the chef wanted me to feel"
    u "the beauty of being full"
    u "and how beautiful life can be"
    p "I can't say I've felt that before"
    u "My child, art comes at a price"
    p "I've actually always wondered"
    p "how do you know if art is good or bad?"
    u "well... that's easy"
    u "the more rare and interesting it is, the more it is worth"
    u "tthe curators decide based on the market values, and you decide if it's worth it"
    u "who knows, maybe you'll profit from keeping it awhile"
    p "knowledgeable"
    u "BUT"
    u "hahah"
    u "what do I know?"
    u "I'm just some dumb blonde"
    p "not all blondes are dumb"
    u ":P I'm acttually not even blonde"
    p "neither am I"
    u "or are you?"
    p "am I?"
    u "anyways"
    u "plane landing bye"
    return
        



    
    

    
        
