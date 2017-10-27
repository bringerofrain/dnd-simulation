import random

tohit = 12;
bonus = 0;
hit = 0.0;
advhit=0.0;
rot = 3000
for i in range(1,rot):
    roll1 = random.randint(1,20);
    advroll = random.randint(1,20);
    if roll1+bonus >= tohit:
        hit+=1.0;
        advhit+=1.0;
    elif advroll+bonus >= tohit:
        advhit+=1.0;

hit = hit/rot * 100;
advhit = advhit/rot *100;

print ("Normal Roll: %.2f Adv Roll: %.2f" % (hit,advhit));

#smite vs battlemaster

battlerounds = 45;
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;

    loopbr = 1;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10);
        if roll1 >= tohit:
            dmg += random.randint(1,10);

        if (rollbon == 20):
            dmg += random.randint(1, 4);
        if rollbon >= tohit:
            dmg += random.randint(1, 4);
        if (roll2 == 20):
            dmg += random.randint(1, 10);
        if roll2 >= tohit:
            dmg += random.randint(1, 10);

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Total Base Line Damage 1 Attack per Short Rest: %.2f"%(dmgavg));
## Battle Master
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice+=1;
        if (rollbon == 20):
            dmg += random.randint(1, 4)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if rollbon >= tohit:
            dmg += random.randint(1, 4)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll2 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0);
            if roll1 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (rollbon == 20):
                dmg += random.randint(1, 4) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0);
            if rollbon >= tohit:
                dmg += random.randint(1, 4) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll2 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0);
            if roll2 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));
## Battle Master Orc DW
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,8)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll1 >= tohit:
            dmg += random.randint(1,8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice+=1;
        if (rollbon == 20):
            dmg += random.randint(1, 8)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if rollbon >= tohit:
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 8)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll2 >= tohit:
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
            if roll1 >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (rollbon == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
            if rollbon >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll2 == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
            if roll2 >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("DualWFeat Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));
## Battle Master Orc
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,10);
        if roll1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice+=1;
        if (rollbon == 20):
            dmg += random.randint(1, 4)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,4);
        if rollbon >= tohit:
            dmg += random.randint(1, 4)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,10);
        if roll2 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,10);
            if roll1 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (rollbon == 20):
                dmg += random.randint(1, 4) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,4);
            if rollbon >= tohit:
                dmg += random.randint(1, 4) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll2 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,10);
            if roll2 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC PAM Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));

## Battle Master Orc
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,10);
        if roll1+1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,8) if supremedice<=5 else 0)+1;
            supremedice+=1;

        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,10);
        if roll2+1 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,8) if supremedice<=5 else 0)+1;
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,10);
            if roll1+1 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0)+1;
                supremedice += 1;

            if (roll2 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,10);
            if roll2+1 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 8) if supremedice <= 5 else 0)+1;
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC Abili STR Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));

## Battle Master Orc DW
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,8)+(random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,8);
        if roll1 >= tohit:
            dmg += random.randint(1,8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice+=1;
        if (rollbon == 20):
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,8);
        if rollbon >= tohit:
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,8);
        if roll2 >= tohit:
            dmg += random.randint(1, 8)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,8);
            if roll1 >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (rollbon == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,8);
            if rollbon >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll2 == 20):
                dmg += random.randint(1, 8) + (random.randint(1, 8)+random.randint(1,8) if supremedice <= 5 else 0)+ random.randint(1,8);
            if roll2 >= tohit:
                dmg += random.randint(1, 8) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC DualWFin Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));

## Champion Orc
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;

    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1>=19):
            dmg += random.randint(1,10)+ random.randint(1,10);
        if roll1 >= tohit:
            dmg += random.randint(1,10);

        if (rollbon >=19):
            dmg += random.randint(1, 4)+ random.randint(1,4);
        if rollbon >= tohit:
            dmg += random.randint(1, 4);

        if (roll2 >=19):
            dmg += random.randint(1, 10)+ random.randint(1,10);
        if roll2 >= tohit:
            dmg += random.randint(1, 10);


        if Surge==True:
            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1>=19):
                dmg += random.randint(1, 10)+ random.randint(1,10);
            if roll1 >= tohit:
                dmg += random.randint(1, 10);

            if (rollbon>=19):
                dmg += random.randint(1, 4) + random.randint(1,4);
            if rollbon >= tohit:
                dmg += random.randint(1, 4);

            if (roll2>=19):
                dmg += random.randint(1, 10) + random.randint(1,10);
            if roll2 >= tohit:
                dmg += random.randint(1, 10);


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC Champ w/ Action Surge DMG/prSR: %.2f"%(dmgavg));


## Battle Master Orc Gaxe
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,12)+(random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,12);
        if roll1 >= tohit:
            dmg += random.randint(1,12)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice+=1;

        if (roll2 == 20):
            dmg += random.randint(1, 12)+(random.randint(1,8) if supremedice<=5 else 0)+ random.randint(1,12);
        if roll2 >= tohit:
            dmg += random.randint(1, 12)+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;

        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 12) + (random.randint(1, 8) if supremedice <= 5 else 0)+ random.randint(1,12);
            if roll1 >= tohit:
                dmg += random.randint(1, 12) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

            if (roll2 == 20):
                dmg += random.randint(1, 12) + (random.randint(1, 8) if supremedice <= 5 else 0)+ random.randint(1,12);
            if roll2 >= tohit:
                dmg += random.randint(1, 12) + (random.randint(1, 8) if supremedice <= 5 else 0);
                supremedice += 1;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC GAXE Supremecy Dice w/ Action Surge DMG/prSR: %.2f"%(dmgavg));

## Smite Master
totaldmg = 0;
for i in range(1, rot):  # Base line Damage

    dmg = 0;
    smitedice = 0;
    loopbr = 1;
    Surge = True;
    while (True):  # Battleround loop
        roll1 = random.randint(1, 20);
        rollbon = random.randint(1, 20);
        roll2 = random.randint(1, 20);

        if (roll1 == 20):
            dmg += random.randint(1, 10);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
        if roll1 >= tohit:
            dmg += random.randint(1, 10);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
            smitedice += 1;
        if (rollbon == 20):
            dmg += random.randint(1, 4);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
        if rollbon >= tohit:
            dmg += random.randint(1, 4);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
            smitedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 10);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
        if roll2 >= tohit:
            dmg += random.randint(1, 10);
            if smitedice <= 2:
                dmg += random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8);
            smitedice += 1;


        if loopbr == battlerounds:
            totaldmg += dmg;
            break;
        loopbr += 1;

dmgavg = totaldmg / rot;
print ("Smite Dice DMG/prSR: %.2f" % (dmgavg));

## Collosus Slayer
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;

    while (True): #Battleround loop
        Coll = True;
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,8) if Coll else 0);
        if roll1+2+1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,8) if Coll else 0)+1;
            Coll = False;
        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,8) if Coll else 0);
        if roll2+2+1 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,8) if Coll else 0)+1;
            Coll = False;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("100 uptime Collosus Slayer DMG/prSR: %.2f"%(dmgavg));

## Collosus Slayer
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;

    while (True): #Battleround loop
        Coll = True;

        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,8) if Coll else 0);
        if roll1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,8) if Coll else 0);
            Coll = False;
        if (rollbon == 20):
            dmg += random.randint(1, 4)+(random.randint(1,8) if Coll else 0);
        if rollbon >= tohit:
            dmg += random.randint(1, 4)+(random.randint(1,8) if Coll else 0);
            Coll = False;
        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,8) if Coll else 0);
        if roll2 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,8) if Coll else 0);
            Coll = False;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
#print ("Collosus noproc 1st attack DMG/prSR: %.2f"%(dmgavg));

## Battle Master
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1==20):
            dmg += random.randint(1,10)+(random.randint(1,10) if supremedice<=5 else 0);
        if roll1 >= tohit:
            dmg += random.randint(1,10)+(random.randint(1,10) if supremedice<=5 else 0);
            supremedice+=1;
        if (rollbon == 20):
            dmg += random.randint(1, 4)+(random.randint(1,10) if supremedice<=5 else 0);
        if rollbon >= tohit:
            dmg += random.randint(1, 4)+(random.randint(1,10) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll2 == 20):
            dmg += random.randint(1, 10)+(random.randint(1,10) if supremedice<=5 else 0);
        if roll2 >= tohit:
            dmg += random.randint(1, 10)+(random.randint(1,10) if supremedice<=5 else 0);
            supremedice += 1;
        if (roll3 == 20):
            dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
        if roll3 >= tohit:
            dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
            supremedice += 1;
        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            roll3 = random.randint(1, 20);
            if (roll1 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
            if roll1 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
                supremedice += 1;
            if (rollbon == 20):
                dmg += random.randint(1, 4) + (random.randint(1, 10) if supremedice <= 5 else 0);
            if rollbon >= tohit:
                dmg += random.randint(1, 4) + (random.randint(1, 10) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll2 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
            if roll2 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
                supremedice += 1;
            if (roll3 == 20):
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
            if roll3 >= tohit:
                dmg += random.randint(1, 10) + (random.randint(1, 10) if supremedice <= 5 else 0);
                supremedice += 1;
        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Supremecy Dice w/ Action Surge 3 attacks DMG/prSR: %.2f"%(dmgavg));


## Champion Orc 3 attacks
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;

    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        roll3 = random.randint(1,20);

        if(roll1>=19):
            dmg += random.randint(1,10)+ random.randint(1,10);
        if roll1 >= tohit:
            dmg += random.randint(1,10);

        if (rollbon >=19):
            dmg += random.randint(1, 4)+ random.randint(1,4);
        if rollbon >= tohit:
            dmg += random.randint(1, 4);

        if (roll2 >=19):
            dmg += random.randint(1, 10)+ random.randint(1,10);
        if roll2 >= tohit:
            dmg += random.randint(1, 10);
        if (roll3 >=19):
            dmg += random.randint(1, 10)+ random.randint(1,10);
        if roll3 >= tohit:
            dmg += random.randint(1, 10);

        if Surge==True:
            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            roll3 = random.randint(1, 20);
            if (roll1>=19):
                dmg += random.randint(1, 10)+ random.randint(1,10);
            if roll1 >= tohit:
                dmg += random.randint(1, 10);

            if (rollbon>=19):
                dmg += random.randint(1, 4) + random.randint(1,4);
            if rollbon >= tohit:
                dmg += random.randint(1, 4);

            if (roll2>=19):
                dmg += random.randint(1, 10) + random.randint(1,10);
            if roll2 >= tohit:
                dmg += random.randint(1, 10);
            if (roll3 >= 19):
                dmg += random.randint(1, 10)+ random.randint(1,10);
            if roll3 >= tohit:
                dmg += random.randint(1, 10);


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC Champ w/ Action Surge 3 attacks DMG/prSR: %.2f"%(dmgavg));


print ("------------------------");
## ORC PAM GWF Supremecy Dice D8 2Attck 1Bon
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            die2 = random.randint(1, 10)
            die2 = (random.randint(1, 10) if die2 <= 2 else die2)
            dmg += die1+die2+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)
        if roll1 >= tohit:
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0)
            supremedice+=1
        if (rollbon == 20):
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            die2 = random.randint(1, 4)
            die2 = (random.randint(1, 4) if die2 <= 2 else die2)
            dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
        if rollbon >= tohit:
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
        if (roll2 == 20):
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            die2 = random.randint(1, 10)
            die2 = (random.randint(1, 10) if die2 <= 2 else die2)
            dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
        if roll2 >= tohit:
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
            supremedice += 1


        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                die2 = random.randint(1, 10)
                die2 = (random.randint(1, 10) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
            if roll1 >= tohit:
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
                supremedice += 1
            if (rollbon == 20):
                die1 = random.randint(1, 4)
                die1 = (random.randint(1, 4) if die1 <= 2 else die1)
                die2 = random.randint(1, 4)
                die2 = (random.randint(1, 4) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
            if rollbon >= tohit:
                die1 = random.randint(1, 4)
                die1 = (random.randint(1, 4) if die1 <= 2 else die1)
                dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
            if (roll2 == 20):
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                die2 = random.randint(1, 10)
                die2 = (random.randint(1, 10) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
            if roll2 >= tohit:
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
                supremedice += 1


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC PAM GWF Supremecy Dice D8 2Attck 1Bon w/ Action Surge DMG/prSR: %.2f"%(dmgavg));
## Battle Master Orc 2 attacks GWF Gsword
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1,6)
            die1 = (random.randint(1,6) if die1<=2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            die3 = random.randint(1, 6)
            die3 = (random.randint(1, 6) if die3 <= 2 else die3)
            die4 = random.randint(1, 6)
            die4 = (random.randint(1, 6) if die4 <= 2 else die4)
            dmg += die1+die2+die3+die4+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll1+1 >= tohit:
            die1 = random.randint(1, 6)
            die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            dmg += die1+die2+(random.randint(1,8) if supremedice<=5 else 0)+1;
            supremedice+=1;

        if (roll2 == 20):
            die1 = random.randint(1, 6)
            die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            die3 = random.randint(1, 6)
            die3 = (random.randint(1, 6) if die3 <= 2 else die3)
            die4 = random.randint(1, 6)
            die4 = (random.randint(1, 6) if die4 <= 2 else die4)
            dmg += die1 + die2 + die3 + die4 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
        if roll2+1 >= tohit:
            die1 = random.randint(1, 6)
            die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
            supremedice += 1;


        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                die3 = random.randint(1, 6)
                die3 = (random.randint(1, 6) if die3 <= 2 else die3)
                die4 = random.randint(1, 6)
                die4 = (random.randint(1, 6) if die4 <= 2 else die4)
                dmg += die1 + die2 + die3 + die4 + (
                random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll1 + 1 >= tohit:
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;

            if (roll2 == 20):
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                die3 = random.randint(1, 6)
                die3 = (random.randint(1, 6) if die3 <= 2 else die3)
                die4 = random.randint(1, 6)
                die4 = (random.randint(1, 6) if die4 <= 2 else die4)
                dmg += die1 + die2 + die3 + die4 + (
                random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll2 + 1 >= tohit:
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC GWF Gsword w/STR Supremecy Dice D8 2 attacks w/ Action Surge DMG/prSR: %.2f"%(dmgavg));

## Battle Master Orc 2 attacks GWF Gsword
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1,6)
            #die1 = (random.randint(1,6) if die1<=2 else die1)
            die2 = random.randint(1, 6)
            #die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            die3 = random.randint(1, 6)
            #die3 = (random.randint(1, 6) if die3 <= 2 else die3)

            dmg += die1+die2+die3+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll1+1 >= tohit:
            die1 = random.randint(1, 6)
            die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            dmg += die1+die2+(random.randint(1,8) if supremedice<=5 else 0)+1;
            supremedice+=1;

        if (roll2 == 20):
            die1 = random.randint(1, 6)
            #die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            #die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            die3 = random.randint(1, 6)
            #die3 = (random.randint(1, 6) if die3 <= 2 else die3)


            dmg += die1 + die2 + die3 +  (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
        if roll2+1 >= tohit:
            die1 = random.randint(1, 6)
            die1 = (random.randint(1, 6) if die1 <= 2 else die1)
            die2 = random.randint(1, 6)
            die2 = (random.randint(1, 6) if die2 <= 2 else die2)
            dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
            supremedice += 1;


        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                die3 = random.randint(1, 6)
                die3 = (random.randint(1, 6) if die3 <= 2 else die3)

                dmg += die1 + die2 + die3 +  (
                random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll1 + 1 >= tohit:
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;

            if (roll2 == 20):
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                die3 = random.randint(1, 6)
                die3 = (random.randint(1, 6) if die3 <= 2 else die3)

                dmg += die1 + die2 + die3 + (
                random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll2 + 1 >= tohit:
                die1 = random.randint(1, 6)
                die1 = (random.randint(1, 6) if die1 <= 2 else die1)
                die2 = random.randint(1, 6)
                die2 = (random.randint(1, 6) if die2 <= 2 else die2)
                dmg += die1 + die2 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC GWF Gsword 5d6 crit w/STR Supremecy Dice D8 2 attacks w/ Action Surge DMG/prSR: %.2f"%(dmgavg));


## Battle Master Orc 2 attacks GWF Gaxe
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1,12)
            die1 = (random.randint(1,12) if die1<=2 else die1)
            die2 = random.randint(1, 12)
            die2 = (random.randint(1, 12) if die2 <= 2 else die2)

            dmg += die1+die2+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0);
        if roll1+1 >= tohit:
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)

            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0)+1;
            supremedice+=1;

        if (roll2 == 20):
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            die2 = random.randint(1, 12)
            die2 = (random.randint(1, 12) if die2 <= 2 else die2)

            dmg += die1 + die2 + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
        if roll2+1 >= tohit:
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)

            dmg += die1 +  (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
            supremedice += 1;


        if Surge==True:

            Surge = False;
            roll1 = random.randint(1, 20);
            rollbon = random.randint(1, 20);
            roll2 = random.randint(1, 20);
            if (roll1 == 20):
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                die2 = random.randint(1, 12)
                die2 = (random.randint(1, 12) if die2 <= 2 else die2)

                dmg += die1 + die2 +(random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll1 + 1 >= tohit:
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)

                dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;

            if (roll2 == 20):
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                die2 = random.randint(1, 12)
                die2 = (random.randint(1, 12) if die2 <= 2 else die2)
                dmg += die1 + die2  + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0);
            if roll2 + 1 >= tohit:
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)

                dmg += die1 +  (random.randint(1, 8) if supremedice <= 5 else 0) + 1;
                supremedice += 1;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("ORC GWF GAxes w/STR Supremecy Dice D8 2 attacks w/ Action Surge DMG/prSR: %.2f"%(dmgavg));
print ("");
print ("-------------------------------------------");
print ("");

##Barb Human Varient PAM Level 5 2 Attacke
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20)+1;
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1, 10)
            #die1 = (random.randint(1, 10) if die1 <= 2 else die1)

            #die2 = (random.randint(1, 10) if die2 <= 2 else die2)
            dmg += die1+die2; #+(random.randint(1,8)+random.randint(1,8) if supremedice<=5 else 0)
        if roll1 >= tohit:
            die1 = random.randint(1, 10)
            #die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1; #+(random.randint(1,8) if supremedice<=5 else 0)

        if (rollbon == 20):
            die1 = random.randint(1, 4)
            #die1 = (random.randint(1, 4) if die1 <= 2 else die1)

            #die2 = (random.randint(1, 4) if die2 <= 2 else die2)
            dmg += die1 + die2; # + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
        if rollbon >= tohit:
            die1 = random.randint(1, 4)
            #die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1 + (random.randint(1, 8) if supremedice <= 5 else 0)
        if (roll2 == 20):
            die1 = random.randint(1, 10)
            #die1 = (random.randint(1, 10) if die1 <= 2 else die1)

            #die2 = (random.randint(1, 10) if die2 <= 2 else die2)
            dmg += die1 + die2;# + (random.randint(1, 8) + random.randint(1, 8) if supremedice <= 5 else 0)
        if roll2 >= tohit:
            die1 = random.randint(1, 10)
            #die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1; # + (random.randint(1, 8) if supremedice <= 5 else 0)
            supremedice += 1



        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb Human Varient PAM Level 5 2 Attacks: %.2f"%(dmgavg));
##Barb Human Varient GWF Level 5 2 Attacke
totaldmg=0;
tohit = 17;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20)+1;
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);
        iscrit = 0;
        if(roll1==20):
            die1 = random.randint(1, 12);
            dmg += die1+die2;
            iscrit =1;
        if roll1 >= tohit:
            die1 = random.randint(1, 12)
            dmg += die1+10;


        if (roll2 == 20):
            die1 = random.randint(1, 12)
            dmg += die1 + die2;
            iscrit = 1;
        if roll2 >= tohit:
            die1 = random.randint(1, 12)
            dmg += die1+10;
        if (iscrit ==1):
            if (rollbon == 20):
                die1 = random.randint(1, 12)
                dmg += die1 + die2;
            if rollbon >= tohit:
                die1 = random.randint(1, 12)
                dmg += die1+10;
        iscrit=0;



        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb Human Varient GWF Level 5 2 Attacks: %.2f"%(dmgavg));

##Barb Orc Varient PAM Level 5 2 Attacke
totaldmg=0;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        rollbon = random.randint(1,20);
        roll2 = random.randint(1,20);

        if(roll1==20):
            die1 = random.randint(1, 10)
            die2 = random.randint(1, 10)
            die3 = random.randint(1, 10)
            dmg += die1+die2+die3;
        if roll1 >= tohit:
            die1 = random.randint(1, 10)
            dmg += die1;
        if (rollbon == 20):
            die1 = random.randint(1, 4)
            die2 = random.randint(1, 4)
            die3 = random.randint(1, 4)
            dmg += die1 + die2 + die3;
        if rollbon >= tohit:
            die1 = random.randint(1, 4)
            dmg += die1;
        if (roll2 == 20):
            die1 = random.randint(1, 10)
            die2 = random.randint(1, 10)
            die3 = random.randint(1, 10)
            dmg += die1 + die2 + die3;
        if roll2 >= tohit:
            die1 = random.randint(1, 10)
            dmg += die1;



        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb Orc PAM Level 5 2 Attacks: %.2f"%(dmgavg));

##Barb/Chmp Human Varient lvl-6/GWFS/Reckless
totaldmg=0;
tohit = 12;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        roll1adv = random.randint(1,20)
        rollbon = random.randint(1,20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1,20);


        if(roll1>=19 or roll1adv >= 19):
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1;
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1;

        if (rollbon >= 19 or rollbonadv >= 19):
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1;
        if rollbon >= tohit or rollbonadv >= tohit:
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1;





        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Chmp Human Varient lvl6/GWFS/Reckless/1 Attk: %.2f"%(dmgavg));


#Barb/Bmast 3/3 Human Varient lvl6/GWFS/Reckless/1 Attk:
totaldmg=0;
tohit = 12;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop

        roll1 = random.randint(1, 20);
        roll1adv = random.randint(1, 20)
        rollbon = random.randint(1, 20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1, 20);

        if (roll1 >= 20 or roll1adv >= 20):
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;
        if (rollbon >= 20 or rollbonadv >= 20):
            die1 = random.randint(1, 4)
            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
        if rollbon >= tohit or rollbonadv >= tohit:
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
            supremedice += 1;



        if Surge==True:

            Surge = False;
            if (roll1 >= 20 or roll1adv >= 20):
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
            if roll1 >= tohit or roll1adv >= tohit:
                die1 = random.randint(1, 10)
                die1 = (random.randint(1, 10) if die1 <= 2 else die1)
                dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
                supremedice += 1;
            if (rollbon >= 20 or rollbonadv >= 20):
                die1 = random.randint(1, 4)
                dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
            if rollbon >= tohit or rollbonadv >= tohit:
                die1 = random.randint(1, 4)
                die1 = (random.randint(1, 4) if die1 <= 2 else die1)
                dmg += die1+(random.randint(1,8) if supremedice<=5 else 0);
                supremedice += 1;


        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Bmast 3/3 Human Varient lvl6/GWFS/Reckless/1 Attk:  %.2f"%(dmgavg));

##Barb/Chmp H-Orc lvl-6/GWFS/Reckless
totaldmg=0;
tohit = 12;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        roll1adv = random.randint(1,20)
        rollbon = random.randint(1,20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1,20);


        if(roll1>=19 or roll1adv >= 19):
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            die2 = random.randint(1, 12)
            die2 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1+die2;
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1;
        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Chmp H-ORC lvl6/GWFS/Reckless/1 Attk: %.2f"%(dmgavg));

##Barb/Chmp H-Orc lvl-6/GWF/GWFS/Reckless
totaldmg=0;
tohit = 17;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        roll1adv = random.randint(1,20)
        rollbon = random.randint(1,20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1,20);
        iscrit = 0;

        if(roll1>=19 or roll1adv >= 19):
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            die2 = random.randint(1, 12)
            die2 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1+die2;
            iscrit == 1
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1+10;
        if (iscrit ==1):
            if (rollbon >= 19 or rollbonadv >= 19):
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                die2 = random.randint(1, 12)
                die2 = (random.randint(1, 12) if die1 <= 2 else die1)
                dmg += die1 + die2;
            if rollbon >= tohit:
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                dmg += die1+10;
        iscrit=0;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Chmp H-ORC lvl7/GWF/GWFS/Reckless/1 Attk: %.2f"%(dmgavg));


##Barb/Chmp Human Vrient lvl-7/GWF/GWFS/Reckless
totaldmg=0;
tohit = 16;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        roll1adv = random.randint(1,20)
        rollbon = random.randint(1,20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1,20);
        iscrit = 0;

        if(roll1>=19 or roll1adv >= 19):
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            die2 = random.randint(1, 12)
            die2 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1;#+die2;
            iscrit == 1
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 12)
            die1 = (random.randint(1, 12) if die1 <= 2 else die1)
            dmg += die1+10+1;
        if (iscrit ==1):
            if (rollbon >= 19 or rollbonadv >= 19):
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                die2 = random.randint(1, 12)
                die2 = (random.randint(1, 12) if die1 <= 2 else die1)
                dmg += die1;# + die2;
            if rollbon >= tohit:
                die1 = random.randint(1, 12)
                die1 = (random.randint(1, 12) if die1 <= 2 else die1)
                dmg += die1+10+1;
        iscrit=0;

        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Chmp Human Varient lvl7/GWF/GWFS/Reckless/1 Attk: %.2f"%(dmgavg));

##Barb/Chmp Human Varient lvl7/PAM/GWFS/Reckless/1 Attk
totaldmg=0;
tohit = 11;
for i in range(1,rot): # Base line Damage

    dmg = 0;
    supremedice = 0;
    loopbr = 1;
    Surge = True;
    while (True): #Battleround loop
        roll1 = random.randint(1,20);
        roll1adv = random.randint(1,20)
        rollbon = random.randint(1,20);
        rollbonadv = random.randint(1, 20);
        roll2 = random.randint(1,20);


        if(roll1>=19 or roll1adv >= 19):
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1;
        if roll1 >= tohit or roll1adv >= tohit:
            die1 = random.randint(1, 10)
            die1 = (random.randint(1, 10) if die1 <= 2 else die1)
            dmg += die1+1;

        if (rollbon >= 19 or rollbonadv >= 19):
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1;
        if rollbon >= tohit or rollbonadv >= tohit:
            die1 = random.randint(1, 4)
            die1 = (random.randint(1, 4) if die1 <= 2 else die1)
            dmg += die1+1;





        if loopbr==battlerounds:
            totaldmg += dmg;
            break;
        loopbr+=1;

dmgavg = totaldmg / rot;
print ("Barb/Chmp Human Varient lvl7/PAM/GWFS/Reckless/1 Attk: %.2f"%(dmgavg));