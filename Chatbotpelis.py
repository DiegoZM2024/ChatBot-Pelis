import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Has activado a {bot.user}')

#SALUDO
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy tu bot{bot.user}! de peliculas')

#PELICULAS EN GENERAL
@bot.command()
async def peliculas(ctx):
    peliculas = ["Avatar",
                 "Avengers: Endgame",
                 " Star Wars: Episodio VII El despertar de la fuerza",
                 "Spider-Man: No Way Home",
                 "Jurassic World"
                 ] 
    await ctx.send('Aqui unas peliculas que te pueden gustar:' + ', '.join(peliculas))
    await ctx.send("https://th.bing.com/th/id/R.36529c131a22733a250fd4037fe92459?rik=UG5p2cwiOInr2A&pid=ImgRaw&r=0")

#PELICULAS DE TERROR
@bot.command()
async def terror(ctx):
    terror_peliculas = ["It","FIVE NIGHTS AT FREDDY","Annabelle: Creation"]
    await ctx.send('Las películas de terror buscan generar miedo usando lo sobrenatural, psicológico o violento. Clásicos como Psicosis y modernas como El Conjuro destacan en el género, explorando nuestros miedos más profundos.')
    await ctx.send('Aqui algunas peliculas de terror:'+ ', '.join(terror_peliculas))
    await ctx.send('https://th.bing.com/th/id/OIP.9xwxahJNE3nqozb2HyOs9QHaHa?rs=1&pid=ImgDetMain')

#PELICULAS DE ACCION
@bot.command()
async def accion(ctx):
    accion_peliculas = ["Avengers: Endgame","Iron Man 3","The Dark Knight Rises "]
    await ctx.send('Las películas de acción presentan escenas emocionantes con peleas, persecuciones y explosiones, donde los héroes enfrentan grandes desafíos. Su ritmo acelerado mantiene al espectador al borde del asiento.')
    await ctx.send('Aqui algunas peliculas de accion:'+ ', '.join(accion_peliculas))
    await ctx.send('https://img.freepik.com/premium-photo/fiery-explosion-with-white-background-red-explosion-with-word-fire-it_81048-4728.jpg?w=2000')

#PELICULAS ANIMADAS
@bot.command()
async def animadas(ctx):
    animadas_peliculas = ["El Rey León ","Frozen II ","Minions"]
    await ctx.send('Las películas animadas utilizan técnicas de animación para contar historias, destacándose por su estilo visual, narrativas accesibles y personajes memorables. Abordan temas de aventura y relaciones, y tienen un notable impacto cultural.')
    await ctx.send('Aqui algunas peliculas animadas:'+ ', '.join(animadas_peliculas))
    await ctx.send('https://th.bing.com/th/id/OIP.bPKALbV70frlVxCEY5UJ2QHaEK?rs=1&pid=ImgDetMain')

#RAMDON
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#TOKEN
bot.run("MTI4NDI5ODAwMjkxNTI2MjQ5NQ.GqEEoa.fbcz36ZQsl2qUeVdo7k2-aCchkxLT981E7mSX4")