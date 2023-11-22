import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='?', intents=intents)

mogs = [
    "https://tenor.com/view/mog1-mog-cat-gif-19684059",
    "https://tenor.com/view/mog-mog2-rog-rog2-gog-gif-20524383",
    "https://tenor.com/view/mog-mog3-rog-rog3-gog-gif-20524397",
    "https://tenor.com/view/mog-mog4-rog-rog4-gog-gif-20524410",
    "https://tenor.com/view/mog-mog5-rog-rog5-gog-gif-20524450",
    "https://tenor.com/view/mog6-mog-lel-gif-25476903",
    "https://tenor.com/view/mog7-mog-rog-rog7-gog-gif-20524514",
    "https://tenor.com/view/mog-mog8-rog-rog8-gog-gif-20524534",
    "https://tenor.com/view/mog-mog9-rog-rog9-gog-gif-20528855",
    "https://tenor.com/view/mog-mog10-rog-rog10-gog-gif-20528899",
    "https://tenor.com/view/mog-mog11-gog-gog11-rog-gif-20528927",
    "https://tenor.com/view/mog-12-cat-mog12-mogcat-gif-23205111",
    "https://tenor.com/view/mog-mog12-gog-gog12-rog-gif-20529000", # mog 13
    "https://tenor.com/view/mog-mog14-gog-gog14-rog-gif-20549274",
    "https://tenor.com/view/mog-mog15-rog-rog15-gog-gif-20549304",
    "https://tenor.com/view/mog-mog16-gog-gog16-rog-gif-20549321",
    "https://tenor.com/view/mog-mog17-gog-gog17-rog-gif-20549341",
    "https://tenor.com/view/mog18-mog-moggy-gif-26264380",
    "https://tenor.com/view/mog-mog19-rog-rog19-cat-mad-gif-20549428",
    "https://tenor.com/view/mog-mog20-gog-gog20-rog-gif-20549449",
    "https://tenor.com/view/mog21cat-gif-20702176",
    "https://tenor.com/view/mog-mog22-roger-rog22-gog-gif-20549470",
    "https://tenor.com/view/cat-situp-cat-mog23-mog-gog23-gif-20549478",
    "https://tenor.com/view/mog24-mog-24-cat-gif-gif-20702200",
    "https://tenor.com/view/mog-mog25-25-cat-gif-gif-20702225 https://tenor.com/view/mog-mog25-cat-dog-what-the-cat-doin-gif-24414365",
    "https://tenor.com/view/mog26-mog-26-cat-gif-gif-20702299",
    "https://tenor.com/view/mog27-mog-27-cat-gif-gif-20702334",
    "https://tenor.com/view/mog28-mog-28-cat-gif-gif-20702307",
    "https://tenor.com/view/mog29-mog-29-cat-gif-gif-20702330",
    "https://tenor.com/view/mog30-cat-gif-cat-gif-gif-20702333",
    "https://tenor.com/view/mog31-mog-31-cat-gif-gif-20702351",
    "https://tenor.com/view/mog32-mog-32-cat-gif-gif-20702349",
    "https://tenor.com/view/mog33-mog-33-cat-gif-cat-gif-20702362",
    "https://tenor.com/view/mog34-mog-34-cat-gif-gif-20703114",
    "https://tenor.com/view/mog35-mog-35-cat-gif-cat-gif-20703117",
    "https://tenor.com/view/mog36-mog-36-cat-gif-cat-gif-20703121",
    "https://tenor.com/view/mog37-mog-37-cat-gif-cat-gif-20703129",
    "https://tenor.com/view/mog38-mog-38-cat-gif-cat-gif-20703139",
    "https://tenor.com/view/mog39-mog-39-cat-gif-cat-gif-20703160",
    "https://tenor.com/view/mog40-mog-40-cat-gif-cat-gif-20703149",
    "https://tenor.com/view/mog41-mog-41-cat-gif-cat-gif-20703167",
    "https://tenor.com/view/mog42-mog-42-cat-gif-cat-gif-20703166",
    "https://tenor.com/view/mog-cat-mog43-43-mogcat-gif-23218388",
    "https://tenor.com/view/mog-cat-love-mogcat-mog44-442oons-gif-23218416",
    "https://tenor.com/view/mog45-mog-gif-24242305",
    "https://tenor.com/view/mog46-mog-gif-24270354",
    "https://tenor.com/view/mog-mog47-47-mogcat-cat-gif-24611843 mog 47 is the same as mog 53 btw",
    "https://tenor.com/view/mog48-48-mog-gif-24617839",
    "https://tenor.com/view/mog-49-mogcat-mog49-cat-gif-24611253",
    "https://tenor.com/view/mog-47-mogcat-cat-mog47-gif-24611315", # mog 50
    "https://tenor.com/view/mog-47-mogcat-mog47-cat-gif-24611354", # mog 51
    "https://tenor.com/view/mog-47-mogcat-cat-mog47-gif-24611366", # mog 52
    "https://tenor.com/view/mog-53-mog53-mogcat-cats-gif-24611858 mog 53 is the same as mog 47 btw",
    "https://tenor.com/view/mog-47-mog47-mogcat-cat-gif-24623069", # mog 54
    "https://tenor.com/view/mog-mogcat-cat-mog55-55-gif-24623108",
    "https://tenor.com/view/mog-56-mog56-mogcat-cat-gif-24623131",
    "https://tenor.com/view/mog-57-mog57-mogcat-cat-gif-24626113",
    "https://tenor.com/view/mog-mog58-58-mogcat-cat-gif-24712744",
    "https://tenor.com/view/mog59-mogcat-mog-59-cat-gif-25139154",
    "https://tenor.com/view/mog-60-mog60-mogcat-cat-gif-24746366",
    "https://tenor.com/view/mog61-mog-cat-piano-keyboard-gif-25245372",
    "https://tenor.com/view/mogcat-cat-mog62-mog-62-gif-25243459",
    "https://tenor.com/view/mogcat-cat-mog63-mog-63-gif-25243563",
    "https://tenor.com/view/mogcat-cat-mog64-mog-64-gif-25243613 https://tenor.com/view/mogcat-cat-mog64-mog-64-gif-25243600",
    "https://tenor.com/view/mog65-mog-cat-fat-fat-cat-gif-25245401",
    "https://tenor.com/view/mog66-gif-26386711",
    "https://tenor.com/view/mog67-mog-mog-cat-67-gif-26307180",
    "https://tenor.com/view/mog68-gif-26386737",
    "https://tenor.com/view/mog-mog69-gif-24662410",
    "https://tenor.com/view/mog-70-mog70-mogcat-cat-gif-25484762",
    "https://tenor.com/view/mog-mog71-mog-cat-cat-mog-gif-cat-71-mog-cat-gif-26891533",
    "https://tenor.com/view/mog-72-mog72-mogcat-cat-gif-25484786",
    "https://tenor.com/view/mog73-mog-73-mogcat-cat-gif-25661115",
    "https://tenor.com/view/mog74-mog-74-mogcat-cat-gif-25661117",
    "https://tenor.com/view/mog75-mogambo-khush-hua-75th-birthday-mogcat-cat-gif-25661119 https://tenor.com/view/mog-cat-funny-funny-cat-gif-21691815",
    "https://tenor.com/view/mog76-mog-76-mogcat-cat-gif-25661163",
    "mog 77 does not exist; see mog 76 or mog 78",
    "https://tenor.com/view/mog78-mog-78-mogcat-cat-gif-25661179",
    "https://tenor.com/view/mog79-mog-79-mogcat-cat-gif-25661183",
    "https://tenor.com/view/mog80-mogambo-khush-hua-mogcat-cat-80-gif-25661185",
    "https://tenor.com/view/mog81-mog-81-mogcat-cat-gif-25661190",
    "https://tenor.com/view/mog82-mog-82-mogcat-cat-gif-25661189",
    "https://tenor.com/view/mog83-mog-83-mogcat-cat-gif-25661195",
    "https://tenor.com/view/mog84-mog-84-mogcat-cat-gif-25661196",
    "https://tenor.com/view/cat-mog-moggy-mog-cat-mog85a-gif-26891592",
    "https://tenor.com/view/mog-moggy-mog-cat-cat-mog86-gif-26924342",
    "https://tenor.com/view/mog-moggy-mog-cat-cat-mog87-gif-26891600",
    "https://tenor.com/view/mog-moggy-cat-mog-cat-mog88-gif-26891585",
    "https://tenor.com/view/mog-mog-cat-cat-moggy-mog89-gif-26891615",
    "https://tenor.com/view/mog90-mog-cat-mog-90-gif-26316937",
    "https://tenor.com/view/mog91-mog-mog-cat-91-cat-mog-gif-26326775",
    "https://tenor.com/view/mog92-mogambo-khush-hua-cat-mog-cat-92-gif-26891548",
    "https://tenor.com/view/mog93-mogli-moggy-mog-cat-cats-gif-26891619",
    "https://tenor.com/view/mog94-mog-cat-moggy-mog-cat-gif-26891569",
    "https://tenor.com/view/mog95-mog-cat-moggy-95-gif-26891553",
    "https://tenor.com/view/mog-moggy-mog-cat-mog96-cat-gif-26891576",
    "https://tenor.com/view/mog-gif-26318100",
    "https://tenor.com/view/mog-98-mog-gif-6196803731608159364 https://tenor.com/view/mog-98-mog-gif-6196803731608159364",
    "https://tenor.com/view/mog99-gif-26180482",
    "https://tenor.com/view/mog100-gif-26133816",
    "https://tenor.com/view/mog101-mog-cat-mog-moggy-cat-gif-26891557",
    "https://tenor.com/view/mog-mog102-102-cat-mog-mog-cat-gif-26300330",
    "https://tenor.com/view/mog103-cat-mog-mog-cat-mog-gif-26428549",
    "https://tenor.com/view/mog-104-gif-6336716868645477420 https://tenor.com/view/mog-mog-104-gif-816714745653365479 https://tenor.com/view/mog-104-mog-104-gif-822952215075303495 https://tenor.com/view/mog-mog-104-mog-100-mog-1000-gif-16714640344074906384",
    "https://tenor.com/view/mog-mog-105-105-gif-1879241882392112618 https://tenor.com/view/mog-105-mog-105-mog105-gif-13830050651316603744",
    "https://tenor.com/view/mog-106-mog-106-gif-2432050528772104764",
    "https://tenor.com/view/mog-mog-107-107-gif-1859466788014934118",
    "https://tenor.com/view/mog-mog-108-108-gif-11883533419252950732 https://tenor.com/view/mog-108-mog-108-gif-16833618277488244199",
    "https://tenor.com/view/109-mog-109-mog-gif-17421863116584677729",
    "https://tenor.com/view/110-mog-110-mog-gif-280233573771536682",
    "https://tenor.com/view/mog-mog-111-111-gif-8422683939033564578",
    "https://tenor.com/view/mog-mog-112-112-gif-4198922926690955155",
    "https://tenor.com/view/mog-mog-113-113-gif-8896785179839969196",
    "https://tenor.com/view/mog-mog-114-114-gif-13088143464782017856",
    "https://tenor.com/view/mog-mog-115-115-gif-1352499604648829037",
    "https://tenor.com/view/mog-116-mog-116-gif-3093957462083455758",
    "https://tenor.com/view/mog-117-mog-117-gif-1995972873773813841",
    "https://tenor.com/view/mog-118-mog-118-gif-11487753289118386160",
    "https://tenor.com/view/mog-mog-119-119-gif-9290021765772760380",
    "https://tenor.com/view/mog-120-mog-120-gif-4113456347564774129", # its finally over
]

@bot.event
async def on_ready():
    print(f'ready, logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='mog', help='Get a mog by index or random')
async def get_mog(ctx, index_or_random: str):
    if index_or_random.lower() == 'random':
        await ctx.send(random.choice(mogs))
    else:
        try:
            index = int(index_or_random)
            if 1 <= index <= len(mogs):
                mog = mogs[index - 1]
                await ctx.send(mog)
            else:
                await ctx.send(f'mog {index} does not exist')
        except ValueError:
            await ctx.send('argument has to be a number or "random"')

bot.run('YOUR_TOKEN_HERE')