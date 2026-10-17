import discord
import time
from discord.ext import commands
commentidiz = {"non_svolgo_la_differenziata": "Per la salvaguardia dell'ambiente, ti consiglierei di prestare più attenzione a questo tuo tipo di abitudini. Svolgere la raccolta differenziata è un'azione molto importante e che non va assolutamente sottovalutata. Per maggiori informazioni, consulta il volantino dedicato del tuo Comune di resdenza.", "non_mi_importa_del_riscaldamento_globale": "Ciò che stai dicendo è gravissimo! Il riscaldamento globale è un reale, e molto grave, problema che si sta presentando sul nostro Pianeta. Ti consiglierei di ripensare alle tue convinzioni e svolgere delle ricerche nel web.", "mi_piace_fare_del_male_alle_piante": "Questa tua abitudine è molto grave! Le piante non solo sono esseri viventi esattamente come noi, ma, inoltre, sono anche un'importantissima fonte di ossigeno. Cerca di non ripeterlo, non solo per il bene delle piante, ma, naturalmente, anche per il tuo."}
affermazionidiz = ["Sì", "Certo"]
negazionidiz = ["No", "Assolutamente_no"]
intents = discord.Intents.default()
intents.message_content = True
punti = 0

bot1 = commands.Bot(command_prefix='?', intents=intents)

@bot1.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot1.user}')


@bot1.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot1.user}!')

@bot1.command()
async def analisi(ctx, commenti):
    await ctx.send("Benvenuto nella modalità di analisi! Qui, se dovessi nominare, nei tuoi successivi comandi, degli errori nei confronti della salvaguardia dell'ambiente, ti correggerò.")
    if str(commenti) in commentidiz.keys():
        await ctx.send(commentidiz[str(commenti)])
    else:
        await ctx.send("Fortunatamente, la tua richiesta non è stata considerata dannosa per l'ambiente. Continua con queste abitudini!")

@bot1.command()
async def domande(ctx):
    await ctx.send("Benvenuto nella modalità quiz! Qui, ti proporremo delle domande riguardanti l'ambiente a cui dovrai rispondere!")
    await ctx.send("Dobbiamo svolgere continuamente la raccolta differenziata?")
@bot1.command()
async def risposta_uno(ctx, commenti, punti):
    if str(commenti) in affermazionidiz:
        await ctx.send("Perfetto! Passiamo alla prossima domanda!")
        punti += 1
        time.sleep(3)
        await ctx.send("Bisogna essre fieri dell'effetto serra?")
    else:
        await ctx.send("Mi dispiace, la risposta non è corretta.")
        time.sleep(3)
        await ctx.send("Bisogna essre fieri dell'effetto serra?")
@bot1.command()
async def risposta_due(ctx, commenti, punti):
    if str(commenti) in negazionidiz:
        await ctx.send("Perfetto! Passiamo alla prossima domanda!")
        punti += 1
        time.sleep(3)
        await ctx.send("Sei d'accordo con l'abbattimento eccessivo di alberi?")
    else:
        await ctx.send("Mi dispiace, la risposta non è corretta.")
        time.sleep(3)
        await ctx.send("Sei d'accordo con l'abbattimento eccessivo di alberi?")
@bot1.command()
async def risposta_tre(ctx, commenti, punti):
    if str(commenti) in negazionidiz:
        await ctx.send("Perfetto!")
        punti += 1
        time.sleep(3)
        if punti == 3:
            await ctx.send("Complimenti! Hai risposto correttamente alle domande proposte!")
        else:
            await ctx.send("Mi dispiace, non hai totalizzato il massimo dei voti.")  
    else:
        await ctx.send("Mi dispiace, la risposta non è corretta.")
        time.sleep(3)
        if punti == 3:
            await ctx.send("Complimenti! Hai risposto correttamente alle domande proposte!")
        else:
            await ctx.send("Mi dispiace, non hai totalizzato il massimo dei voti.")


bot1.run("MTU1ODQ5MjM0MDYyNzQ0Mzc3Mg.GnRuoN.KZkCJ1HHQc38xWnJjuK7uMYw0X1dN_r9f0D2Yg")