import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def geri_dönüşüm(ctx):
    await ctx.send(f'Eğer geri dönüşüm atıklarını hangi kategoriye atacağınızı bilmiyorsanız ve öğrenmek istiyorsanız bilgi yazın!')

@bot.command()
async def bilgi(ctx):
    await ctx.send(f'Cam atıkları cam geri dönüşüm kutusuna atabilirsiniz.')
    time.sleep(1)
    await ctx.send(f'Plastik atıkları plastik geri dönüşüm kutusuna atabilirsiniz.')
    time.sleep(1)
    await ctx.send(f'Kağıt atıkları kağıt geri dönüşüm kutusuna atabilirsiniz.')
    time.sleep(1)
    await ctx.send(f'Metal atıkları metal geri dönüşüm kutusuna atabilirsiniz.')
    time.sleep(1)
    await ctx.send(f'Pil atıkları pil geri dönüşüm kutusuna atabilirsiniz.')
    time.sleep(1)
    
@bot.command()
async def resim(ctx):
    with open(r'çevre dostu bot\cevre_dostu.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'İşte hangi tür atıkları hangi geri dönüşüm kutusuna atabileceğinizi gösteren bir resim.')





@bot.command()
async def geri_dönüşüm_atıklarını_dogru_yere_atmazsak(ctx):
    await ctx.send(f'İşte birkaç bilgi için "geri_dönüşüm_atmak" yazın')


@bot.command()
async def geri_dönüşüm_atmak(ctx):
    await ctx.send(f'Kirlilik: Atıklar doğru şekilde ayrıştırılmayıp çevreye atıldığında, su, toprak ve hava kirliliğine neden olabilir. Özellikle plastik gibi ayrışması yüzlerce yıl süren malzemeler, doğada kalıcı kirlilik yaratır.')
    time.sleep(2)
    await ctx.send(f'Vahşi yaşam üzerinde olumsuz etkiler: Yanlış atılan atıklar, vahşi yaşam için tehlikeli olabilir. Hayvanlar atıkları yiyecek olarak yanlış algılayabilir, bu da sindirim sistemi tıkanıklıklarına ve hatta ölüme yol açabilir. Ayrıca, su kaynaklarına karışan zararlı maddeler sucul yaşamı tehdit eder.')
    time.sleep(2)
    await ctx.send(f'Kaynakların israfı: Geri dönüşüm atıklarının doğru şekilde ayrıştırılmaması, yeniden kullanılabilecek materyallerin israf edilmesine neden olur. Bu durum, yeni ürünlerin üretimi için daha fazla ham maddeye ve enerjiye ihtiyaç duyulmasına yol açar, bu da doğal kaynakların hızla tükenmesine ve enerji tüketiminin artmasına neden olur.')
    time.sleep(2)
    await ctx.send(f'Geri dönüşüm sürecinin etkinliğinin azalması: Yanlış atılan atıklar, geri dönüşüm tesislerinde ekstra ayrıştırma işlemi gerektirir, bu da işlemin maliyetini ve zamanını artırır. Bazı durumlarda, kirlenmiş veya yanlış ayrıştırılmış atıklar geri dönüştürülemez hale gelebilir ve dolayısıyla çöplüklere yönlendirilir.')
    time.sleep(2)
    await ctx.send(f'Ekonomik kayıplar: Geri dönüşüm süreçlerinin verimliliğinin azalması, belediyeler ve geri dönüşüm tesisleri için ek maliyetlere neden olur. Bu durum, vergilerin artmasına veya geri dönüşüm programlarının finansmanında zorluklara yol açabilir.')
    time.sleep(2)
    await ctx.send(f'İklim değişikliği üzerindeki etkiler: Doğru şekilde ayrıştırılmayan ve geri dönüştürülmeyen atıkların bertarafı genellikle daha fazla sera gazı emisyonuna neden olur. Bu emisyonlar, iklim değişikliğinin etkilerini daha da kötüleştirir.')
    time.sleep(2)


    


bot.run("token")
