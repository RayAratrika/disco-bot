import discord as dc;
import os;

# //need intents for accessing members and certain other details//
bot = dc.Client(intents = dc.Intents.all());

# //on server join//
@bot.event
async def on_guild_join(guild):
	for ch in guild.text_channels: 
		if ch.permissions_for(guild.me).send_messages: 
			#dsc = "Here are some helpful information about me-\ndisco-h - suggest happy songs\ndisco-l - suggest sad songs\ndisco-hello - if you want a greeting from me :)\ndisco-pop - suggest pop songs\ndisco-rock - suggest rocks songs\n AND disco-info for info about me!"
			emb = dc.Embed(
				title = "Hello!", 
				description = "Hi! I'm Disco, a music suggestion bot.\nLet's get ready for some music, shall we?\n\nAdd me to other servers with the link below:\nhttps://discord.com/api/oauth2/authorize?client_id=800048826756890655&permissions=3214400&scope=bot \nHere are some commands I follow:\n",
				color = 0xFFA000);
			emb.add_field(
				name="disco-hello",
				value="Greeting message",
				inline=True);
			emb.add_field(
				name="disco-h",
				value="Suggest happy songs",
				inline=True);
			emb.add_field(
				name="disco-l",
				value="Suggest sad songs",
				inline=True);
			emb.add_field(
				name="disco-info",
				value="Info about the bot",
				inline=True);
			emb.add_field(
				name="disco-pop",
				value="Suggest pop songs of all ages",
				inline=True);
			emb.add_field(
				name="disco-rock",
				value="Suggest rock songs of all ages",
				inline=True);

			await ch.send(embed = emb);
		break;

# //on bot ready//
@bot.event
async def on_ready():
	print(f"{bot.user} ready...")

# //on message on channel//
@bot.event
async def on_message(msg):
	# check if author is bot or not
	if msg.author == bot.user: return;

	#disco-hello: greeting message
	if msg.content == ('disco-hello'):
		dsc = "Hello "+ msg.author.mention +" my musical human fren :)"
		emb = dc.Embed(
			title = "Greetings!", 
			description = dsc, 
			color = 0xFFA000);#  liked- 3D5AFE, B39DDB, 90CAF9, 1123A0

		await msg.channel.send(embed = emb);

	# disco-h: happy songs
	elif msg.content == ('disco-h'):
		emb = dc.Embed(
			title = "Happy Happy Happy!",
			description = "Here are some happy songs for you-\n1.Dancing with myself - Billy Idol\n2.Back in the game - Airbourne\n\nGlad I could take part in your happiness!",
			color = 0x0288D1);

		await msg.channel.send(embed = emb);
	
	# disco-l: sad songs
	elif msg.content == ('disco-l'):
		emb = dc.Embed(
			title = "Feeling Low?", 
			description = "Here are some low songs for you-\n1.Lovely - Billie Eilish ft. Khalid\n2.In loving memeory - Alter Bridge\n\nI'm here if you need me for anything my friend :)",
			color = 0x08bf4b);

		await msg.channel.send(embed = emb);

	# disco-pop: pop songs
	elif msg.content == ('disco-pop'):
		emb = dc.Embed(
			title = "Pop it, Lock it!", 
			description = "Here are some pop songs for you-\n1.Take on me - A-ha\n2.Thunderclouds - Sia, Diplo ft Labyrinth",
			color = 0x00BCD4);

		await msg.channel.send(embed = emb);

	# disco-rock: rock songs
	elif msg.content == ('disco-rock'):
		emb = dc.Embed(
			title = "Rockin' in the free world!", 
			description = "Here are some rock songs for you-\n1.Money for nothing - Dire Straits\n2.While my guitar gently weeps - The beatles",
			color = 0x6A1B9A);

		await msg.channel.send(embed = emb);
	
	# disco-info: info about the bot
	elif msg.content == ('disco-info'):
		emb = dc.Embed(
			title = "Here is some helpful information about me-",
			color = 0xFFA000);
		emb.add_field(
			name="disco-hello",
			value="Greeting message",
			inline=True);
		emb.add_field(
			name="disco-h",
			value="Suggest happy songs",
			inline=True);
		emb.add_field(
			name="disco-l",
			value="Suggest sad songs",
			inline=True);
		emb.add_field(
			name="disco-pop",
			value="Suggest pop songs of all ages",
			inline=True);
		emb.add_field(
			name="disco-rock",
			value="Suggest rock songs of all ages",
			inline=True);
		emb.add_field(
			name="disco-info",
			value="Info about the bot",
			inline=True);

		await msg.channel.send(embed = emb);
		#msg.add_reaction("👀");
	
	# mentionong the bot
	if bot.user.mentioned_in(msg) and msg.mention_everyone is False:
		#dsc = "Hello "+ msg.author.mention +" my musical human fren :)"
		emb = dc.Embed(
			title = "I'm needed?!", 
			description = f"Yes {msg.author.mention} how can I be of help to you?\n\nTry out these commands-\n>> disco-h\n>> disco-l\n>> disco-hello\n>> disco-pop\n>> disco-rock\n>> disco-info", 
			color = 0xFFA000);
		await msg.channel.send(embed = emb);


bot.run("ODAwMDQ4ODI2NzU2ODkwNjU1.YAMdiA.0zFHlzXi2zTi6w_ENZa5Ba8irGM")