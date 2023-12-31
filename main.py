from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
import random
from faker import Faker

DATABASE_URL = "postgresql://postgres:Shantanu8983@@localhost:5432/UrlTask"


app = FastAPI()

# CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/terms")
async def get_terms():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her.Dere kan bruke programmet GRATIS i 14 dager.LettFaktura er så lett og selvforklarende at sjansen for at du vil komme til å trenge support er minimal, men hvis du skulle trenge support, så er vi her for deg, med vårt kontor bemannet større delen av døgnet. Etter prøveperioden så fortsetter abonnementet og koster 99 kroner eks. mva per måned, som faktureres årlig. Hvis du ikke ønsker å beholde programmet, så er det bare til å avbryte prøveperioden ved å gi beskjed innen 14 dager fra nedlasting.Dere har selvfølgelig rett til å avslutte bruken av programmet uten kostnad, ved å gi oss beskjed per email innen 14 dager fra nedlasting, om at dere ikke ønsker å fortsette med programmet, og betaler da selvfølgelig ikke heller noe. Hvis vi ikke innen 14 dager fra nedlasting mottar slik beskjed fra dere, så kan ordren av naturlige grunner ikke endres. Med nedlasting menes den dato og klokkeslett når dere har valgt å trykke på knappen Fakturere Nå. Fakturering skjer for ett år av gangen. Prisen for LettFaktura (tilbudspris kr 99,- per måned / ord. pris kr 129,- per måned) er for årsavgift Start for ett års bruk av programmet.(Ved bruk av tilbudsprisen kr 99,- så regnes ett års perioden fra nedlastning.) Alle priser er eks. mva. Timeregistrering. Kalkulering, Medlemsfakturering, Tilbud, Kunde Oppfølging, Lager Telling, Lagerstyring og Engelsk fakturatekst er tilleggsmoduler som kan bestilles etter installasjon av programmet.Årsavgiften er løpende men hvis dere ikke ønsker å fortsette å bruke programmet, så er det bare å gi beskjed tretti dager før starten av den nestfølgende ett års perioden. Introduksjonstilbudet (kr 99,- per måned) er for årsavgift Start for det første året.  Etter det første året faktureres ord. pris hvilket for tiden er, for årsavgift Start, ett hundre og tjueni kroner per måned, for årsavgift Fjernstyring, to hundre og sekstifem kroner per måned og for årsavgift Pro, tre hundre og trettitre kroner per måned. Etter ett år faktureres årsavgift Fjernstyring som standard men dere kan velge Start eller Pro ved å gi beskjed når som helst før forfall. Hvis dere velger å beholde programmet ved å ikke gi oss beskjed per email innen 14 dager fra nedlasting, om at dere ikke ønsker å fortsette med programmet, så aksepterer dere at dere kommer å betale fakturaen for deres bestilling. Kode til programmet vil sendes automatisk etter at fakturaen er betalt. Å ikke betale fakturaen eller sen betaling gir ikke rett til å annullere bestillingen. Vi hjelper gjerne å fikse logo for dere til selvkostpris. Lisens for bruk av LettFaktura selges selvfølgelig i følge gjeldende lover. For å lettere kunne hjelpe dere og gi dere support samt for å følge lovene  må vi av naturlige grunner lagre deres informasjon.I forbindelse med lagring av informasjon så krever loven at vi gir dere følgende informasjon:Hvis dere bestiller som privatperson så har dere den angrerett som loven tilsier. Deres informasjon lagres slik at vi kan hjelpe dere m.m. Vi kommer til å bruke den for å kunne hjelpe dere hvis dere trenger hjelp, følge lovene vedr. bokføring m.m. Når det kommer oppgraderinger og lignende, kan vi komme til å sende dere tilbud og lignende om våre produkter og tjenester per email eller lignende. Dere kan komme til å bli kontaktet per email, post og telefon. Hvis dere ikke ønsker å bli kontaktet, bare send oss en email vedr. det.Dere kan når som helst be om å ikke få tilsendt informasjon om oppgraderinger per email, faks, brev eller lignende og vi kommer da selvfølgelig ikke å gjøre det. Slik begjæring sender dere til oss per email, faks, brev eller lignende. Av naturlige grunner må vi lagre, databehandle og flytte deres data. Deres informasjon lagres inntil videre. Dere gir oss tillatelse til å lagre, databehandle og flytte deres data, samt å sende dere tilbud og lignende per email, faks, brev og lignende. Grunnet måten det fungerer på med programvare trenger tillatelsen også å gis til andre parter. Tillatelsen gis derfor til oss, samt til de bedrifter og/eller person/personer som eier programvaren, kildekoden, hjemmesiden og lignende. Det gis også til nåværende og fremtidige bedrifter eiet og/eller kontrollert av en eller flere av de som i dag eier og/eller kontrollerer oss. Det gis også til nåværende og fremtidige bedrifter eiet og/eller kontrollert av en eller flere av de som i dag eier og/eller kontrollerer de bedrifter, (om noen), som eier eller kommer til å eie programvaren, kildekoden, hjemmesiden og lignende. Det gis også til nåværende og fremtidige personer (om noen) som eier eller kommer til å eie programvaren, kildekoden, hjemmesiden og lignende. Dette både for nåværende og fremtidige produkter og tjenester. Det gis også til annen bedrift, som vi kan bruke for å sende/selge produkter, oppgraderinger og lignende, enten ved underlisensiering eller på annen måte. Dere har selvfølgelig rett å begjære å få del av, endre og slette informasjonen vi holder om dere. Dere har også rett å begjære begrensing av databehandlingen, og å protestere mot databehandlingen og retten til dataportabilitet. Dere har rett å klage til tilsynsmyndighet. Mer juridisk info om oss finner dere . Det er lovene i Irland som er gjeldende lover. Det er selvfølgelig helt frivillig å legge ordre. Vi bruker selvsagt ikke noen automatisert profileringer eller beslutninger. Hvis dere ønsker å kontakte oss, vennligst bruk da informasjonen på denne eller noen av våre andre hjemmesider. Vår erfaring er at våre kunder er meget fornøyde med måten vi jobber på og håper og tror at det også kommer til å bli deres opplevelse.Ha en flott dag!"}

@app.get("/us")
async def get_us():
    return {"message": "We that dispose of and drive this homepage and that also sell the programs that are sold on this homepage are: Lettfaktura Ltd, registered in Ireland with company number 638535. Registered office is in Co. Laois, Ireland.We hope that you will have much joy and use of our homepage.Have a still great day!"}





@app.get("/getAllProducts")
async def get_products_route():
    converted_list = [[7465000852,"Product 1",93881,632235,"Kg",58,"Description for Product 1"],[5752106165,"Product 2",46280,465899,"Liter",47,"Description for Product 2"],[2422695555,"Product 3",42880,1171347,"Liter",79,"Description for Product 3"],[2581987276,"Product 4",98764,867344,"Liter",16,"Description for Product 4"],[6233241536,"Product 5",70659,1939737,"Liter",50,"Description for Product 5"],[1571769736,"Product 6",71091,184941,"Liter",68,"Description for Product 6"],[8252392448,"Product 7",12173,741082,"Kg",4,"Description for Product 7"],[4173937893,"Product 8",66715,774322,"Kg",85,"Description for Product 8"],[1733876550,"Product 9",26408,133300,"Kg",65,"Description for Product 9"],[4876386493,"Product 10",54156,1706394,"Piece",89,"Description for Product 10"],[2800441092,"Product 11",12397,1400929,"Kg",54,"Description for Product 11"],[9200764438,"Product 12",1280,524818,"Kg",70,"Description for Product 12"],[9619323085,"Product 13",85612,1187133,"Kg",69,"Description for Product 13"],[9080206171,"Product 14",65100,460234,"Piece",25,"Description for Product 14"],[6699514855,"Product 15",81104,1044044,"Kg",11,"Description for Product 15"],[9272130698,"Product 16",12225,462301,"Piece",19,"Description for Product 16"],[2571472752,"Product 17",7019,1380450,"Kg",15,"Description for Product 17"],[8620922048,"Product 18",55420,1840476,"Liter",9,"Description for Product 18"],[4521660667,"Product 19",85446,740732,"Piece",1,"Description for Product 19"],[7853266096,"Product 20",92019,1027648,"Liter",47,"Description for Product 20"]]
    print(converted_list,"converted_list")
    return {"message": converted_list}
    