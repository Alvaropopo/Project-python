from oop import*
MSalah=FootballPlayer("Mohammad Salah",89,"RW","Egypt","Liverpool")
VVanDijk=FootballPlayer("Virgil Van Dijk",89,"CB","The Netherlands","Liverpool")
SMcTominay=FootballPlayer("Scott McTominay",79,"CDM","Scotland","Manchester United")
AGarnacho=FootballPlayer("Alejandro Garnacho Ferreyra",74,"LW","Argentina","Manchester United")
RVarane=FootballPlayer("Raphael Varane",84,"CB","France","Manchester United")
WEndo=FootballPlayer("Wataru Endo",79,"CDM","Japan","Liverpool")
AOnana=Keeper("Andre Onana",84,"GK","Cameroon","Manchester United")
Allison=Keeper("Allison Ramses Becker",89,"GK","Brazil","Liverpool")


MSalah.kick()
VVanDijk.getball()
if(not RVarane.tackle(VVanDijk)):
    VVanDijk.kick()
    if(AOnana.catchball()):
        AOnana.kick()
    else:
        VVanDijk.goal()
else:
    RVarane.getball()
    RVarane.kick()
    AGarnacho.getball()
    AGarnacho.kick()
    if(Allison.catchball()):
        Allison.kick()
    else:
        AGarnacho.goal()
