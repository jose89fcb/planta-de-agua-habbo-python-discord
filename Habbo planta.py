import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def planta(ctx,  keko):
    await ctx.message.delete()
    await ctx.send("Generando planta de agua...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=none&direction=4&head_direction=4&gesture=std&size=l"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1
    
    #####
    img2 = (10, 10, 120, 60) #Recortamos la imagen del keko
    img1 = img1.crop(img2)
    ####
   
    
   
    
    
    img2 = img1.copy()
    
    
  


    lluvia = Image.open(r"imagenes/lluvia.png").convert("RGBA") #Imagen de la lluvia
    img1 = lluvia.resize((169,193), Image.ANTIALIAS)#tamaño de la lluvia
 
    hoja = Image.open(r"imagenes/hoja.png").convert("RGBA") #Imagen de la hoja
    img1 = hoja.resize((169,193), Image.ANTIALIAS)#tamaño de la hoja

    
    
    
    img1 = Image.open(r"imagenes/plantadeagua.png").convert("RGBA") #Imagen de la planta
    

   


    img1.paste(img2,(75,45), mask = img2) #Posicion del keko 1
    
    
    img1.paste(hoja,(0,0), mask = hoja) #Posicion de la hoja 

    img1.paste(lluvia,(0,0), mask = lluvia) #Posicion de la lluvia

    




    
    
  
    

    
    
  
    


   
    
   


    
    
    
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)
       

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))

      




       

         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])    


