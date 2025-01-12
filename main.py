import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$contaminación'):
        await message.channel.send("""La contaminación es la presencia de sustancias o agentes
contaminantes en el medio ambiente, que pueden tener efectos negativos sobre la salud humana,
animal y vegetal. Se origina principalmente por actividades industriales, el uso de vehículos,
la deforestación y el manejo inadecuado de residuos.""")
    elif message.content.startswith('$solución'):
        await message.channel.send("""Solución: Reducir el uso de combustibles fósiles,
fomentar el reciclaje, promover el uso de energías renovables y concienciar sobre 
la importancia de conservar los ecosistemas.""")
    elif message.content.startswith('$riesgos'):
        await message.channel.send("""Riesgos: Enfermedades respiratorias,
pérdida de biodiversidad, cambio climático, deterioro de los ecosistemas y escasez de recursos naturales.""")


client.run("INGRESA TU TOKEN")
